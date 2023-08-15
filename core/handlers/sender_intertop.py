from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext

from core.utils import sender_list_intertop
from core.utils.dbconnect import Request
from core.utils.sender_list_intertop import SenderListIntertop
from core.utils.sender_state import Steps
from core.keyboards.inline_sender import get_confirm_button_keyboard


async def sender_decide(bot: Bot, request: Request, senderlistintertop: SenderListIntertop):
    # if not await request.check_table(name_table):
    #     await request.create_table(name_table)
    count = await senderlistintertop.broadcaster_intertop()
    # await call.message.answer(f"повідомлення успішно розіслано [{count}] користувачам")
    # await request.delete_table(name_camp)
