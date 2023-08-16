from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='початок роботи'
        ),
        BotCommand(
            command='znyzky',
            description='переглянути актуальні знижки'

        ),
        BotCommand(
            command='inline',
            description='Показувати інлайн клавіатуру'
        )

    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())