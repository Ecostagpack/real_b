# from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram import Bot
# from aiogram.filters import CommandObject
# from aiogram.fsm.context import FSMContext
#
# from core.utils.dbconnect import Request
# from core.utils.sender_list import SenderList
# from core.utils.sender_state import Steps
# from core.keyboards.inline_sender import get_confirm_button_keyboard
#
#
# async def get_sender(message: Message, command: CommandObject, state: FSMContext):
#     if not command.args:
#         await message.answer(f"Для створення кампаніі для розсилки введи команду /sender і текст для розсилки")
#         return
#     await message.answer(f"Починаємо розсилку. Ім'я кампаніі {command.args}\r\n\r\n"
#                          f"Відправ мені контент, який буде вікористано як рекламне повідомлення")
#     await state.update_data(name_camp=command.args)
#     await state.set_state(Steps.get_message)
#
#
# async def get_message(message: Message, state: FSMContext):
#     await message.answer(f"Ок, я запам'ятав повідомлення для розсилки\r\n\r\n"
#                          f"Кнопку будемо добавляти?", reply_markup=get_confirm_button_keyboard())
#     await state.update_data(message_id=message.message_id, chat_id=message.from_user.id)
#     await state.set_state(Steps.q_button)
#
# async def q_button(call: CallbackQuery, bot: Bot, state: FSMContext):
#     if call.data == 'add_button':
#         await call.message.answer(f"Відправ текст для кнопки", reply_markup=None)
#         await state.set_state(Steps.get_text_button)
#     elif call.data == 'no_button':
#         await call.message.edit_reply_markup(reply_markup=None)
#         data = await state.get_data()
#         message_id = int(data.get('message_id'))
#         chat_id = int(data.get('chat_id'))
#         await confirm(call.message, bot, message_id, chat_id)
#         await state.set_state(Steps.get_url_button)
#
#     await call.answer()
#
# async def get_text_button(message: Message, state: FSMContext):
#     await state.update_data(text_button=message.text)
#     await message.answer(f"Тепер надішли посилання")
#     await state.set_state(Steps.get_url_button)
#
# async def get_url_button(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(url_button=message.text)
#     added_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text=(await state.get_data()).get('text_button'),
#                 url=f"{message.text}"
#             )
#         ]
#     ])
#     data = await state.get_data()
#     message_id = int(data.get('message_id'))
#     chat_id = int(data.get('chat_id'))
#     await confirm(message, bot, message_id, chat_id, added_keyboard)
#
# async def confirm(message: Message, bot: Bot, message_id: int, chat_id: int, reply_markup: InlineKeyboardMarkup = None):
#     await bot.copy_message(chat_id, chat_id, message_id, reply_markup=reply_markup)
#     await message.answer(f"Ось повідомлення, яке буде розіслане. Підтверди будьласка",
#                          reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                              [
#                                  InlineKeyboardButton(
#                                      text='confirm',
#                                      callback_data='confirm_sender'
#
#                                  )
#                              ],
#                              [
#                                  InlineKeyboardButton(
#                                      text='Скасувати',
#                                      callback_data='cansel_sender'
#
#                                  )
#                              ]
#                          ]))
#
# async def sender_decide(call: CallbackQuery, bot: Bot, state: FSMContext, request: Request, senderlist: SenderList):
#     data = await state.get_data()
#     message_id = data.get('message_id')
#     chat_id = data.get('chat_id')
#     text_button = data.get('text_button')
#     url_button = data.get('url_button')
#     name_camp = data.get('name_camp')
#
#     if call.data == 'confirm_sender':
#         await call.message.edit_text(f"Починаю розсилку", reply_markup=None)
#
#         if not await request.check_table(name_camp):
#             await request.create_table(name_camp)
#         count = await senderlist.broadcaster(name_camp, chat_id, message_id, text_button, url_button)
#         await call.message.answer(f"повідомлення успішно розіслано [{count}] користувачам")
#         await request.delete_table(name_camp)
#
#     elif call.data == 'cansel_sender':
#         await call.message.edit_text(f"Розсилку зупинено", reply_markup=None)
#
#     await state.clear()

# 7777777777777777777777777777777777777777777777777777777777777777

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from core.keyboards.inline_sender import get_confirm_button_keyboard
from core.utils.dbconnect import Request
from core.utils.sender_list import SenderList
from core.utils.sender_state import Steps



# async def get_sender(message: Message, command: CommandObject, state: FSMContext):
#     if not command.args:
#         await message.answer(f"Для створення кампаніі для розсилки введи команду /sender і текст для розсилки")
#         return
#     await message.answer(f"Починаємо розсилку. Ім'я кампаніі {command.args}\r\n\r\n"
#                          f"Відправ мені контент, який буде вікористано як рекламне повідомлення")
#     await state.update_data(name_camp=command.args)
#     await state.set_state(Steps.get_message)
async def get_sender(message: Message, command: CommandObject, state: FSMContext):
    if not command.args:
        await message.answer(f"Для створення кампаніі для розсилки введи команду /sender і текст для розсилки")
        return
    await message.answer(f"Починаємо розсилку. Ім'я кампаніі {command.args}\r\n\r\n"
                         f"Відправ мені контент, який буде вікористано як рекламне повідомлення")
    await state.update_data(name_camp=command.args)
    await state.set_state(Steps.get_message)

async def get_message(message: Message, state: FSMContext):
    await message.answer(f"Ок, я запам'ятав повідомлення для розсилки\r\n\r\n"
                         f"Кнопку будемо добавляти?", reply_markup=get_confirm_button_keyboard())
    await state.update_data(message_id=message.message_id, chat_id=message.from_user.id)
    await state.set_state(Steps.q_button)

async def q_button(call: CallbackQuery, bot: Bot, state: FSMContext):
    if call.data == 'add_button':
        await call.message.answer(f"Відправ текст для кнопки", reply_markup=None)
        await state.set_state(Steps.get_text_button)
    elif call.data == 'no_button':
        await call.message.edit_reply_markup(reply_markup=None)
        data = await state.get_data()
        message_id = int(data.get('message_id'))
        chat_id = int(data.get('chat_id'))
        await confirm(call.message, bot, message_id, chat_id)
        await state.set_state(Steps.get_text_button)

    await call.answer()

async def get_text_button(message: Message, state: FSMContext):
    await state.update_data(text_button=message.text)
    await message.answer(f"Тепер надішли посилання")
    await state.set_state(Steps.get_url_button)

async def get_url_button(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(url_button=message.text)
    added_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=(await state.get_data()).get('text_button'),
                url=f"{message.text}"
            )
        ]
    ])
    data = await state.get_data()
    message_id = int(data.get('message_id'))
    chat_id = int(data.get('chat_id'))
    await confirm(message, bot, message_id, chat_id, added_keyboard)

async def confirm(message: Message, bot: Bot, message_id: int, chat_id: int, reply_markup: InlineKeyboardMarkup = None):
    await bot.copy_message(chat_id, chat_id, message_id, reply_markup=reply_markup)
    await message.answer(f"Ось повідомлення, яке буде розіслане. Підтверди будь ласка",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                             [
                                 InlineKeyboardButton(
                                     text='confirm',
                                     callback_data='confirm_sender'

                                 )
                             ],
                             [
                                 InlineKeyboardButton(
                                     text='Скасувати',
                                     callback_data='cansel_sender'

                                 )
                             ]
                         ]))

async def sender_decide(call: CallbackQuery, bot: Bot, state: FSMContext, request: Request, senderlist: SenderList):
    data = await state.get_data()
    message_id = data.get('message_id')
    chat_id = data.get('chat_id')
    text_button = data.get('text_button')
    url_button = data.get('url_button')
    name_camp = data.get('name_camp')

    if call.data == 'confirm_sender':
        await call.message.edit_text(f"Починаю розсилку", reply_markup=None)

        if not await request.check_table(name_camp):
            await request.create_table(name_camp)
        count = await senderlist.broadcaster(name_camp, chat_id, message_id, text_button, url_button)
        await call.message.answer(f"повідомлення успішно розіслано [{count}] користувачам")
        await request.delete_table(name_camp)

    elif call.data == 'cansel_sender':
        await call.message.edit_text(f"Розсилку зупинено", reply_markup=None)

    await state.clear()



















