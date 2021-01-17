import os


API_SPECS_PATH: str = os.environ.get('API_SPECS_PATH', 'docs/api/v1/openapi.yaml')
LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')
TELEGRAM_BOT_TOKEN: str = os.environ.get('TELEGRAM_BOT_TOKEN', '')
TEMPLATE_PATH: str = os.environ.get('TEMPLATE_PATH', 'forwarder/resources/templates/default.j2')
FILTER_EXPRESION: str = os.environ.get(
    'FILTER_EXPRESION',
    '"commit_status" in event.metadata and event.metadata["commit_status"] == "update"'
    )
