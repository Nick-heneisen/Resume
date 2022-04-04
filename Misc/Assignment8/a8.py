#############################################
# Problem 1
#############################################

def F(n, m, p):
    """
    Uses recursion to calculate an integer.

    Args: (integer, integer, integer)


    Returns: (integer)

    """
    #loops until p is 0
    if p == 0:
        return 100 + n - m
    else:
        return n * m - p + F(n - 3, m - 2, p - 1)

def Ft(n, m, p, v = 100):
    """
    Uses tail recursion to calculate an integer.

    Args: (integer, integer, integer)

    Returns: (integer)

    """
    #loops until p is 0
    if p == 0:
        return v + n - m
    else:
        return Ft(n - 3, m - 2, p - 1, (n * m) - p + v)

def B(n):
    """
    Uses recursion to calculate an integer.

    Args: (integer)

    Returns: (integer)

    """
    #loops until n is 0
    if n == 0:
        return 5
    elif n == 1:
        return 10
    else: 
        return 5 * n + B(n - 1)

def Bt(n, v=0):
    """
    Uses tail recursion to calculate an integer.

    Args: (integer)

    Returns: (integer)

    """

    #loops until n is 0
    if n == 0:
        return 5 + v
    elif n == 1:
        return 10 + v
    else:
        return Bt(n - 1, 5 * n + v)


def x(n):
    """
    Uses recursion to calculate an integer.

    Args: (integer)

    Returns: (integer)

    """
    #if n is odd, the bottom else runs, otherwise the top elif does.
    if n == 0:
        return 3
    elif n % 2 == 0:
        return 2 * n + 1 + x(n - 1)
    else:
        return 2 * n + x(n - 1)

def xt(n, v=3):
    """
    Uses tail recursion to calculate an integer.

    Args: (integer)

    Returns: (integer)

    """
    #if n is odd, the bottom else runs, otherwise the top elif does.
    if n == 0:
        return v
    elif n % 2 == 0:
        return xt(n - 1, 2 * n + 1 + v)
    else:
        return xt(n - 1, 2 * n + v)

#############################################
# Problem 2
#############################################
d, c = "d","c"
def balance(xbook):
    """
    Returns true or false depeding on whether or not the checkbook is balanced.

    Args: (list)

    Returns: (boolean)

    """
    #initializes variables
    credit = 0
    debit = 0

    #Checks for credit or debit
    for i in xbook:
        if i[0] == "c": 
            credit += i[1]
        else:
            debit += i[1]
    #Finds the difference and returns true or false depending on it
    if credit - debit == 0:
        return True
    else: 
        return False

def balance_rec(xbook):
    """
    Returns true or false depeding on whether or not the checkbook is balanced.

    Args: (list)

    Returns: (boolean)

    """

    def bh(blst):
        #base condition
        if blst == []:
            return 0

        #checks for credit or debit, loops recursively
        if blst[0][0] == "c":
            return bh(blst[1:]) + (blst[0][1])
        else:
            return bh(blst[1:]) - (blst[0][1])
    return not bh(xbook)


#############################################
# Problem 3
#############################################
def gsf_close(a, r, n):
    
    """
    Calculates a sum for function g.

    Args: (int, int, int)

    Returns: (int)

    """

    if r == 1:
        return 0
    else:
        answer = a * ((1 - r ** n) / (1 - r))
        return answer


def gsf(a, r, n):
    """
    Calculates a sum for function g.

    Args: (int, int, int)

    Returns: (int)

    """
    final = 0
    for i in range(0, n):
        final += a * (r ** i)

    return final

def g(a, r, n):
    """
    Calculates a sum for function g.

    Args: (int, int, int)

    Returns: (int)

    """
    def gh(k):
        if k == 0:
            return a
        else:
            return gh(k - 1)+(a * r ** k)

    return gh(n - 1)

#############################################
# Problem 4
#############################################
def occurs(x,xlst):
    """Problem 4.  For loop implementation of occurs

    Args:
        x (number): value
        xlst (list): list of values

    Returns:
        found: boolean (True or False)

    """

    found = False
    for i in xlst:
        if x == i:
            found = True
            break
    return found

def occurs_w(x,xlst):
    """
    Checks if a value (x) is present in a list.

    Args: (int, list)

    Returns: (boolean)

    """

    found = False
    while xlst:
        if x == xlst[0]:
            found = True
            break
        else:
            xlst = xlst[1:]
    return found


def occurs_r(x,xlst):
    """
    Checks if a value (x) is present in a list.

    Args: (int, list)

    Returns: (boolean)

    """
    found = False
    if xlst == []:
        found = False
        return found
    elif xlst[0] == x:
        found = True
        return found
    else:
        xlst = xlst[1:]
        return occurs_r(x, xlst)

#############################################
# Problem 5
#############################################
def gcd(x,y):
    """
    Returns the greatest common divisor of the inputs.

    Args: (int, int)


    Returns: (int)

    """
    if y == 0:
        return x
    else: 
        return gcd(y, x % y)

if __name__ == "__main__": 
    # Problem 1
    print("The next 3 lines are calls for F and Ft")
    print(F(5,5,5),Ft(5,5,5))
    print(F(1,2,3),Ft(1,2,3))
    print(F(5,4,2),Ft(5,4,2))
    
    print("The next 5 lines are calls for B and Bt")
    for i in range(5):
       print(B(i), Bt(i))
       
    print("The next 5 lines are calls for x and xt")
    for i in range(5):
           print(x(i),xt(i))

    # Problem 2  
    d,c = "d","c"
    xbook1 = [[d, 895],[c,7500],[d,339],[c,234],[d,6400],[d,100]]
    xbook2 = [[d, 95],[c,500],[d,39],[c,234],[d,600],[d,10]]
    print(balance_rec(xbook1),balance(xbook1))
    print(balance_rec(xbook2), balance(xbook2))

    # Problem 3
    print(gsf(2,3,5))
    print(g(2,3,5))
    print(gsf_close(2,3,5))

    #Problem 4
    print(occurs(1,[2,3,4]),occurs_w(1,[2,3,4]),occurs_r(1,[2,3,4]))
    print(occurs([1],[1,3,4]),occurs_w([1],[1,3,4]),occurs_r([1],[1,3,4]))
    print(occurs([1],[1,[1],2]),occurs_w([1],[1,[1],2]),occurs_r([1],[1,[1],2]))

    # Problem 5
    print(gcd(10,6))
    print(gcd(12,9))
    print(gcd(55,40))

