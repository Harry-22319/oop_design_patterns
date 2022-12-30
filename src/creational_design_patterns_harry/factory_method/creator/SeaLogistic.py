from .Logistic import Logistic
from ..product.Vehicle import Vehicle
from ..product.Ship import Ship


class SeaLogistic(Logistic):
    def factory_method(self) -> Vehicle:
        return Ship()
