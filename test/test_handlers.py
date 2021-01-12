import pytest

from toolz import curry

from forwarder.app import get_app


BASE_URL = '/v1'


@pytest.fixture
def cli(loop, aiohttp_client, fake_telegram_cli):
    @curry
    async def setup_telegram_client(app, _useless_reference):
        app['telegram_client'] = fake_telegram_cli
        return app
    app = get_app(setup_telegram_client)

    return loop.run_until_complete(aiohttp_client(app.app))


async def test_forward_event(cli, chat_id, event_dict):
    resp = await cli.post(f'{BASE_URL}/event/{chat_id}', json=event_dict)
    assert resp.status == 200
    assert await resp.json() == event_dict


async def test_ping(cli):
    resp = await cli.get(f'{BASE_URL}/ping')
    assert resp.status == 200
    assert await resp.json() == 'pong'
