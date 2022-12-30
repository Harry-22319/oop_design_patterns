from src.creational_design_patterns_harry.abstract_factory.factory.AbstractFactory import AbstractFactory
from src.creational_design_patterns_harry.abstract_factory.factory.ModernFactory import ModernFactory
from src.creational_design_patterns_harry.abstract_factory.factory.ArtFactory import ArtFactory


def client_code(factory: AbstractFactory):
    product_a = factory.generate_product_a()
    product_b = factory.generate_product_b()
    product_c = factory.generate_product_c()

    product_a.print_type()
    product_b.print_type()
    product_c.print_type()


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ModernFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ArtFactory())