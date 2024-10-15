from interfaces import IDocument
from interfaces import ISnapshot

from dataclasses import dataclass


@dataclass
class Document(IDocument):

    _content: str = ""

    def set_content(self, content: str):
        self._content = content

    def get_content(self):
        return self._content

    def save(self):
        return ISnapshot(self._content)

    def restore(self, snapshot: ISnapshot):
        self._content = snapshot.get_state()
