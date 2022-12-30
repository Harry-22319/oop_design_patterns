from src.creational_design_patterns_harry.factory_method.creator.Logistic import Logistic
from src.creational_design_patterns_harry.factory_method.creator.AirLogistic import AirLogistic
from src.creational_design_patterns_harry.factory_method.creator.LandLogistic import LandLogistic
from src.creational_design_patterns_harry.factory_method.creator.SeaLogistic import SeaLogistic


def client_code(logistic: Logistic) -> None:
    print(f"Client: I'm not aware of the type of logistic, but it still works.\n"
          f"{logistic.factory_method()}", end="")


if __name__ == "__main__":
    print("App: Launched with the air logistic.")
    client_code(AirLogistic())
    print("\n")

    print("App: Launched with the land logistic.")
    client_code(LandLogistic())

    print("App: Launched with sea logistic.")
    client_code(SeaLogistic())
