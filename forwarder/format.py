from jinja2 import Template

from forwarder.config import TEMPLATE_PATH
from forwarder.typing import Event


# Load template at boot
with open(TEMPLATE_PATH, 'r') as f:
    template = Template(f.read())


def get_message(event: Event) -> str:

    return template.render(event=event)
