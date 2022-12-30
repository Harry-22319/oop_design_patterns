from .Logistic import Logistic
from ..product.Vehicle import Vehicle
from ..product.Truck import Truck


class LandLogistic(Logistic):
    def factory_method(self) -> Vehicle:
        return Truck()
