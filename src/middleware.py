from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update
from aiogram.types.base import TelegramObject


class SomeMiddleware(BaseMiddleware):

    async def on_post_process_update(self, update: Update, data_from_handler: list[dict], data: dict):
        data_from_handler = data_from_handler[0]
        if data_from_handler and data_from_handler[0].get('from_handler', dict()).get('to_sqs', False):
            data_to_aws = {'update_id': update.update_id, 'message': update.message.to_python()}
            # aws_response = lambda_handler(data_to_aws, None)
