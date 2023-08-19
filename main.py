import asyncpg
import asyncio
import logging
import contextlib

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

# from core.utils.sender_list_intertop import send_message_to_clients
from core.handlers.basic import get_start, pokaz_znyzky
from core.middlewares.dbmiddleware import DbSession
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.inertop import Inter_skidki_women, Inter_skidki_men, Inter_skidki_children
from aiogram.types.message import Message, ContentType
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.utils.dbconnect import Request
from core.handlers import sender_intertop, apsched, sender
from core.middlewares.apschedulermiddleware import SchedulerMiddleware
from core.utils.sender_list import SenderList
# from core.utils.sender_list_intertop import SenderListIntertop
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
    # senderlist = SenderList
    scheduler = AsyncIOScheduler(timezone='Europe/Kyiv')
    scheduler.add_job(apsched.send_message_interval, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                      kwargs={'bot': bot})
    # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour='8',
    #                   minute='15', start_date=datetime.now(), kwargs={'bot': bot, 'senderlistintertop': SenderListIntertop})
    # scheduler.add_job(apsched.get_ids_cron, trigger='cron', hour='8', minute='11', start_date=datetime.now(),
    #                   kwargs={'bot': bot, 'message': Message, 'request': Request})
    scheduler.start()
    dp.update.middleware.register(DbSession(pool_connect))
    # dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    # dp.callback_query.register(send_message_to_clients, F.data.in_(['rozislaty', 'ne_rozsylaty']))
    dp.message.register(pokaz_znyzky, F.text == '/znyzky')
    dp.message.register(Inter_skidki_women, F.text == 'skidki_women')
    dp.message.register(Inter_skidki_men, F.text == 'skidki_men')
    dp.message.register(Inter_skidki_children, F.text == 'skidki_children')
    dp.message.register(get_start, F.text == '/start')
    dp.message.register(sender.get_sender, Command(commands='sender', magic=F.args),
                                          F.chat.id == settings.bots.admin_id)
    #
    dp.message.register(sender.get_message, Steps.get_message)
    dp.callback_query.register(sender.q_button, Steps.q_button)
    dp.message.register(sender.get_text_button, Steps.get_text_button, F.chat.id == settings.bots.admin_id)
    dp.message.register(sender.get_url_button, Steps.get_url_button, F.chat.id == settings.bots.admin_id, F.text)
    dp.callback_query.register(sender.sender_decide, F.data.in_(['confirm_sender', 'cansel_sender']))
    sender_list = SenderList(bot, pool_connect)
    # sender_list_intertop = SenderListIntertop(bot, pool_connect)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), senderlist=sender_list)
        # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), senderlistintertop=sender_list_intertop)
    except Exception as ex:
        logging.error(f"[!!! Exeption] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())








# import contextlib
#
# from aiogram import Bot, Dispatcher, F
# import asyncio
# import logging
#
# from aiogram.filters import Command
#
# from core.settings import settings
#
# from core.utils.commands import set_commands
# from core.middlewares.dbmiddleware import DbSession
# import asyncpg
#
# from core.handlers import basic
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
#
# async def start_bot(bot: Bot):
#     await set_commands(bot)
#     await bot.send_message(settings.bots.admin_id, text='Бот запущен!')
#
#
# async def stop_bot(bot: Bot):
#     await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')
#
#
# async def create_pool():
#     return await asyncpg.create_pool(user='postgres', password='RQJdRIM71-jCw', database='users',
#                                      host='127.0.0.1', port=5432, command_timeout=60)
#
#
# async def start():
#     logging.basicConfig(level=logging.INFO,
#                         format="%(asctime)s - [%(levelname)s] -  %(name)s - "
#                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
#                         )
#
#     bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
#     pool_connect = await create_pool()
#     dp = Dispatcher()
#     dp.update.middleware.register(DbSession(pool_connect))
#     dp.startup.register(start_bot)
#     dp.shutdown.register(stop_bot)
#
#     dp.message.register(basic.add_trigger, Command(commands='add_trigger', magic=F.args), F.reply_to_message)
#     dp.message.register(basic.get_triggers, Command(commands='get_triggers'))
#     dp.message.register(basic.get_values, F.text.startswith('#'))
#     try:
#         await dp.start_polling(bot)
#     finally:
#         await bot.session.close()
#
#
# if __name__ == "__main__":
#     with contextlib.suppress(KeyboardInterrupt, SystemExit):
#         asyncio.run(start())




# import asyncpg
# import asyncio
# import logging
# import contextlib
#o
# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command, CommandStart
# from core.middlewares.dbmiddleware import DbSession
# from core.settings import settings
# from core.utils.commands import set_commands
#
# from aiogram.types import Message, ContentType
# from core.handlers.basic import get_start
# from core.filters.iscontaсt import IsTrueContact
# # from core.handlers.contact import get_true_contact, get_fake_contact
#
#
#
# import json
# from typing import Dict
#
# # from core.handlers.basic import get_location
# # from core.handlers.basic import get_inline
# # from core.handlers.callback import select_macbook, select_znyzka
# # from core.handlers.callback import select_znyzka
# from core.utils.callbackdata import MacInfo
# from core.middlewares.countermiddleware import CounterMiddleware
# # from core.middlewares.officehours import OfficeHoursMiddelware
#
# from core.middlewares.apschedulermiddleware import SchedulerMiddleware
#
# from core.handlers import form
# from core.utils.sender_list import SenderList
# from core.utils.statesform import StapsForm
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from core.handlers import apsched
# from datetime import datetime, timedelta
# from core.handlers import sender
# from core.utils.sender_state import Steps
#
#
# async def start_bot(bot: Bot):
#     await set_commands(bot)
#     await bot.send_message(settings.bots.admin_id, text='бот запущено')
#
# async def stop_bot(bot: Bot):
#     await bot.send_message(settings.bots.admin_id, text='бот зупинено')
#
# async def create_pool():
#     return await asyncpg.create_pool(user='postgres', password='RQJdRIM71-jCw', database='users',
#                                      host='127.0.0.1', port=5432, command_timeout=60)
# # async def create_pool():
# #     return await asyncpg.create_pool(user=settings.db.db_user, password=settings.db.db_password,
# #                                      database=settings.db.db_database, host=settings.db.db_host, port=5432,
# #                                      command_timeout=60)
#
# # async def get_text(message:Message):
# #     await message.answer(f"Вы прислали текстовое сообщение")
# #
# # async def get_hello(message: Message):
# #     await message.answer("привет")
#
# async def start():
#     logging.basicConfig(level=logging.DEBUG,
#                         format="%(asctime)s -[%(levelname)s] - %(name)s - (%(filename)s).%(funcName)"
#                                "s(%(lineno)d)-%(message)s"
#                         )
#
#     bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
#     pool_connect = await create_pool()
#     dp = Dispatcher()
#     dp.update.middleware.register(DbSession(pool_connect))
#     dp.startup.register(start_bot)
#     dp.shutdown.register(stop_bot)
#     # scheduler = AsyncIOScheduler(timezone='Europe/Kyiv')
#     # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour='12',
#     #                   minute='29', start_date=datetime.now(), kwargs={'bot': bot})
#     # scheduler.start()
#
#     # dp.message.middleware.register(CounterMiddleware())
#     # dp.update.middleware.register(OfficeHoursMiddelware())
#     # dp.update.middleware.register(SchedulerMiddleware(scheduler))
#
#
#     dp.message.register(sender.get_sender, Command(commands='sender', magic=F.args),
#                         F.chat.id == settings.bots.admin_id)
#     dp.message.register(sender.get_message, Steps.get_message, F.chat.id == settings.bots.admin_id)
#
#     dp.callback_query.register(sender.q_button, Steps.q_button)
#     dp.message.register(sender.get_text_button, Steps.get_text_button,
#                         F.chat.id == settings.bots.admin_id)
#     dp.message.register(sender.get_url_button, Steps.get_url_button,
#                         F.chat.id == settings.bots.admin_id, F.text)
#     #
#     # dp.message.register(form.get_form, Command(commands='form'))
#     # dp.message.register(form.get_name, StapsForm.GET_NAME)
#     # dp.message.register(form.get_last_name, StapsForm.GET_LAST_NAME)
#     # dp.message.register(form.get_age, StapsForm.GET_AGE)
#     # dp.message.register(get_inline, Command(commands=['inline']))
#     # dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro'))
#     # dp.message.register(get_location, F.content_type == ContentType.LOCATION)
#     # dp.message.register(get_photo, F.photo)
#     # dp.message.register(get_start, Command(commands=['start']))
#     # dp.message.register(get_true_contact)
#     # dp.message.register(get_fake_contact)
#     dp.callback_query.register(sender.sender_decide, F.data.in_(['confirm_sender', 'cansel_sender']))
#     sender_list = SenderList(bot, pool_connect)
#     try:
#         await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), senderlist=sender_list)
#         # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
#     except Exception as ex:
#         logging.error(f"[!!! Exception] - {ex}", exc_info=True)
#     finally:
#         await bot.session.close()
#
#
# if __name__ == '__main__':
#     with contextlib.suppress(KeyboardInterrupt, SystemExit):
#         asyncio.run(start())
#
#
#     # dp.message.register(get_hello, F.text.lower().startswith('привет'))
#     # dp.message.register(get_text, F.text)
#
#     # dp.message.register(get)
#
#     # dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
#
#     # async def get(message: Message):
#     #     data_message = message.dict()
#     #     print(json.dumps(data_message, default=str))
#     #     result_data_message = await get_data_message(data_message=data_message)
#     #     for key, value in result_data_message.items():
#     #         print(f"{key} - {value}")
#     #         if isinstance(value, str):
#     #             print(f'используя magic_filter к данным {key} можно обратиться через F.{key} == "{value}"')
#     #         elif isinstance(value, int):
#     #             print(f'используя magic_filter к данным {key} можно обратиться через F.{key} == {value}')
#
#     # async def get_data_message(data_message: Dict, prefix: str = '', sep: str = '.'):
#     #     correct_dict = {}
#     #     for key, value in data_message.items():
#     #         if isinstance(value, Dict):
#     #             correct_dict.update(await get_data_message(data_message=value, prefix=f'{prefix}{key}{sep}'))
#     #         else:
#     #             correct_dict[f"{prefix}{key}"] = value
#     #     return correct_dict
#     # dp.message.register(get_start, F.text == '/start')