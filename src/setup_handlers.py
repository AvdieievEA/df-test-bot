from aiogram import Dispatcher
from handlers import *
from middleware import SomeMiddleware


def register_bot_handlers(dp: Dispatcher):
    Dispatcher.set_current(dp)

    register_messages_handlers(dp)
    register_command_handlers(dp)


def register_middleware(dp: Dispatcher):
    Dispatcher.set_current(dp)

    dp.middleware.setup(SomeMiddleware())
