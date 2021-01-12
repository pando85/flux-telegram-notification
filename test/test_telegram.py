from forwarder.errors import ResponseError
from forwarder.telegram import send_event


async def test_send_to_telegram(fake_telegram_cli, chat_id, event):
    event_response = await send_event(fake_telegram_cli, chat_id, event)
    assert event_response == event


async def test_send_to_telegram_fail(fake_telegram_cli_fail, chat_id, event):
    event_response = await send_event(fake_telegram_cli_fail, chat_id, event)
    expected_result = ResponseError(404, {'error': 'Not Found'})
    assert isinstance(event_response, ResponseError)
    assert event_response.status_code == expected_result.status_code
    assert event_response.message == expected_result.message
