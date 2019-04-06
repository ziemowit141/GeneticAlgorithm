from Function import Function
from DriverCode import crossover
import unittest


class FunctionShould(unittest.TestCase):

    def test_give_proper_value_second_degree(self):
        sut = Function()
        sut.coefficients.clear()
        sut.coefficients.append(3)
        sut.coefficients.append(4)
        self.assertEqual(sut.get_value(2), 10)

    def test_give_proper_value_third_degree(self):
        sut = Function()
        sut.coefficients.clear()
        sut.coefficients.append(3)
        sut.coefficients.append(4)
        sut.coefficients.append(5)
        self.assertEqual(sut.get_value(2), 25)


class DriverCodeShould(unittest.TestCase):

    def test_crossover(self):
        population = []
        population_copy = [Function(), Function()]
        
# test_case = FunctionShould()
# test_case.give_proper_value()
