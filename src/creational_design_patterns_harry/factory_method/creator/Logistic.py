from __future__ import annotations
from abc import ABC, abstractmethod
from ..product.Vehicle import Vehicle


class Logistic(ABC):

    @abstractmethod
    def factory_method(self) -> Vehicle:
        pass
