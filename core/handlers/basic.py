from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import get_reply_keyboard
from core.utils.dbconnect import Request


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    # await bot.send_message(message.from_user.id, f"Привіт, {message.from_user.first_name}, радий тебе бачити")
    await message.answer(f"Привіт, {message.from_user.first_name}, радий тебе бачити",
                         reply_markup=get_reply_keyboard())
    await message.answer(f"Привіт, {message.from_user.first_name}, радий тебе бачити")


async def get_photo(message: Message, bot: Bot):
    await message.answer('Ок, ти відправив мені картинку, я збережу її')

    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'fotka.jpg')


async def get_hellow(message: Message, bot: Bot):
    await message.answer('І тобі привіт')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)


# from aiogram.filters import CommandObject

# from core.utils.dbconnect import Request
#
#
# async def add_trigger(message: Message, command: CommandObject, request: Request):
#     name_trigger = command.args.replace(' ', '_')
#     value_trigger = message.reply_to_message.message_id
#     await request.add_trigger(name_trigger, value_trigger)
#     await message.answer(f'Триггер {name_trigger} добавлен')
#     print(message.chat.id)
#
#
# async def get_triggers(message: Message, request: Request):
#     msg = await request.get_triggers()
#     await message.answer(msg, parse_mode="MARKDOWN")
#
#
# async def get_values(message: Message, bot: Bot, request: Request):
#     values = await request.get_values(message.text.replace('#', ''))
#     list_values = values.split('\r\n')
#
#     for value in list_values:
#         await bot.copy_message(message.chat.id, message.chat.id, int(value))


# 7777777777777777777777777777777777
# from aiogram import Bot
# from aiogram.types import Message
# # from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
# from core.keyboards.reply import get_reply_keyboard
# # from core.keyboards.inline import select_macbook, get_inline_keyboard
# from aiogram.types import Message, ContentType
# # from core.handlers.callback import select_znyzka
# from core.keyboards.inline import get_inline_keyboard
# from core.utils.dbconnect import Request
# import json
# import asyncio
#
#
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
#
#
# async def get_start(message: Message, bot: Bot, request: Request):
#     await request.add_data(message.from_user.id, message.from_user.first_name)
#     # await message.answer(f"Повідомлення # {counter}")
#     await message.answer(f"Привет {message.from_user.first_name}, радий тебе бачити."
#                          f" Натисни кнопки 'skidki' та 'skidki_men',щоб переглянути знижки на взуття"
#                          f" у мережі магазинів INTERTOP",
#                         reply_markup=get_reply_keyboard())
#
#
#
# # async def get_inline(message: Message, bot: Bot):
# #     await message.answer(f"Привіт, {message.from_user.first_name},передаю тобі інлайн клавіатуру",
# #                          reply_markup=get_inline_keyboard())
#
#
#
#
#
# # async def get_location(message: Message, bot: Bot):
# #     await message.answer(f"Ти відправив свою геолкацію\r\a"
# #                          f"{message.location.latitude}\r\n{message.location.latitude}")
# #
# #
# # async def get_photo(message: Message, bot: Bot):
# #     await message.answer(f"ОК. Ти відправив мені картинку. Я збережу її собі")
# #     file = await bot.get_file(message.photo[-1].file_id)
# #     await bot.download_file(file.file_path, 'photo.jpg')
