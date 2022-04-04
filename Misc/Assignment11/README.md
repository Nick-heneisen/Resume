# Assignment 11

- Username: nheneise
- Commit hash used for grading: e214bd903016d5f4f29cc35de0aaa82905e6f5fa

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 30         |
| Code Review & style   | 30         |
| Student tests         | 30         |
| Docstrings            | 10         |


## Total Score: 98/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (28/30 pts)
See Pytest output below for a detailed description of the tests
that failed.


## Code Review & style (30/30 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `check_number`: 3/3
    - `parse_date`: 6/6
    - TA Comments: 

- Problem 2:
    - `_op1`: 4/4
    - `_op2`: 4/4
    - `clear`: 3/3
    - `e`: 1/1
    - `ln`: 1/1
    - `add`: 1/1
    - `div`: 1/1
    - `mult`: 1/1
    - `minus`: 1/1
    - `exp`: 1/1
    - `push`: 3/3
    - TA Comments: 

- Forbidden functions used (if any): _


## Student Tests (30/30 pts)
- You had to provide 2 test case for each function/method,
  with the exception of the `calc.e` function.

- Problem 1:
    - `test_check_number`: 3/3
    - `test_date_syntax`: 3/3


- Problem 2:
    - `test_calc_e`: 3/3
    - `test_calc_ln`: 3/3
    - `test_calc_add`: 3/3
    - `test_calc_mult`: 3/3
    - `test_calc_minus`: 3/3
    - `test_calc_div`: 3/3
    - `test_calc_exp`: 3/3
    - `test_calc_push`: 3/3

- TA Comments:


## Docstrings and Comments (10/10 pts)
Student's functions all have properly formatted docstrings in the right place. You lose 1 point for each function that doesn't have proper docstrings or comment.

- Problem 1: Docstrings were given
- Problem 2: 10/10



TA Comments: 

## Pytest Results
```
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.2.5, py-1.9.0, pluggy-0.13.1
rootdir: /home/kbub/Fall-2021/GradingData/Assignment11/nheneise
plugins: assume-2.4.3
collected 68 items

test_a11.py FF..............................................F........... [ 88%]
.....FF.                                                                 [100%]

=================================== FAILURES ===================================
_________________________ test_check_number[-3--1-10] __________________________

i = -3, low = -1, high = 10

    @pytest.mark.parametrize('i,low,high',
    [ (i,-1,10) for i in range(-3,11) ])
    def test_check_number(i,low,high):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
>               a11.check_number(i,'foo',low,high)

test_a11.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

i = -3, msg = 'foo', low = -1, high = 10

    def check_number(i,msg,low,high):
        """
        Checks that integer i is in correct range  low..high (inclusive)
        i (int) the number
        msg (s) error message fragment (one of 'Month', 'Day', or 'Year')
        low (int) low end of range
        high (int) high end of range
    
        returns i or raises ValueError(...)
        """
    
        if i >= low and i <= high:
            return i
        else:
            vError = ValueError(msg)
>           raise vError
E           ValueError: foo

a11.py:18: ValueError

During handling of the above exception, another exception occurred:

i = -3, low = -1, high = 10

    @pytest.mark.parametrize('i,low,high',
    [ (i,-1,10) for i in range(-3,11) ])
    def test_check_number(i,low,high):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
>               a11.check_number(i,'foo',low,high)
E               AssertionError: Regex pattern 'Invalid foo -3' does not match 'foo'.

test_a11.py:14: AssertionError
_________________________ test_check_number[-2--1-10] __________________________

i = -2, low = -1, high = 10

    @pytest.mark.parametrize('i,low,high',
    [ (i,-1,10) for i in range(-3,11) ])
    def test_check_number(i,low,high):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
>               a11.check_number(i,'foo',low,high)

test_a11.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

i = -2, msg = 'foo', low = -1, high = 10

    def check_number(i,msg,low,high):
        """
        Checks that integer i is in correct range  low..high (inclusive)
        i (int) the number
        msg (s) error message fragment (one of 'Month', 'Day', or 'Year')
        low (int) low end of range
        high (int) high end of range
    
        returns i or raises ValueError(...)
        """
    
        if i >= low and i <= high:
            return i
        else:
            vError = ValueError(msg)
>           raise vError
E           ValueError: foo

a11.py:18: ValueError

During handling of the above exception, another exception occurred:

i = -2, low = -1, high = 10

    @pytest.mark.parametrize('i,low,high',
    [ (i,-1,10) for i in range(-3,11) ])
    def test_check_number(i,low,high):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
>               a11.check_number(i,'foo',low,high)
E               AssertionError: Regex pattern 'Invalid foo -2' does not match 'foo'.

test_a11.py:14: AssertionError
_______________________________ test_div_except ________________________________

self = <a11.calc object at 0x7f5beb920790>
f = <function calc.div.<locals>.<lambda> at 0x7f5beb86caf0>

    def _op2(self,f):
        # f is a function that takes two operands
        # apply f to top two items in stack.  top
        # element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        """Takes the previously inputted 2 numbers in the
        stack and computes them with the operator given in the
        latest stack, putting the latest number in the front.
    
        Args:
            f (function): The operand that is computing the
            numbers
    
        Returns:
            float: The answer to the previous numbers and the operand
        """
        try:
            a = self.s.pop()
            b = self.s.pop()
>           self.s.push(f(a, b))

a11.py:141: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

a = 0.0, b = 1.0

>   return self._op2(lambda a, b:b / a if b != 0 else self.zero())
E   ZeroDivisionError: float division by zero

a11.py:202: ZeroDivisionError

During handling of the above exception, another exception occurred:

    def test_div_except():
        c.clear()
        c.push(3)
        c.push(1.0)
        c.push(0.0)
        s = str(c)
        with pytest.raises(ZeroDivisionError,match='division by zero'):
>           c.div()

test_a11.py:105: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:202: in div
    return self._op2(lambda a, b:b / a if b != 0 else self.zero())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <a11.calc object at 0x7f5beb920790>
f = <function calc.div.<locals>.<lambda> at 0x7f5beb86caf0>

    def _op2(self,f):
        # f is a function that takes two operands
        # apply f to top two items in stack.  top
        # element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        """Takes the previously inputted 2 numbers in the
        stack and computes them with the operator given in the
        latest stack, putting the latest number in the front.
    
        Args:
            f (function): The operand that is computing the
            numbers
    
        Returns:
            float: The answer to the previous numbers and the operand
        """
        try:
            a = self.s.pop()
            b = self.s.pop()
            self.s.push(f(a, b))
            return self.s.peek()
        except:
            self.s.push(b)
>           raise IndexError("list index out of range")
E           IndexError: list index out of range

a11.py:145: IndexError
________________________________ test_ln_except ________________________________

    def test_ln_except():
        c.clear()
        c.push(7)
        c.push(0)
        s = str(c)
        with pytest.raises(ValueError, match="math domain error"):
            c.ln()
>       assert s == str(c)
E       AssertionError: assert '[0.0, 7.0]' == '[7.0]'
E         - [7.0]
E         + [0.0, 7.0]

test_a11.py:144: AssertionError
_______________________________ test_add_except ________________________________

self = <a11.calc object at 0x7f5beb920790>
f = <function calc.add.<locals>.<lambda> at 0x7f5beb86cca0>

    def _op2(self,f):
        # f is a function that takes two operands
        # apply f to top two items in stack.  top
        # element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        """Takes the previously inputted 2 numbers in the
        stack and computes them with the operator given in the
        latest stack, putting the latest number in the front.
    
        Args:
            f (function): The operand that is computing the
            numbers
    
        Returns:
            float: The answer to the previous numbers and the operand
        """
        try:
            a = self.s.pop()
>           b = self.s.pop()

a11.py:140: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <a11.stack object at 0x7f5beb850bb0>

    def pop(self):
>       top = self.s[0]
E       IndexError: list index out of range

a11.py:80: IndexError

During handling of the above exception, another exception occurred:

    def test_add_except():
        c.clear()
        c.push(7)
        s = str(c)
        with pytest.raises(IndexError,match="list index out of range"):
>           c.add()

test_a11.py:151: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:186: in add
    return self._op2(lambda a, b:a + b)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <a11.calc object at 0x7f5beb920790>
f = <function calc.add.<locals>.<lambda> at 0x7f5beb86cca0>

    def _op2(self,f):
        # f is a function that takes two operands
        # apply f to top two items in stack.  top
        # element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        """Takes the previously inputted 2 numbers in the
        stack and computes them with the operator given in the
        latest stack, putting the latest number in the front.
    
        Args:
            f (function): The operand that is computing the
            numbers
    
        Returns:
            float: The answer to the previous numbers and the operand
        """
        try:
            a = self.s.pop()
            b = self.s.pop()
            self.s.push(f(a, b))
            return self.s.peek()
        except:
>           self.s.push(b)
E           UnboundLocalError: local variable 'b' referenced before assignment

a11.py:144: UnboundLocalError
=========================== short test summary info ============================
FAILED test_a11.py::test_check_number[-3--1-10] - AssertionError: Regex patte...
FAILED test_a11.py::test_check_number[-2--1-10] - AssertionError: Regex patte...
FAILED test_a11.py::test_div_except - IndexError: list index out of range
FAILED test_a11.py::test_ln_except - AssertionError: assert '[0.0, 7.0]' == '...
FAILED test_a11.py::test_add_except - UnboundLocalError: local variable 'b' r...
========================= 5 failed, 63 passed in 0.18s =========================

```