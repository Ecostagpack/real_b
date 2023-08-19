from aiogram.fsm.state import State, StatesGroup

#
class Steps_Intertop(StatesGroup):
    create_message_for_clients = State()


class Steps(StatesGroup):
    get_message = State()
    q_button = State()
    get_text_button = State()
    get_url_button = State()