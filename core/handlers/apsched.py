from aiogram import Bot
import json
import datetime

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard
import psycopg_pool
# from core.utils.sender_list_intertop import SenderListIntertop
from core.utils.dbconnect import Request
from core.keyboards.inline_sender import dobavlyaty_button_keyboard
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from core.utils.sender_state import Steps_Intertop


async def send_message_interval(bot: Bot):
    today = datetime.date.today()
    with open('datas/data_card.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        count_women = 0
        for card in data_card:

            item_women = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
                   f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"
            count_women += 1

            # return item_women
    await bot.send_message(1498055556,
                    f"{today}\nПривіт.\nЗнайдено нові знижки на взуття в иережі  Інтертоп.\n"
                    f" {count_women} нових товарів\n\nЩоб переглянути, натисни кнопки intertop")
    await bot.send_message(1498055556,
                           f"/sender intertop")

    #     with open('datas/data_card.json', 'r', encoding='utf-8') as file:
    #         data_card = json.load(file)
    #         count_women = 0
    #         for card in data_card:
    #             count_women += 1
    #             # item_women = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
    #             #              f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"
    #
    #
    #     with open('datas\data_card_men.json', 'r', encoding=' utf-8') as file:
    #         data_card = json.load(file)
    #         count_men = 0
    #         for card in data_card:
    #             count_men += 1
    #
    #     with open('datas\data_card_children.json', 'r', encoding=' utf-8') as file:
    #         data_card = json.load(file)
    #         count_children = 0
    #         for card in data_card:
    #             count_children += 1
    #
    #     await bot.send_message(1498055556, f"Привіт. з'явилося {count_women} одиниць жіночого взуття, {count_men} одиниць\r\n"
    #                                        f" чоловічого взуття, {count_children} одиниць дитячого взуття зі знижками.\r\n ")



# async def create_message_for_clients(message: Message, state: FSMContext):
#     await state.update_data(message_id=message.message_id, chat_id=message.from_user.id)


# async def send_message_free(bot: Bot, senderlistintertop: SenderListIntertop):
#     users_ids = await senderlistintertop.get_users(self=senderlistintertop)
#     for user_id in users_ids:
#         await bot.send_message(str(user_id), 'повідомлення по графіку')


# async def get_ids_cron(bot: Bot, message: Message, request: Request):
#     ids = await request.get_triggers()
#
#     for id in ids:
#         print(id)
#
#
# # #
# # #
# async def send_message_middleware(bot: Bot, chat_id: int):
#     await bot.send_message(chat_id, f"це повідомлення відправлено за допомогою міддлварі")
#
# # async def send_message_refresh_cron(bot: Bot, senderlist: SenderList, name_table):
# async def send_message_refresh_cron(bot: Bot, senderlistintertop: SenderListIntertop, name_table):
#     with open('datas/data_card.json', 'r', encoding='utf-8') as file:
#         data_card = json.load(file)
#         count_women = 0
#         for card in data_card:
#             count_women += 1
#             # item_women = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n" \
#             #              f"<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"
#
#
#     with open('datas\data_card_men.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count_men = 0
#         for card in data_card:
#             count_men += 1
#
#     with open('datas\data_card_children.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count_children = 0
#         for card in data_card:
#             count_children += 1
#
#     users_ids = await senderlistintertop.get_users(name_table)
#     for user_id in users_ids:
#
#         await bot.send_message(user_id, f"Привіт. з'явилося {count_women} одиниць жіночого взуття, {count_men} одиниць\r\n"
#                                        f" чоловічого взуття, {count_children} одиниць дитячого взуття зі знижками.\r\n "
#                                        f"Щоб переглянути, натисни SKIDKI, SKIDKI_MEN, SKIDKI_CHILDREN", reply_markup=get_reply_keyboard())

    # count = await senderlist.broadcaster(name_table)
    # await bot.(f"повідомлення успішно розіслано [{count}] користувачам")

# async def send_message_refresh_cron(bot: Bot):
#     with open('datas\data_card.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count = 0
#         for card in data_card:
#             count +=1
#
#     with open('datas\data_card_men.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count_men = 0
#         for card in data_card:
#             count_men += 1
#
#     with open('datas\data_card_children.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count_children = 0
#         for card in data_card:
#             count_children += 1
#
#     await bot.send_message(1498055556, f"Привіт. з'явилося {count} одиниць жіночого взуття, {count_men} одиниць\r\n"
#                                        f" чоловічого взуття, {count_children} одиниць дитячого взуття зі знижками.\r\n "
#                                        f"Щоб переглянути, натисни SKIDKI, SKIDKI_MEN, SKIDKI_CHILDREN", reply_markup=get_reply_keyboard())
# async def send_message_refresh_cron(self, bot: Bot):
# # , name_table, user_id
# # async def send_message_refresh_cron(bot: Bot, sender_list: Sender_list):
#     request = Request
#     with open('datas\data_card.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count = 0
#         for card in data_card:
#             count += 1
#
#     with open('datas\data_card_men.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count_men = 0
#         for card in data_card:
#             count_men += 1
#
#     with open('datas\data_card_children.json', 'r', encoding=' utf-8') as file:
#         data_card = json.load(file)
#         count_children = 0
#         for card in data_card:
#             count_children += 1
#     name_table = 'datausers'
#     user_id = await self.get_user(name_table)
#     # users_id = await sender_list.get_users(name_table)
#     await bot.send_message(chat_id=user_id, text=f"Привіт. з'явилося {count} одиниць жіночого взуття, {count_men} одиниць\r\n"
#                                        f" чоловічого взуття, {count_children} одиниць дитячого взуття зі знижками.\r\n "
#                                        f"Щоб переглянути, натисни SKIDKI, SKIDKI_MEN, SKIDKI_CHILDREN", reply_markup=get_reply_keyboard())
#     # await bot.send_message(user_id, f"Привіт. з'явилося {count} одиниць жіночого взуття, {count_men} одиниць\r\n"
#     #                                    f" чоловічого взуття, {count_children} одиниць дитячого взуття зі знижками.\r\n "
#     #                                    f"Щоб переглянути, натисни SKIDKI, SKIDKI_MEN, SKIDKI_CHILDREN", reply_markup=get_reply_keyboard())
#
#
# # async def send_message_json(bot: Bot):
# #     with open('datas\data_card.json', 'r', encoding=' utf-8') as file:
# #         data_card = json.load(file)
# #         # items_list = []
# #         for card in data_card:
# #             # item = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n'Акційна_ціна':  {card['Акційна_ціна']},\n'Знижка':  {card['Знижка']}"
# #             item = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>"
# #             # items_list.append(item)
# #             # for i in items_list:
# #             #     cards_item = i
# #             # return card
# #         await bot.send_message(1498055556, item)
#     # await bot.send_message(1498055556, items_list)
#
# # ***********************************************************
# # @dp.message_handler(Text(equals='skidki'))
# # async def Inter_skidki(message: types.Message):
# #     await message.answer('please waiting...')
# #
# #     with open('datas/data_card.json', 'r', encoding='utf-8') as file:
# #         data_card = json.load(file)
# #         # items_list = []
# #         for card in data_card:
# #             item = f"{card['link']},\n'Стара_ціна':  {card['Стара_ціна']},\n<b>'Акційна_ціна':  {card['Акційна_ціна']},\n</b><b>'Знижка':  {card['Знижка']}</b>,\n{curr_time}"
# #             # items_list.append(item)
# #             # for i in items_list:
# #             #     cards_item = i
# #
# #             await message.answer(item)