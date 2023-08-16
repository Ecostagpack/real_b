from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import get_reply_keyboard
from core.utils.dbconnect import Request


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.answer(f"Привіт, {message.from_user.first_name}, радий тебе бачити, в меню обери послугу")


async def pokaz_znyzky(message: Message, bot: Bot):
    await message.answer('Обери знижки', reply_markup=get_reply_keyboard())


async def Inter_skidki(message: Message):
    await message.answer('please waiting...')

    with open('datas/data_card.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count = 0
        for card in data_card:
            count += 1
            item = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"

            await message.answer(item)


async def Inter_skidki_men(message: Message):
    await message.answer('please waiting...')

    with open('datas/data_card_men.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count = 0
        for card in data_card:
            count += 1
            item = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"

            await message.answer(item)


async def Inter_skidki_children(message: Message):
    await message.answer('please waiting...')

    with open('datas/data_card_children.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count = 0
        for card in data_card:
            count += 1
            item = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"

            await message.answer(item)
