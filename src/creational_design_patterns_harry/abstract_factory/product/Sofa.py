from __future__ import annotations
from abc import ABC, abstractmethod


class Sofa(ABC):

    @abstractmethod
    def print_type(self):
        pass
