from __future__ import annotations
from abc import ABC, abstractmethod


class CoffeeTable(ABC):

    @abstractmethod
    def print_type(self):
        pass
