from .Logistic import Logistic
from ..product.Vehicle import Vehicle
from ..product.Plane import Plane


class AirLogistic(Logistic):
    def factory_method(self) -> Vehicle:
        return Plane()
