from dataclasses import dataclass
from interfaces import ISnapshot


@dataclass
class Snapshot(ISnapshot):

    _state: object

    def get_state(self):
        return self._state
