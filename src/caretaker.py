from interfaces import IDocument

from dataclasses import dataclass


@dataclass
class Caretaker:

    _snapshots = []

    def save_state(self, document: IDocument):
        self._snapshots.append(document.save())
        print(self._snapshots)

    def restore_state(self, document: IDocument):
        last_snapshot = self._snapshots.pop()
        document.restore(last_snapshot)
        print(self._snapshots)
