from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='початок роботи'
        ),
#         BotCommand(
#             command='help',
#             description='допомога'
#         ),
#         BotCommand(
#             command='cansel',
#             description='відмінити'
#         ),
        BotCommand(
            command='inline',
            description='Показувати інлайн клавіатуру'
        )
#         BotCommand(
#             command='form',
#             description='почати опитування'
#         ),
#         BotCommand(
#             command='audio',
#             description='надіслати аудіо'
#         ),
#         BotCommand(
#             command='document',
#             description='надіслати документ'
#         ),
#         BotCommand(
#             command='mediagroup',
#             description='надіслати медіагрупу'
#         ),
#         BotCommand(
#             command='photo',
#             description='надіслати фото'
#         ),
#         BotCommand(
#             command='sticker',
#             description='надіслати стікер'
#         ),
#         BotCommand(
#             command='video',
#             description='надіслати відео'
#         ),
#         BotCommand(
#             command='video_note',
#             description='надіслати відео повідомлення'
#         ),
#         BotCommand(
#             command='voice',
#             description='надіслати голосове повідомлення'
#         )
#
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())