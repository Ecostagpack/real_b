import asyncpg
import asyncio
import logging
import contextlib

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart

from core.handlers.basic import get_start
from core.middlewares.dbmiddleware import DbSession
from core.settings import settings
from core.utils.commands import set_commands
from aiogram.types.message import Message, ContentType
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.utils.dbconnect import Request
from core.handlers import sender_intertop, apsched
from core.middlewares.apschedulermiddleware import SchedulerMiddleware
from core.utils.sender_list_intertop import SenderListIntertop
from core.utils.sender_state import Steps
from datetime import datetime, timedelta





async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, 'Бот запущено')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Бот зупинено')


async def create_pool():
    # return await asyncpg.create_pool(user='postgres', password='RQJdRIM71-jCw', database='users',
    #                           host='127.0.0.1', port=5432, command_timeout=60)
    return await asyncpg.create_pool(user=settings.db.db_user, password=settings.db.db_password,
                                     database=settings.db.db_database, host=settings.db.db_host,
                                     port=5432, command_timeout=60)



async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    pool_connect = await create_pool()
    dp = Dispatcher()
    senderlistintertop = SenderListIntertop
    scheduler = AsyncIOScheduler(timezone='Europe/Kyiv')
    scheduler.add_job(apsched.send_message_free, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                      kwargs={'bot': bot, 'senderlistintertop': senderlistintertop})
    # scheduler = AsyncIOScheduler(timezone='Europe/Kyiv')
    # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour='11',
    #                   minute='58', start_date=datetime.now(), kwargs={'bot': bot, name_table, senderlistintertop})
    # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour='8',
    #                   minute='15', start_date=datetime.now(), kwargs={'bot': bot, 'senderlistintertop': SenderListIntertop})
    # scheduler.add_job(apsched.get_ids_cron, trigger='cron', hour='8', minute='11', start_date=datetime.now(),
    #                   kwargs={'bot': bot, 'message': Message, 'request': Request})
    scheduler.start()
    dp.update.middleware.register(DbSession(pool_connect))
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    # dp.message.register(Inter_skidki_women, F.text == 'skidki_women')
    # dp.message.register(Inter_skidki_men, F.text == 'skidki_men')
    # dp.message.register(Inter_skidki_children, F.text == 'skidki_children')
    dp.message.register(get_start, F.text == '/start')
    # dp.message.register(get_hellow, F.text == 'привет')
    # dp.message.register(get_photo, F.photo)
    # dp.message.register(get_start, Command(commands=['start', 'run']))
    # dp.message.register(sender.get_sender, Command(commands='sender', magic=F.args),
    #                                       F.chat.id == settings.bots.admin_id)

    # dp.message.register(sender.get_message, Steps.get_message)
    # dp.callback_query.register(sender.q_button, Steps.q_button)
    # dp.message.register(sender.get_text_button, Steps.get_text_button, F.chat.id == settings.bots.admin_id)
    # dp.message.register(sender.get_url_button, Steps.get_url_button, F.chat.id == settings.bots.admin_id, F.text)
    dp.message.register(sender_intertop.sender_decide, F.text == '/run')
    sender_list_intertop = SenderListIntertop(bot, pool_connect)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), senderlistintertop=sender_list_intertop)
    except Exception as ex:
        logging.error(f"[!!! Exeption] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
