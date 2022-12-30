from src.creational_design_patterns_harry.abstract_factory.factory.AbstractFactory import AbstractFactory
from src.creational_design_patterns_harry.abstract_factory.product.ArtChair import ArtChair
from src.creational_design_patterns_harry.abstract_factory.product.ArtSofa import ArtSofa
from src.creational_design_patterns_harry.abstract_factory.product.ArtCoffeeTable import ArtCoffeeTable


class ArtFactory(AbstractFactory):

    def generate_product_a(self):
        return ArtChair()

    def generate_product_b(self):
        return ArtSofa()

    def generate_product_c(self):
        return ArtCoffeeTable()
