from dataclasses import dataclass


@dataclass
class Snapshot:

    _state: object

    def get_state(self):
        return self._state
