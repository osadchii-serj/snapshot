from abc import ABC, abstractmethod


class ISnapshot(ABC):

    @abstractmethod
    def get_state(self):
        raise NotImplementedError()


class IDocument(ABC):

    @abstractmethod
    def set_content(self, content: str):
        raise NotImplementedError()

    @abstractmethod
    def get_content(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self):
        raise NotImplementedError()

    @abstractmethod
    def restore(self, snapshot):
        raise NotImplementedError()
