from abc import ABC, abstractmethod


class NoteAbstract(ABC):
    """An abstract interface for note classes"""
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def is_equal(self, other: 'NoteAbstract') -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def add_interval(self, interval: int) -> 'NoteAbstract':
        pass

    @abstractmethod
    def get_interval(self, other: 'NoteAbstract') -> int:
        pass
