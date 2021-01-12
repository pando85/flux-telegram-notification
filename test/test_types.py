from forwarder.typing import InvolvedObject, Event


def test_event(event):
    assert isinstance(event, Event)
    assert isinstance(event.involvedObject, InvolvedObject)
