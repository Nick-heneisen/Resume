import a9
import pytest
import math
from pytest import approx

def test_pop():
    # replace with your tests
    assert False

def test_error():
    # replace with your tests
    assert False

def test_get_data():
    # replace with your tests
    assert False

def test_get_dic():
    # replace with your tests
    assert False

def test_get_state_pop():
    # replace with your tests
    assert False

def test_covid():
    # no additional tests required
    dic = a9.get_dic("us-counties.csv")
    state_pop = a9.get_state_pop("sp.csv")
    assert a9.ccc(dic,(0,2))[(0,2)] == 896
    assert a9.scd("Alabama", dic) == 8166
    assert a9.usdd(dic,state_pop)["Texas"] == 0.103

@pytest.mark.parametrize("test_input,expected", 
    [   
        ((lambda x: 1           ,0,10,100), 10),
        ((lambda x: x           ,0,10,100), 50),
        ((lambda x: 3*x*x + 1   ,0,6,100),6**3+6),
    ])
def test_simpson(test_input,expected):
    # no additional tests required
    assert a9.simpson(*test_input) == approx(expected)
