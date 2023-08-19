from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import get_reply_keyboard
from core.utils.dbconnect import Request
from core.utils.dbconnect import Request
from core.utils.sender_list import SenderList
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from core.handlers.apsched import send_message_middleware
from datetime import datetime, timedelta
# from core.utils.sender_list_intertop import SenderListIntertop


# async def Inter_sk_wo(message: Message, bot: Bot, apscheduler: AsyncIOScheduler, sendlistint: SenderListIntertop):
#     with open('datas/data_card.json', 'r', encoding='utf-8') as file:
#         data_card = json.load(file)
#         count = 0
#         for card in data_card:
#             count += 1
#             item_women = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
#                    f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"
#             # return item_women
#             # await message.answer(item_women)
#         apscheduler.add_job(send_message_middleware, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
#                             kwargs={bot: bot, 'chat_id': sendlistint.get_users2()})

async def Inter_skidki_women(message: Message):
    await message.answer('please waiting...')

    with open('datas/data_card.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count_women = 0
        for card in data_card:
            count_women += 1
            item_women = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"
            # return item_women
            await message.answer(item_women)


async def Inter_skidki_men(message: Message):
    await message.answer('please waiting...')

    with open('datas/data_card_men.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count_men = 0
        for card in data_card:
            count_men += 1
            item_men = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"

            await message.answer(item_men)


async def Inter_skidki_children(message: Message):
    await message.answer('please waiting...')

    with open('datas/data_card_children.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count_children = 0
        for card in data_card:
            count_children += 1
            item_children = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"

            await message.answer(item_children)