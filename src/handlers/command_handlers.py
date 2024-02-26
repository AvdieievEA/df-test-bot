from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes


async def hello_command_handler(message: types.Message, state: FSMContext):
    await message.answer("I'm a bot, please talk to me!")


def register_command_handlers(dp: Dispatcher):
    dp.register_message_handler(
        hello_command_handler,
        commands=["hello"],
        content_types=ContentTypes.TEXT,
    )
