from pprint import pprint

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, Update


async def hello_message_handler(message: types.Message, state: FSMContext):
    await message.answer(f"I'm a bot, please talk to me!")
    return {'from_handler': {'to_sqs': True}}


def register_messages_handlers(dp: Dispatcher):
    dp.register_message_handler(
        hello_message_handler,
        regexp=r'(?i)\bhello\b',
        content_types=ContentTypes.TEXT,
    )
