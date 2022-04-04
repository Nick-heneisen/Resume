"""
CS200 Assignment 4 
   Practice with iterables
"""

import math

if __name__ == "__main__":
    print()
    print("Currently running `a4.py`")
    print("The output presented here is just extra print information; the output you see in the terminal is for reference—not for final grading")
    print("To determine if functions work properly, refer to the testing file")

#####################################################################################################
#PROBLEM ONE
#####################################################################################################

#INPUT non-negative integer n
#RETURN string of * that, when printed,
# is a block
# if n = 0, then return ""
def block(n):
    """
    Prints a block of asterisks with 
    n columns and rows

    Args:
        1 integer

    Returns:
        Block of asterisks
    """
    if n > 0:
        return((("*" * n) + "\n") * n)
    else:
        return ""
pass

#INPUT non-negative integer n
#RETURN string of * that, when printed,
# is an outline 
# if n = 0, then return ""
def square(n):
    """
    Prints a square of asterisks with 
    n columns and rows

    Args:
        1 integer

    Returns
        Square of asterisks
    """
    if n > 0:
        if n == 1:
            return("*\n")
        elif n == 2:
            return("**\n**\n")
        else: 
            return(("*" * n + "\n") + (("*" + " " * (n - 2) + "*" + "\n") * (n - 2)) + ("*" * n) + "\n")
    else:
        return "" 


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 1")
    for i in range(5):
        print("Block of size {0}".format(i))
        print(block(i))
    

    for i in range(5):
        print("Square of size {0}".format(i))
        print(square(i))
   

#####################################################################################################
#PROBLEM 2
#####################################################################################################

#DATA
## DO NOT CHANGE THESE VARIABLES MANUALLY
act, Au,Ag,Pd,Pt ="act", "gold", "silver", "paladium", "platinum"
spot_price = {Au:1833.15, Ag:27.61, Pt:1275.20, Pd: 2426.60}
portfolio = {act: 10000}
portfolio["holdings"] = {Au:(0,0), Ag:(0,0), Pt:(0,0), Pd: (0,0)}

#INPUT portfolio, metal, and number of ounces of metal
#RETURN True or False
#True: transaction has been made
#False: transaction has not been made  
def purchase(portfolio, metal, amt):
    """
    Returns true if there is enough money 
    in the account to make a transaction for 
    the inputted metal & quantity

    inputs:
        (portfolio, metal, integer)

    returns: 
        boolean
    """
    if spot_price[metal] * amt <= portfolio[act]:
        portfolio[act] -= spot_price[metal] * amt
        portfolio["holdings"][metal] = (portfolio["holdings"][metal][0] + amt, portfolio["holdings"][metal][1] + spot_price[metal] * amt)
        return True
    else:
        return False

#INPUT portfolio and metal
#RETURN non-negative integer of number of ounces
#that can be purchased
def how_much(portfolio, metal):
    """
    returns the most amount of a metal 
    that you can putchase with your current funds

    inputs:
        (portfolio, metal)

    returns:
        (integer)
    """
    mostAmount = portfolio[act] // spot_price[metal] 
    return mostAmount
    

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 2")
    print(purchase(portfolio,Au, 1))
    print(portfolio)
    print(purchase(portfolio,Au, 1000))
    print(portfolio)

    purchase(portfolio,Au, 2)
    purchase(portfolio,Ag,3)
    purchase(portfolio,Pt,2)
    print(portfolio)
    print(how_much(portfolio, Pd))

#####################################################################################################
#PROBLEM 3
#####################################################################################################

#INPUT a possibly empty list of numbers
#RETURN the smallest number and the number of times
#it occurs in the list
def find_num_min(xlst):
    """
    returns the smallest number and 
    how many times it occurs

    inputs:
        (none)

    returns:
        (tuple)
    """
    count = 0
    min = 10
    if len(xlst) == 0:
            return ()
    for i in xlst:
        if i < min:
            min = i
        elif i == min:
            count += 1
        
    return (min, (count + 1)) 
    

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 3")
    x1 = []
    x2 = [1,0,0,1]
    x3 = [1,2,3,4,0]
    x4 = [5]
    x5 = [-1,0,2,2,0,-1]

    x = [x1,x2,x3,x4,x5]
    for i in x:
        print(find_num_min(i))

#####################################################################################################
#PROBLEM 4
#####################################################################################################
#Solving cryptarithms

#INPUT None
#RETURN list of all possible solutions    
def search_me_me_bee():
    """
    Finds integers that satisfy the expression
    ME + ME == BEE.

    Args:
        None

    Returns:
        List of numbers that satisfy and the
        cooresponding letter.
    """
    for M in range(0, 10):
        for E in range(0, 10):
            for B in range(0, 10):
                if (10 * M + E) + (10 * M + E) == ((B * 100) + (E * 10) + E):
                    
                    if not M in [B, E] and not B in [M, E] and not E in [M, B]:
                        return [[['M', M], ['B', B], ['E', E]]]
#INPUT None
#RETURN list of all possible solutions
def search_go_to_out():
    """
    Finds integers that satisfy the expression
    TO + GO == OUT.

    Args:
        None

    Returns:
        List of numbers that satisfy and the
        cooresponding letter.
    """
    for T in range(0, 10):
        for O in range(0, 10):
            for G in range(0, 10):
                for U in range(0, 10):
                  if (T * 10 + O) + (G * 10 + O) == (O * 100 + U * 10 + T):
                    
                    if not T in [O, U, G] and not O in [U, T, G] and not U in [T, G, O] and not G in [T, O, U]:
                        return [[['T', T], ['O', O], ['U', U], ['G', G]]]


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 4")
    print(search_me_me_bee())
    print(search_go_to_out()) 

#####################################################################################################
#PROBLEM 5
#####################################################################################################

#INPUT a (possibly empty) list of integers
#RETURN the length of the longest monotonic sequence
def increase(xlst):
    
    """
    returns the largest monotonically 
    increasing sequence of the list

    inputs:
        (list)
    
    returns:
        (integer)
    """
    top = 0
    small = 0
    change = -1
    for i in xlst:
        if len(xlst) == 0:
            return ()
        elif i >= small:
            small = i
            change += 1
            if change > top:
                top = change
        elif i < small:
            small = i
            if change > top:
                top = change
                change = 0
            else:
                change = 0

    return top


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 5")
    x1 = [0,1,2,2,3,1,2,3,1,1,0,1]
    x2 = [1,2,3,4,5,0,1,1,1,1,1,1,1,1]
    x3 = [1,2,3,4,5,1]
    x4 = [5,4,3,2,1]
    xlst = [x1,x2,x3,x4, []]
    for i in xlst:
        print("Longest monotonic sequence in {0}: \n{1}".format(i,increase(i)))

#####################################################################################################
#PROBLEM 6
#####################################################################################################

#INPUT string of containing only letters, spaces, comma, and period
#RETURN a dictionary that gives the count of each letter
def letter_count(text):
    """
    counts how many times each letter occurs in 
    the string

    input:
        (string)

    returns:
        (dictionary)
    """
    letters = {}
    for i in text:
        if i != " " and i != "," and i != ".":
            i = i.lower()
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
                

    return letters  

        

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 6")
    f ="Two roads diverged in a yellow wood,\
        And sorry I could not travel both\
        And be one traveler, long I stood\
        And looked down one as far as I could\
        To where it bent in the undergrowth"
    g = "the quick brown fox jumped over the lazy dog"
    print(letter_count(f))
    print(letter_count(g))

#####################################################################################################
#PROBLEM 7
#####################################################################################################

#INPUT two vectors of same length
#RETURN dot product
def dot_prod(x,y):
    multiplication = []
    for i in range(0, len(x)):
        multiplication.append(x[i] * y[i])
    answer = sum(multiplication)
    return answer 

#INPUT vector and scalar
#RETURN vector 
def scalar_vec(x,n):
    scalar = [element * n for element in x]
    return scalar

#INPUT vector
#RETURN non-negative scalar (float or real)
def euc_len(x):
    
    squared = [x ** 2 for x in x]
    add = sum(squared)
    root = math.sqrt(add)
    return root

#INPUT two vectors
#RETURN the angle in DEGREES between 
def ang_vec(x,y):
    answer = math.acos((dot_prod(x, y) / (euc_len(x) * euc_len(y))))
    return math.degrees(answer)

#INPUT vector
#RETURN uni vector
def unit_vec(x):
    euclenx = euc_len(x)
    answer = scalar_vec(x, 1 / euclenx)
    return answer

#INPUT two vectors and either "+" or "-"
#RETURN sum or difference of vectors
def vec_op(x, y, op):
    addition = []
    subtraction = []
    if op == "+":
        for i in range(0, len(x)):
            addition.append((x[0] + x[1]) and (y[0] + y[1]))
            sum = x[0] + x[1]
            return[sum, addition[0]]
    if op == "-":
        for i in range(0, len(x)):
            subtraction.append((x[0] - x[1]) and (y[0] - y[1]))
            subtractionResult = x[0] - x[1]
            return[subtractionResult, subtraction[0]]


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 7")
    # Vectors
    x = [4,3]
    y = [3,5]

    print(vec_op(x,y,"+"))
    print(vec_op(x,y,"-"))
    print(dot_prod(x,y))
    print(scalar_vec(x,1/5))
    print(euc_len(x))
    print(euc_len(y))
    print(ang_vec(x,y))
    print(unit_vec(x))
    print(euc_len(unit_vec(x)))


#####################################################################################################
#PROBLEM 8
#####################################################################################################

# https://www.michigan.gov/documents/dnr/TreeAge_401065_7.pdf

def tree_age(circumferance, bark, growth_rate):
    inches = circumferance[0] * 12 + circumferance[1]
    diameter = inches / 3.14
    radius = (diameter / 2) - bark
    return math.floor(radius / growth_rate)


def noninvasive_tree_age(circumferance, tree):
    treeRate = {"White Oak":5.0, "Red Oak": 4.0, "Pin Oak":3.0, "Linden":3, "Basswood":3.0}
    inches = circumferance[0] * 12 + circumferance[1]
    diameter = inches / math.pi
    radius = (diameter / 2) + .25
    return math.floor(radius * treeRate[tree])


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 8")
    print("\ttree_age")
    print(tree_age([12,10], .5, .2))
    print(tree_age([1,1],0,.3))
    print("\tnoninvasive_tree_age")
    print(noninvasive_tree_age([12,10], "White Oak"))
    print(noninvasive_tree_age([5, 5], "Red Oak"))


#####################################################################################################
#PROBLEM 9
#####################################################################################################

#INPUT list of int, str, set, tuple, lists...
#RETURN list of unique values in list
#REQUIREMENTS cannot use Python set or set functions
#Can use in predicate
def make_unique(xlst):
    pass



#INPUT list and size
#RETURN returns a list of list of size
#if there is left over that's less than
#size, then make the a list
def partition(xlst, size):
    pass


#INPUT list and object
#RETURN all the locations of object in the list
#REQUIREMENTS Cannot use any list functions
def occurs_at_index(xlst, item):
    pass



#INPUT two lists x,y
#RETURN list of *unique* objects that belong to both lists
#REQUIREMENTS cannot use Python set, set functions
def intersect(xlst, ylst):
    pass


#INPUT list of numbers and int 0,1
#RETURN if int is 0, then find minimum
#if int is 1, then find maximum
#REQUIREMENTS cannot use Python max, min
#ERROR if list is empty, return []
def optimum(xlst,s):
    pass


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 9")
    print("\tmake_unique")
    x1 = [1,0,1,0,"dog", "cat", "cat", (1,),(1,),(2,)]
    x2 = [[],[],"","",(),()]
    print(make_unique(x1))
    x3 = []
    print(make_unique(x2))
    print(make_unique(x3))
    print("\tpartition")
    print(partition([1,2,3,4],0))
    print(partition([1,2,3,4],2))
    print(partition([1,2,3,4],1))
    print(partition([1,2,3,4],3))
    print(partition([1,2,3,4],4))
    print(partition([1,2,3,4],5))
    print("\toccurs_at_index")
    print(occurs_at_index([0,1,0,1,1],1))
    print(occurs_at_index([0,1,0,1,1],2))
    print(occurs_at_index([0,1,0,1,1],0))
    print("\tintersect")
    print(intersect([],[1]))
    print(intersect([2],[]))
    print(intersect([1,1],[1,1,2]))
    print(intersect([2,1,2,3],[3,1,3]))
    print("\toptimum")
    print(optimum([],0))
    print(optimum([],1))
    print(optimum([1],0))
    print(optimum([1],1))
    print(optimum([1,1,-1,100,-100],0))
    print(optimum([1,1,-1,100,-100],1))


#####################################################################################################
#PROBLEM 10
#####################################################################################################

#INPUT list of numbers 
#RETURN sum
def sigma(xlst):
    pass


#INPUT list of numbers
#RETURN sum of the squares
def sigma_square(xlst):
    pass


#INPUT list of pairs of numbers [[x0,y0],[x1,y1],...,[xn,yn]]
#RETURN sum of the products x0*y0+x1*y1+...+xn*yn
#If list is empty, return []
def sigma_product(xlst,ylst):
    pass


#INPUT takes a list of lists
#RETURN returns list of slices [0:1], [1:2], ...
#of each list
#The ORDER of the ouput is critical -- look at the
#unit test please
def separate(xlst):
    pass




#INPUT coefficents and input value to linear function
#RETURN predicted value
def linear_model(a,b,x):
    return a*x + b

#INPUT list of pairs d = [[x0,y0], [x1,y1], ... ]
#RETURN coefficients a,b as a tuple to 
#linear function f(x) = ax + b
def make_linear(xlst):
    pass


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 10")
    print("\tsigma")
    print(sigma([]))
    print(sigma([1,2,-3,3]))
    print(sigma([100,10,1]))
    print("\tsigma_square")
    print(sigma_square([]))
    print(sigma_square([-1,1,1]))
    print(sigma_square([10,2,3]))
    print("\tsigma_product")
    print(sigma_product([1,2,3],[1,10,100]))
    print(sigma_product([-1,-2,3],[9,0,3]))
    print(sigma_product([],[]))
    print("\tseparate")
    print(separate([]))
    print(separate([[1],[2],[3],[4],[5]]))
    print(separate([[1,10],[2,20]]))
    print(separate([[1,10,100],[2,20,200],[3,30,300]]))
    print(separate([[1,1],[2,3],[4,3],[3,2],[5,5]]))


    print("** To see plot uncomment the lines below **")

    # d1 = [[43,99],[21,65],[25,79],[42,75],[57,87],[59,81]]
    # d2 = [[1,1],[2,3],[4,3],[3,2],[5,5]]

    # x,y = separate(d1)
    # print(x)
    # print(y)
    # a,b = make_linear(d1)
    # print(a,b)
    # x,y = separate(d2)
    # print(x)
    # print(y)
    # a,b = make_linear(d2)
    # print(a,b)

    # #Code to visualize data
    # #BEGIN
    # import matplotlib.pyplot as plt

    # x,y = separate(d2)

    # #plot data and line
    # x1 = list(range(1,6))
    # y1 = []
    # for i in x1:
    #     y1 += [linear_model(a,b,i)]
    # plt.scatter(x,y,color="red")
    # plt.plot(x1,y1)

    # #plot predicted points
    # for i in x:
    #     plt.scatter(i,linear_model(a,b,i),color="green")

    # #plot residuals
    # for i,j in d2:
    #     plt.plot([i,i],[j,linear_model(a,b,i)], linestyle =(0, (1, 1)), color="black" )

    # #text on plot   
    # plt.text(3.2,2.27,r"residuals $|y - f(x)|$")
    # plt.ylabel(r"$f(x) = {0}x + {1}$".format(a,b))
    # plt.xlabel('x')
    # plt.title("Linear Model")

    # #render to display
    # plt.show()

    # #END

#####################################################################################################
#PROBLEM 11
#####################################################################################################

#INPUT either list, string, or tuple
#RETURN reverse list, string, or tuple
#REQUIREMENTS cannot use slicing 
#to reverse string
#if the iterable is a number DD0..0, then the
#return discards the leading zeros DD
def reverse(x):
    pass
    


#INPUT take a string
#RETURN True if the string is palindrome, False otherwise
#REQUIREMENTS treat letters as all lower case
#remove space, comma, period, question mark, exclamation
#point
def palindrome(x):
    pass


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 11")
    print("\treverse")
    xtest = ["abc", 120, (1,2,3), [1,2,3]]

    for i in xtest:
        print(reverse(i))

    print("\tpalindrome")
    xlst = ["Step on no pets.", "Was it a cat I saw?", "A",\
            "Eva, can I see bees in a cave?", "Uhh...", "Oreos yum!"]

    for i in xlst:
        print(palindrome(i))
