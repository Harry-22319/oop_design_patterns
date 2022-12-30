from __future__ import annotations
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def print_type(self):
        pass
