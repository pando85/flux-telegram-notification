import pytest

from aiohttp import web

from forwarder.errors import ResponseError
from forwarder.telegram import send_alert


async def fake_send(request):
    assert request.match_info['bot_id'][0:3] == 'bot'
    body = await request.json()
    assert isinstance(body['chat_id'], int)
    assert isinstance(body['text'], str)
    return web.Response()


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        if response.status != 404:
            return response
        message = response.message
    except web.HTTPException as ex:
        if ex.status != 404:
            raise
        message = ex.reason
    return web.json_response({'error': message}, status=404)


def get_fake_telegram():
    app = web.Application(middlewares=[error_middleware])
    app.add_routes([web.post('/{bot_id}/sendMessage', fake_send)])
    return app


@pytest.fixture
def fake_telegram_cli(loop, aiohttp_client):
    app = get_fake_telegram()
    return loop.run_until_complete(aiohttp_client(app))


async def test_send_to_telegram(fake_telegram_cli, chat_id, alert_ok):
    alert_response = await send_alert(fake_telegram_cli, chat_id, alert_ok, '')
    assert alert_response == alert_ok


async def test_send_to_telegram_fail(fake_telegram_cli, chat_id, alert_ok):
    alert_response = await send_alert(fake_telegram_cli, chat_id, alert_ok, 'bad_url')
    expected_result = ResponseError(404, {'error': 'Not Found'})
    assert isinstance(alert_response, ResponseError)
    assert alert_response.status_code == expected_result.status_code
    assert alert_response.message == expected_result.message