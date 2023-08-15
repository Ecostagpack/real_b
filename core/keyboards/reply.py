from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='skidki_women')
    keyboard_builder.button(text='skidki_men')
    keyboard_builder.button(text='skidki_children')
    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True)
#     # return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
#
#
#
#     # keyboard_builder.button(text='кнопка 2')
#     # keyboard_builder.button(text='кнопка 3')
#     # keyboard_builder.button(text='відправити геолокацію',request_location=True)
#     # keyboard_builder.button(text='відправити контакт', request_contact=True)
#     # keyboard_builder.button(text='створити вікторину', request_poll=KeyboardButtonPollType())
#     # keyboard_builder.adjust(3, 2, 1)
#     #     input_field_placeholder='відправ локацію, номер телефону, або створи вікторину')
#
#
#
# # reply_keyboard = ReplyKeyboardMarkup(keyboard=[
# #     [
# #         KeyboardButton(
# #             text='ряд 1. кнопка 1'
# #         ),
# #         KeyboardButton(
# #             text='ряд 1. кнопка 2'
# #         ),
# #         KeyboardButton(
# #             text='ряд 1. кнопка 3'
# #         ),
# #     ],
# #     [
# #         KeyboardButton(
# #             text='ряд 2. кнопка 1'
# #         ),
# #         KeyboardButton(
# #             text='ряд 2. кнопка 2'
# #         ),
# #         KeyboardButton(
# #             text='ряд 2. кнопка 3'
# #         ),
# #         KeyboardButton(
# #             text='ряд 2. кнопка 4'
# #         )
# #     ],
# #     [
# #         KeyboardButton(
# #             text='ряд 3. кнопка 1'
# #         ),
# #         KeyboardButton(
# #             text='ряд 3. кнопка 2'
# #         )
# #     ]
# #     ], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='обери кнопку', selective=True)
# #
# # loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
# #     [
# #         KeyboardButton(
# #             text='відправити геолокацію',
# #             request_location=True
# #         )
# #     ],
# #     [
# #         KeyboardButton(
# #             text='відправити свій контакт',
# #             request_contact=True
# #         )
# #     ],
# #     [
# #         KeyboardButton(
# #             text='створити вікторину',
# #             request_poll=KeyboardButtonPollType()
# #         )
# #     ]], resize_keyboard=True, one_time_keyboard=False,
# #         input_field_placeholder='відправ локацію, номер телефону, або створи вікторину')


