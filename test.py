import pytest
from app.calculator import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator

   #Умножение
   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 3, 4) == 12

    #Вычитание
   def test_subtraction_calculate_correctly(self):
       assert self.calc.subtraction(self, 3, 3) == 0

    #Сложение
   def test_adding_calculate_correctly(self):
       assert self.calc.adding(self, 3, 4) == 7

    #Деление
   def test_division_calculate_correctly(self):
       assert self.calc.division(self, 15, 3) == 5