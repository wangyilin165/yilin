import pytest
from python.calc import Calc

'''
测试加法：
假设，a,b输入为int类型
测试：a,b为正整数 
     a,b为负整数
     a,b为正小数
     a,b为负小数
     a,b为正虚数
     a,b为负虚数
     a,b为二进制数
     
测试除法：
假设：a,b为float类型
测试：a=0,b为非零数
     a=非零数，b=0
     a,b为正整数 
     a,b为负整数
     a,b为正小数
     a,b为负小数
     a,b为正虚数
     a,b为负虚数
'''
test_add_date = [
    (1, 2, 3),
    (-1, -2, -3),
    (0.1, 0.2, 0.3),
    (-0.1, -0.2, -0.3),
    (complex(1, 1), complex(1, 1), complex(2, 2)),
    (complex(-1, -1), complex(-1, -1), complex(-2, -2)),
    (bin(1), bin(1), bin(2))
]

test_div_date = [
    (0, 2, 0),
    (2, 0, 'Fail'),
    (4, 2, 2.0),
    (-4, 2, -2.0),
    (0.4, 0.2, 2.0),
    (-0.4, -0.2, 2.0),
    (complex(1, 1), complex(1, 1), 1),
    (complex(-1, -1), complex(-1, -1), 1),
]


class TestCalc():
    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,result", test_add_date)
    def test_add(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,result", test_div_date)
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result


if __name__ == '__main__':
    pytest.main()
