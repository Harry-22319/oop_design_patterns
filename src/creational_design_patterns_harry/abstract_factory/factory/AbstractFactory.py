from __future__ import annotations
from abc import ABC, abstractmethod
from src.creational_design_patterns_harry.abstract_factory.product.ModernChair import ModernChair
from src.creational_design_patterns_harry.abstract_factory.product.ModernSofa import ModernSofa
from src.creational_design_patterns_harry.abstract_factory.product.ModernCoffeeTable import ModernCoffeeTable


class AbstractFactory:
    @abstractmethod
    def generate_product_a(self) -> ModernChair:
        pass

    @abstractmethod
    def generate_product_b(self) -> ModernSofa:
        pass

    @abstractmethod
    def generate_product_c(self) -> ModernCoffeeTable:
        pass
