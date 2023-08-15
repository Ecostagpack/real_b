# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from core.utils.callbackdata import MacInfo, InterInfo
# # from core.handlers.callback import select_znyzka
# import json
#
# # select_macbook = InlineKeyboardMarkup(inline_keyboard=[
# #     [
# #         InlineKeyboardButton(
# #             text='Macboock Air 13" M1 2020',
# #             callback_data='apple_air_13_m1_2020'
# #         )
# #     ],
# #     [
# #         InlineKeyboardButton(
# #             text='Macboock Pro 14" M1 2020',
# #             callback_data='apple_pro_14_m1_2020'
# #         )
# #     ],
# #     [
# #         InlineKeyboardButton(
# #             text='Macboock Pro 16" 2019',
# #             callback_data='apple_pro_16_i7_2019'
# #         )
# #     ],
# #     [
# #         InlineKeyboardButton(
# #             text='link',
# #             url='https://nztcoder.com/'
# #         )
# #     ],
# #     [
# #         InlineKeyboardButton(
# #             text='Profile',
# #             url='tg://User?Id=1498055556'
# #         )
# #     ]
# # ])
#
#
# def get_inline_keyboard():
#
#
#     keyword_builder = InlineKeyboardBuilder()
#     keyword_builder.button(text='Macboock Air 13" M1 2020', callback_data=MacInfo(model='air', size=13, chip='m1',year=2020))
#     keyword_builder.button(text='Macboock Air 14" M1 2021', callback_data=MacInfo(model='pro', size=14, chip='m1',year=2021))
#     # keyword_builder.button(text='intertop', callback_data=InterInfo(link='link', model='model',
#     #                         brend='brend',  old_price='old_price', action_price='action_price', znizka='znizka'))
#     keyword_builder.button(text='intertop', callback_data='answer')
#
#     keyword_builder.button(text='link', url='https://nztcoder.com/')
#     keyword_builder.button(text='Profile', url='tg://User?Id=1498055556')
#     keyword_builder.adjust(3)
#     return keyword_builder.as_markup()