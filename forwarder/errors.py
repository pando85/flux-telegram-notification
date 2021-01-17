from forwarder.typing import Json


class ResponseError(Exception):
    def __init__(self, status_code: int, message: Json):
        super().__init__(status_code, message)
        self.status_code = status_code
        self.message = message


class FilteredEvent(Exception):
    def __init__(self):
        super().__init__()
        self.status_code = 200
        self.message = {"message": "filtered event, not sended"}
