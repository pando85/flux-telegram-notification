
from forwarder.format import get_message


def test_get_message(event):
    formated_event = get_message(event)
    expected_output = ("""✅ *flux-system.flux-system*
Fetched revision: main/731f7eaddfb6af01cb2173e18f0f75b0ba780ef1

*status*
apply change set

*revision*
master/e548962d278de9ba9046b15c1f53f06cf77db84c

""")
    assert isinstance(formated_event, str)
    assert formated_event == expected_output
