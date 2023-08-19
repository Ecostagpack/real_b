from aiogram.utils.keyboard import InlineKeyboardBuilder

#
def get_confirm_button_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Добавити кнопку', callback_data='add_button')
    keyboard_builder.button(text='не добавляти кнопку', callback_data='no_button')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def dobavlyaty_button_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Добавити кнопку', callback_data='add_button')
    keyboard_builder.button(text='не добавляти кнопку', callback_data='no_button')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
