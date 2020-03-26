import pytest

from python.calc import Calc


class TestCalc():
    def test_add1(self):
        calc = Calc()
        assert calc.add(1, 2) == 3


if __name__ == "__main__":
    pytest.main()

# import unittest
# import sys
#
# sys.path.append("..")
# from python.calc import Calc
#
#
# class TestCalc(unittest.TestCase):
#     def setUp(self) -> None:
#         self.calc = Calc()
#
#     def test_add_1(self):
#         self.assertEqual(3, self.calc.add(1, 2))
#
#     def test_add_2(self):
#         self.assertEqual(300, self.calc.add(100, 200))
#
# if __name__=="__main__":
#     unittest.main()
