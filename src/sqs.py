import asyncio
import json
import os

import dotenv
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
import logging

from setup_handlers import register_bot_handlers

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dotenv.load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


def lambda_handler(event, context):
    logger.info("lambda_handler event: {}".format(json.dumps(event)))
    return asyncio.get_event_loop().run_until_complete(main(event, context))

async def process_event(event, dp: Dispatcher):
    """
    Converting an AWS Lambda event to an update and handling that
    update.
    """

    Bot.set_current(dp.bot)
    event = json.loads(event)
    update = types.Update.to_object(event)
    await dp.process_update(update)


async def main(event, context):
    bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_bot_handlers(dp)

    for record in event['Records']:
        await process_event(record["body"], dp)

    return 'ok'
   