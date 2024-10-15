from abc import ABC, abstractmethod


class ISnapshot(ABC):

    @abstractmethod
    def get_state(self):
        raise NotImplementedError()
