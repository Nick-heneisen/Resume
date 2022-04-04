import pytest
import a11
import math

### problem 1
# Note, we've included tests for exceptions
# You need to provide tests for non-exception cases
def test_check_number():
    low = 0
    high = 10
    for i in range(0,10):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
                assert i == a11.check_number(i,'foo',low,high)

def test_date_syntax(input_str):
    with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
        a11.parse_date(input_str)

def test_check_number_exception():
    low = 0
    high = 10
    for i in range(-3,11):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
                assert i == a11.check_number(i,f'Invalid foo {i}',low,high)

@pytest.mark.parametrize('input_str',[
('12/03'),
('12/03/abcd'),
('12/3/2000'),
('12/3/45'),
('1/23/2003'),
('11-22/2003')
])
def test_date_syntax2(input_str):
    with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
        a11.parse_date(input_str)

@pytest.mark.parametrize('input_str,val, msg',[
    ('00/02/2002','0','Month'),
    ('33/02/2002','33','Month'),
    ('01/00/2002','0','Day'),
    ('01/33/2002','33','Day'),
    ('01-01-1800','1800','Year'),
    ('01-01-2022','2022','Year')
])

def test_date_syntax3(input_str,val,msg):
    with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
        a11.parse_date(input_str)


######### Problem 2
# we've included tests for exceptions at the end

c = a11.calc()

def test_work():
    for e in ["c","3","4","+"]:
        result = c.work(e)
    assert result == '7.0'

def test_calc_e():
    eanswer = c.e()
    assert eanswer == 2.718281828459045

def test_calc_ln():
    c.push("4")
    lnanswer=c.ln()
    assert lnanswer == 1.3862943611198906

def test_calc_add():
    c.push("4")
    c.push("7")
    sum=c.add()
    assert sum == 11.0

def test_calc_mult():
    c.push("4")
    c.push("7")
    multiplyanswer=c.mult()
    assert multiplyanswer == 28

def test_calc_minus():
    c.push("4")
    c.push("7")
    diff=c.minus()
    assert diff == -3.0

def test_calc_div():
    c.push("4")
    c.push("7")
    div=c.div()
    assert div == 0.5714285714285714

def test_calc_exp():
    c.push("4")
    c.push("7")
    expx=c.exp()
    assert expx == 16384.0

data = list(zip(range(-10,10),range(-10,10)))

def test_div_except():
    c.clear()
    c.push(3)
    c.push(1.0)
    c.push(0.0)
    s = str(c)
    with pytest.raises(ZeroDivisionError,match='division by zero'):
        c.div()
    assert s == str(c)
  
def test_push_except():
    c.clear()
    c.push(3)
    c.push(4)
    s = str(c)
    v = 'ab'
    with pytest.raises(ValueError, match =f"could not convert string to float: '{v}'"):
        c.push(v)
    assert s == str(c)

def test_ln_except():
    c.clear()
    c.push(7)
    c.push(0)
    s = str(c)
    with pytest.raises(ValueError, match="math domain error"):
        c.ln()
    assert s == str(c)

def test_add_except():
    c.clear()
    c.push(7)
    s = str(c)
    with pytest.raises(IndexError,match="list index out of range"):
        c.add()
    assert str(c) == s