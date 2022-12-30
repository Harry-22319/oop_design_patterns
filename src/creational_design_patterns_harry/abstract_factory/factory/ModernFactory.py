from src.creational_design_patterns_harry.abstract_factory.factory.AbstractFactory import AbstractFactory
from src.creational_design_patterns_harry.abstract_factory.product.ModernChair import ModernChair
from src.creational_design_patterns_harry.abstract_factory.product.ModernSofa import ModernSofa
from src.creational_design_patterns_harry.abstract_factory.product.ModernCoffeeTable import ModernCoffeeTable


class ModernFactory(AbstractFactory):

    def generate_product_a(self):
        return ModernChair()

    def generate_product_b(self):
        return ModernSofa()

    def generate_product_c(self):
        return ModernCoffeeTable()
