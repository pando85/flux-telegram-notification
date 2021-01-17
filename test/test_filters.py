from forwarder.errors import FilteredEvent
from forwarder.filters import filter_event


def test_filter_event(event):
    filter_expression = "'commit_status' in event.metadata and \
        event.metadata['commit_status'] == 'update'"
    event_no_metadata = event._replace(metadata={})
    response_event = filter_event(filter_expression, event_no_metadata)
    assert response_event == event_no_metadata

    event_to_be_filtered = event._replace(metadata={"commit_status": "update"})
    response_filtered_event = filter_event(filter_expression, event_to_be_filtered)
    assert isinstance(response_filtered_event, FilteredEvent)
