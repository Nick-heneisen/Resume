### Problem 1

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
        raise vError

def parse_date(s):
    """
    Checks that s is a valid date mm/dd/yyyy or mm-dd-yyyy
    Raises SyntaxError if form is wrong or mm, dd,
    yyyy are not digit strings with correct number 
    of digits.  
    Raises ValueError if mm, dd, yyyy are not in legal ranges 
    (checked in order mm, dd, yyyy)

    Returns (int(mm),int(dd),int(yyyy))
    """
    try:
        if s[2] == "-" and s[5] == "-":
            listOfDates = s.split("-")
        elif s[2] == "/" and s[5] == "/":
            listOfDates = s.split("/")
        else:
            sError = SyntaxError(f"Incorrect Date Syntax {s}")
            raise sError
        month = int(listOfDates[0])
        day = int(listOfDates[1])
        year = int(listOfDates[2])
        testSyntaxM = listOfDates[0][1]
        testSyntaxD = listOfDates[1][1]
        testSyntaxY = listOfDates[2][3]
    except:
        sError = SyntaxError(f"Incorrect Date Syntax {s}")
        raise sError
    else:
        month = int(listOfDates[0])
        day = int(listOfDates[1])
        year = int(listOfDates[2])
        return (check_number(month, f"Invalid Month {month}", 1, 12),
        check_number(day, f"Invalid Day {day}", 1, 31),
        check_number(year, f"Invalid Year {year}", 1900, 2021))

if __name__ == '__main__':
    # while True:
    #     try:
    #         s = input("Input a date: ")
    #         if s and s[0] == 'q':  # quit
    #             break
    #         print(parse_date(s))
    #     except SyntaxError as e:
    #         print(e)
    #         pass
    #     except ValueError as e:
    #         print(e)
    pass

### Problem 2

from decimal import DivisionByZero
import math

class stack:
    def __init__(self):
        self.s = []

    def pop(self):
        top = self.s[0]
        self.s = self.s[1:]
        return top

    def push(self,item):
        self.s = [item] + self.s

    def empty(self):
        return self.s == []

    def peek(self):
        return self.s[0] if len(self.s) else None
        
    def __str__(self):
        return str(self.s)
        
class calc:
    def __init__(self):
        self.s = stack()
        return self.s.peek()

    def _op1(self,f):
        """Takes the previously inputted number in the
        stack and computes it with the operator given in the
        latest stack.

        Args:
            f (function): The operand that is computing the
            single number

        Returns:
            float: The answer to the previous number and the operand
        """
        # f is a function that takes one operand
        # apply f to top item in stack.  
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        a= self.s.pop()
        self.s.push(f(a))
        return self.s.peek()

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
            raise IndexError("list index out of range")
    
    def clear(self):
        """Completely resets the stack, allowing new 
        computations to be executed.

        Returns:
            function: returns a fuction that resets the stack to 0 and clears the list.
        """
        # clear the stack
        self.s = stack()

    def e(self):
        """Allows computations that include euler's number
        to be executed by inputting the letter "e".
        """
        #euler's number
        self.push(math.e)
        return math.e

    def ln(self):
        """Computes the natural logarithm of the previously
        inputted number.

        Returns:
            float: the answer to the previous number to the natural logarithm.
        """
        # compute math.log(top of stack) (see math module)
        # use _op1
        return self._op1(lambda a: math.log(a) if a > 0 else self.mde())

    def add(self):
        """Adds the previous two numbers inputted in the stack
        together, and returns the answer.

        Returns:
            float: the sum of the preivous two inputted numbers.
        """
        # add top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda a, b:a + b)

        # op2(def:a = pop(), b = pop(), c = a+b, push a+b)

    def div(self):
        """Divides the previous two inputted numbers in the stack,
        with the latter number in the numerator and first number in
        the denominator.

        Returns:
            float: the quotient of the previous two numbers in
            the stack.
        """
        # divide top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda a, b:b / a if b != 0 else self.zero())

    def mult(self):
        """Multiplies the previous two numbers in the stack
        and returns the product of them.

        Returns:
            float: the product of the two orevious numbers.
        """
        # multiply top two elements on stack
        # use _op2
        # return top element or exception
        return self._op2(lambda a, b:a * b)

    def minus(self):
        """Subtracts the previous two numbers in the stack,
        putting the latter number in the front and the
        first number in the back.

        Returns:
            float: the difference of the two previous numbers.
        """
        # subtract top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda a, b:b - a)

    def exp(self):
        """Computes the exponent of the two previous numbers in
        the stack, with the latter number being the base and the
        first number being the exponent.

        Returns:
            float: the answer to the exponential equation.
        """
        # compute x**y with top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda a, b:b ** a)
    
    def push(self,data):
        """Pushes the latest data that is inputted into the stack
        so that it can be computed with what comes next, or the operator that
        tells the program to compute an answer.

        Args:
            data (string): the value that is being processed, or
            the operator that is being computed for
        """
        # push float(data) onto stack
        return self.s.push(float(data))

    def work(self,data):
        try:
            if data == 'c':
                self.clear()
                return "Starting new computation"
            elif data == 'e':
                return str(self.e())
            elif data == 'ln':
                return str(self.ln())
            elif data == '+':
                return str(self.add())
            elif data == '-':
                return str(self.minus())
            elif data == '*':
                return str(self.mult())
            elif data == '/':
                return str(self.div())
            elif data == '^':
                return str(self.exp())
            else:
                str(self.push(data))
        except Exception as e:
            return str(e)
    
    def __str__(self):
        return str(self.s)

    def zero(self):
        """Raises a DivisionByZeroError since you can't
         raise an error in a lambda
        function.

        Raises:
            DivisionByZero: error when you attempt to
            divide by zero
        """
        raise DivisionByZero("division by zero")

    def mde(self):
        """Raises a mathdomain error since you can't
        raise an error in a lambda function.

        Raises:
            ValueError: error when you attempt to
            take the natural logarithm of a number
            <= 0.
        """
        raise ValueError("math domain error")

if __name__ == "__main__":
    i = 0
    w = calc()
    while True:
        # uncomment the following to help debugging
        print(w)
        data = input(f"{i}: ").strip()
        if data == 'q':
            print('Terminated')
            break
        else:
            result = w.work(data)
            if result != None:
                print(result)
        i = 0 if data == 'c' else i+1
    pass