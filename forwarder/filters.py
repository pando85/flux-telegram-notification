from aiofunctools import bind

from forwarder.typing import Event
from forwarder.errors import FilteredEvent


@bind
def filter_event(filter_str: str, event: Event):
    def custom_filter(event):
        return eval(filter_str)

    if custom_filter(event):
        return FilteredEvent()
    else:
        return event
