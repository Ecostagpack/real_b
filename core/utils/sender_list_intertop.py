# import asyncio
# from datetime import datetime
# from sched import scheduler
#
# from aiogram import Bot
# from aiogram.types import Message
# import asyncpg
# from aiogram.exceptions import TelegramRetryAfter
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from asyncpg import Record
# from typing import List
# from aiogram.types import InlineKeyboardMarkup
#
#
# class SenderListIntertop:
#     def __init__(self, bot: Bot, connector: asyncpg.pool.Pool):
#         self.bot = bot
#         self.connector = connector
#
#
#     async def get_users(self, name_table):
#         async with self.connector.acquire() as connect:
#             name_table = 'datausers'
#             query = f"SELECT user_id FROM {name_table}"
#             results_query: List[Record] = await connect.fetch(query)
#             return [result.get('user_id') for result in results_query]
#
#
#     async def send_message(self, user_id: int):
#         return await self.send_message(user_id)
#
#
#     async def broadcaster_intertop(self, name_table: str):
#         users_ids = await self.get_users(name_table)
#
#         count = 0
#         try:
#             for user_id in users_ids:
#                 if await self.send_message(int(user_id)):
#                     count += 1
#                 await asyncio.sleep(.05)
#         finally:
#             print(f"Повідомлення розіслано {count} користувачам")
#             return count

import asyncio
from datetime import datetime
from sched import scheduler

from aiogram import Bot
from aiogram.types import Message
import asyncpg
from aiogram.exceptions import TelegramRetryAfter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asyncpg import Record
from typing import List
from aiogram.types import InlineKeyboardMarkup


class SenderListIntertop:
    def __init__(self, bot: Bot, connector: asyncpg.pool.Pool):
        self.bot = bot
        self.connector = connector


    async def get_users(self):
        async with self.connector.acquire() as connect:
            # query = f"SELECT user_id FROM datausers WHERE status = 'waiting'"
            query = f"SELECT user_id FROM users_for_sender WHERE status = 'waiting' "

            results_query: List[Record] = await connect.fetch(query)
            return [result.get('user_id') for result in results_query]


    async def send_message(self, user_id: int):
        return await self.send_message(user_id)


    async def broadcaster_intertop(self):
        users_ids = await self.get_users()

        count = 0
        try:
            for user_id in users_ids:
                if await self.send_message(int(user_id)):
                    count += 1
                await asyncio.sleep(.05)
        finally:
            print(f"Повідомлення розіслано {count} користувачам")
            return count

