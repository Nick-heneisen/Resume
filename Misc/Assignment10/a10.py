import random as rn
import math

#############################################
# Problem 1
#############################################
def sel_sqrt(a,b):
    """
    Returns the square root if the number is odd, 
    or multiplies it by 2 if it is even

    Args: (int, int)

    Returns: (list)
    """
    return [round(math.sqrt(i), 2) if i % 2 else 2 * i for i in range(a,b)]

def inchtomtuple_lc(hlist_in):
    """
    Returns a list of the hieghts of people in inches and meters

    Args: (list)

    Returns: (list)
    """
    return [((i), round(i * 0.0254, 4)) for i in hlist_in]

def intomtuple_map(hlist_in):
    """
    Returns a list of the hieghts of people in inches and meters

    Args: (list)

    Returns: (list)
    """
    return list(map(lambda x: (x, round(x * .0254, 4)), hlist_in))

#############################################
# Problem 2
#############################################
def bmi_calc(weight, height):
    """
    Calculates the bmi of someone based off of the height and weight

    Args: (int, int)

    Returns: (tuple)
    """
    return 703 * (weight / (height ** 2))
    
def bmi_lc(blist):
    """
    Puts the BMI's of people in a list

    Args:
        blist (list): list of weights and heights

    Returns:
        list: list of bmis
    """
    return [round(bmi_calc(i[0], i[1]), 2) for i in blist]

def bmi_map(blist):
    """
    Puts the BMI's of people in a list

    Args:
        blist (list): list of weights and heights

    Returns:
        list: list of bmis
    """
    return list(map(lambda i: round(bmi_calc(i[0], i[1]), 2), blist))

def bmi_cat(bmilist):
    """
    Categorizes the BMIs and puts it into a list of all of them

    Args:
        bmilist (list): List of bmis

    Returns:
        list: list of bmis and their category
    """
    return [(i, "Underweight") if i < 18.5 else (i, "Normal") if i >= 18.5 and i < 25 else (i, "Overweight") if i >= 25 and i < 30 else (i, "Obese") for i in bmilist]

#############################################
# Problem 3
#############################################
def bubble_sort(a):
    """
    Sorts the inputted list from smallest to largest.

    Args:
        a (list): list of integers

    Returns:
        list: list of sorted integers
    """
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]

    return a

def wbubble_sort(a):
    """
    Sorts the inputted list from smallest to largest.

    Args:
        a (list): list of integers

    Returns:
        list: list of sorted integers
    """
    i = 0
    while i < len(a):
        j = 0 
        while j < (len(a)) - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    return a

#############################################
# Problem 4
#############################################
def rsel_sort(xlst):
    """
    Sorts the values in the inputted list from smallest to largest

    Args:
        xlst (list): list of integers

    Returns:
        list: sorted list
    """
    newList = []
    def sort(xlst):
        if xlst == []:
            return newList
        else:
            newList.append(min(xlst))
            xlst.remove(min(xlst))
            return sort(xlst)
    return sort(xlst)

#############################################
# Main
#############################################
if __name__ == "__main__": 
    # Problem 1a
    print("sel_sqrt")
    print(sel_sqrt(0,10))
    print(sel_sqrt(10,15))
    print(sel_sqrt(15,20),"\n")

    # Problem 1
    print("Heights")
    heights = []

    for i in range(10):
        heights.append(rn.randint(48,90))
    print(heights)

    print(inchtomtuple_lc(heights))
    print(intomtuple_map(heights),"\n")

    # Problem 2
    print("BMI")
    wh = []
    for i in range(10):
        wh.append((rn.randint(100, 300), heights[i]))
    print(wh)

    print("bmi LC: ", bmi_lc(wh))
    print("bmi Map: ", bmi_map(wh))
    print("bmi Cat: ", bmi_cat(bmi_map(wh)))

    # Problem 3 
    print("Bubble Sort") 
    test = []

    for i in range(10):
        test.append(rn.randint(0,100))
    print(test)

    print(bubble_sort(test))
    print(wbubble_sort(test),"\n")

    # Problem 4
    print("Selection Sort")
    test = []

    for i in range(10):
        test.append(rn.randint(0,100))
    print(test)
    print(rsel_sort(test))

