from typing import Dict, NamedTuple, TypeVar, Union


X = TypeVar('X')
Maybe = Union[X, Exception]

Metadata = Dict[str, str]
Json = Union[dict, list, str]


class InvolvedObject(NamedTuple):
    kind: str = ''
    namespace: str = ''
    name: str = ''
    uid: str = ''
    apiVersion: str = ''
    resourceVersion: str = ''
    fieldPath: str = ''


class Event(NamedTuple):
    involvedObject: InvolvedObject
    severity: str
    timestamp: str
    message: str
    reason: str
    reportingController: str
    reportingInstance: str = ''
    metadata: Metadata = {}

    @classmethod
    def from_dict(cls, _dict: Dict):
        involvedObject = InvolvedObject(**_dict['involvedObject'])
        _dict.pop('involvedObject')
        return cls(
            involvedObject=involvedObject,
            **_dict
        )

    def as_dict(self):
        _dict = self._asdict()
        _dict['involvedObject'] = self.involvedObject._asdict()
        return _dict
