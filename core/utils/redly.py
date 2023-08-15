
# async def alternatyva(message, table_name, chat_id):
#     users = ''
#     data = await state.get_data()
#     text = data.get('text')
#     for user in users:
#         await self.bot.send_message(chat_id, message)
#
#
# async def sendall(message: types.Message):
#     text = 'hellow'
#     users = 'подставлю'
#     for row in users:
#         await bot.send_message(row[0], text)

# @dp.message_handler(commands=['sendall'])
# async def sendall(message: types.Message):
#     if message.chat.type == 'private':
#         if message.from_user.id == 1498055556:
#             text = message.text[9:]
#             users = db.get_users()
#             for row in users:
#                 try:
#                     await bot.send_message(row[0], text)
#                     if int(row[1]) != 1:
#                         db.set_active(row[0], 1)
#                 except:
#                     db.set_active(row[0], 0)
#             await bot.send_message(message.from_user.id,'успішна розсилка')