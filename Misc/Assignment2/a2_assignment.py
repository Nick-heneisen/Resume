import math

#PROBLEM 1 a2_1
def s(speed_limit):

    if (speed_limit >= 55):
        return speed_limit + 5
    elif (speed_limit  >= 45):
        return speed_limit + 3
    elif (speed_limit >= 30):
        return speed_limit + 1
    else:
        return speed_limit

#PROBLEM 2 a2_2
def E(m):
    c = 3e8 #uses scientific notation
    energy = m * (c * c)
    return energy

#PROBLEM 3 a2_3
def f(fuel_price, money, gas_mileage, distance):
    return ((distance // gas_mileage) * fuel_price <= money)

#PROBLEM 4 a2_4

def law_cosines(angle, len_1, len_2):
    #convert degrees to radians
    radians = (angle * math.pi) / 180

    #math to find opposite side length
    oppSide = math.sqrt((len_1 ** 2) + (len_2 ** 2) - (2 * len_1 * len_2) * math.cos(radians))
    return oppSide

#PROBLEM 5 a2_5a

"""
Checks which value is greater of x and y, and 
returns the greater one.
"""
def max(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x


#PROBLEM 5 a2_5b

"""
Checks to see if z is greater than either x or y,
if not, it returns the greater value of x and y.
"""
def max_3(x,y,z):
    if max(x, y) > z:
        return max(x, y)
    elif max(x, y) < z:
        return z
    else:
        return z

#PROBLEM 5 a2_5c

"""
Checks to see if each variable is greater than either
one of the other 2 variables. If so, returns it.
If not, repeats for the other 2.
"""
def max_3h(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > y and z > x:
        return z
    else:
        return x

#PROBLEM 6 a2_6

"""
c1 and c2 are checked for their value, and when
they amtch up correctly they return the mixed
color
"""
def color_wheel(c1,c2):
    if c1 == c2:
        return c1
    elif c1 == "red" and c2 == "yellow":
        return "orange"
    elif c1 == "yellow" and c2 == "red":
        return "orange"
    elif c1 == "blue" and c2 == "red":
        return "purple"
    elif c1 == "red" and c2 == "blue":
        return "purple"
    elif c1 == "yellow" and c2 == "blue":
        return "green"
    elif c1 == "blue" and c2 == "yellow":
        return "green"
    else:
        return "Unknown"
     

#PROBLEM 7 a2_7a

"""
calculates the area of a circle with the given radius
"""
def pizza_area(radius):
    area = math.pi * (radius ** 2)
    return area

#PROBLEM 7 a2_7b

"""
Calculates the cost per inch of the pizzas
and returns the radius of the one with the 
lower value
"""
def cost_per_inch(r1,c1,r2,c2):
    pizza1Cost = c1 / (pizza_area(r1))
    pizza2Cost = (c2 * 2) / (pizza_area(r2) * 2)

    if pizza1Cost > pizza2Cost:
        return r2
    else:
        return r1

def pretty(asn):
    """ Print header for output of each problem

    Args:
        asn (anythong): the problem number
    """
    print(10*"~" + "problem " + str(asn) + 10*"~")

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    pretty(1)
    print(s(60),s(50),s(40),(20))

    pretty(2)
    print("{:.0e}".format(E(.1)))
    
    pretty(3)
    print(f(1, 7.50, 10, 200))
    print(f(1, 20.00, 10, 200))
    print(f(3, 20.00, 10, 200))
    print(f(3, 20.00, 35, 200))

    pretty(4)
    print(law_cosines(50,3,4))
    print(law_cosines(47,9,10))
    print(law_cosines(90,5,5))

    pretty(5)
    print(max_3(1,2,3))
    print(max_3(3,2,1))
    print(max_3(1,3,2))
    print(max_3h(1,2,3))
    print(max_3h(3,2,1))
    print(max_3h(1,3,2))

    pretty(6)
    print(color_wheel("yellow", "blue"))
    print(color_wheel("blue", "yello"))
    print(color_wheel("yellow", "yellow"))
    print(color_wheel("orange", "yellow"))

    pretty(7)
    print(cost_per_inch(18,10,12,7))
    print(cost_per_inch(18,10,12,5))
    print(cost_per_inch(18,10,12,4))