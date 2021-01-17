from aiofunctools import bind, compose
from aiohttp.web import Response

from forwarder import logger
from forwarder.config import FILTER_EXPRESION
from forwarder.filters import filter_event
from forwarder.response import return_200
from forwarder.telegram import send_event
from forwarder.typing import Event


async def forward_event(chat_id, **extra_args) -> Response:
    return await compose(
        Event.from_dict,
        logger.debug,
        filter_event(FILTER_EXPRESION),
        logger.debug,
        send_event(extra_args['request'].app['telegram_client'], chat_id),
        logger.debug,
        bind(lambda x: x.as_dict()),
        return_200)(await extra_args['request'].json())


async def ping() -> Response:
    return compose(
        logger.debug,
        return_200)('pong')
