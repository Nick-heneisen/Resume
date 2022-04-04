
###############
# PROBLEM ONE
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os


def get_data(path,name):
    """
    Gets a file

    Args: (string, string)

    Returns: (list)
    """
    tmp = []
    pn = os.path.join(path, name)
    file = open(pn, "r")
    for d in file:
        x,y = d.split(",")
        tmp += [[int(x), int(y)]]
    return tmp


def pop(year):
    """
    Finds the population for a year

    Args: (int)

    Returns: (float)
    """
    return 1436.53 * (1.01395) ** year

def error(data):   
    """
    Finds the error value of the graph

    Args: (string)

    Returns: (int)
    """
    graph = []
    for i in range(0, 120, 10):
        value = [i, pop(i)]
        graph.append(value)

    errorList = []
    for i in range(0, 12):
        errorList.append([abs((data[i][1])-graph[i][1])/data[i][1]])
    errorValue = 0
    for i in errorList:
        errorValue += i[0] * 100 / 12
    return errorValue




if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    """

    data = get_data("./Assignment9/", "pop.txt")

    total_error = round(error(data),4)

    t = np.arange(0.0, 120.0)
    fig,ax = plt.subplots()

    ax.plot(t, pop(t),'g')
    for y,p in data:
        ax.plot(y,p,'ro--')

    ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    title = "Population Growth. Total ave error = %{0}".format(total_error))
    ax.grid()
    plt.show()

###############
# PROBLEM TWO
###############
import csv

def my_int(xstr):
    if xstr == "":
        return 0
    else:
        return int(xstr)
        
# #INPUT state and state dictionary of data
# #RETURN give the total confirmed deaths for 
# # entire state
def scd(state,dic):
    """
    Finds the total deaths for a state

    Args: (string, dictionary)

    Returns: (int)
    """
    sumDeaths = []
    for i in dic:
        if i[0] == state:
            sumDeaths.append(dic[i][1])
    finalSum = sum(sumDeaths)
    return finalSum

# #INPUT dictionary data and interval (a,b)
# #RETURN all confirmed county cases greater than or equal to a
# #and strictly less than b
def ccc(dic,interval):
    """
    Finds the county confirmed deaths

    Args: (dictionary, tuple)

    Returns: (dictionary)
    """
    newDic = {}
    for i in dic:
        if interval[1] == float('inf'):
            second = 9999999999999999999999999999999999999999
        else:
            second = interval[1]

        if int(interval[0]) <= int(dic[i][0]) and int(dic[i][0]) <= int(second):
            newDic[i] = dic[i][0]
    return newDic

# #INPUT state, data dictionary, state population
# #RETURN state death density: confirmed deaths / population of state
# #as a percentage to 3 places use round(x*100,3)
def sdd(state, dic, state_pop):
    """
    Finds the percentage death density

    Args: (string, dictionary, dictionary)
    """
    population = 0
    deaths = scd(state, dic)
    for i in state_pop:
        if i == state:
            population = int(state_pop[i])
    return round((deaths / population) * 100, 3)

# #INPUT data dictionary and state population 
# #RETURN return the entire US death density
def usdd(dic, state_pop):
    """
    Finds the US state population

    Args: (dictionary, dictionary)

    Returns: (dictionary)
    """
    deathDic = {}
    for i in state_pop:
        state = i
        deathDic[state] = sdd(state, dic, state_pop)
    return deathDic

def get_dic(file_path):
    """
    Opens the file for the dictionary

    Args: (string)

    Returns: (dictionary)
    """
#     """
#     Reading from the file passed in, 
#     extract the following information into a dictionary and RETURN a dictionary. 

#     The key for the dictionary (also described in the document): a tuple
#     The value for each key (also described in the document): a list of size 2 (both need to be integers)

#     To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
#     If you want to do it another way, please ask before attempting to use a method not talked about in class.

#     HINT: You will need to skip the first row. 
#             If you use a CSV reader, you can skip a row by doing `next(reader, None)`
#     """
    with open(file_path, 'r') as file:
        inputFile = file.read()
        final = []
        splitList = inputFile.split("\n")
        for line in splitList:
            final.append(line.split(","))
    dic = {}
    final = final[1:]
    counter = -1
    count2 = -1
    for i in final:
        counter += 1
        count2 = -1
        for j in i:
            count2 += 1
            if j == '':
                final[counter][count2] = 0
    
        dic[i[2], i[1]] = [int(i[6]), int(i[7])]
    return dic

def get_state_pop(file_path):
    """
    Opens the file for the state populations

    Args: (string)

    Returns: (dictionary)
    """
#     """
#     Reading from the file passed in, 
#     extract the following information into a dictionary and RETURN a dictionary. 

#     The key for the dictionary (also described in the document): a string
#     The value for each key (also described in the document): an integer

#     To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
#     If you want to do it another way, please ask before attempting to use a method not talked about in class.
#     """
    with open(file_path,'r')as f:
        readfile = f.read()
        statepop = []
        split_list = readfile.split("\n")
        for line in split_list:
            statepop.append(line.split(","))
        statepop_dic = {}

        #puts into a dictionary
        for i in statepop:
            statepop_dic[i[0]] = i[-1]
        del statepop_dic['']
        return statepop_dic

if __name__ == "__main__":
#     """
#     The code in "__main__" is not being graded, but a tool for you to test 
#     your code outside of the `test_a9.py`. Feel free to add print statements. 
#     # """

#     #Our solutions used these two dictionaries 
#     # has state, county, confirmed case, comfirmed deaths 
#     # has state *most* current population 
    dic = get_dic("/Users/nickheneisen/Github/C200-Assignments-nheneise/Assignment9/us-counties.csv")
    state_pop = get_state_pop("/Users/nickheneisen/Github/C200-Assignments-nheneise/Assignment9/sp.csv")

# #     #county confirmed cases
    intervals = [(0,1),(1,2),(0,2)]
    c0 = ccc(dic,intervals[0])
    c1 = ccc(dic,intervals[1])
    c2 = ccc(dic,intervals[2])
    # if c0:
    #     print(f"Number of state-counties {intervals[0]} is {c0[intervals[0]]}")
    # if c1:
    #     print(f"Number of state-counties {intervals[1]} is {c1[intervals[1]]}")
    # if c2:
    #     print(f"Number of state-counties {intervals[2]} is {c2[intervals[2]]}")
    max = float('inf')
    cm = ccc(dic,(266380,max))
    print(">= 266380 confirmed cases")
    print(cm)

# #     #state confirmed deaths
    print(f"Alabama: {scd('Alabama', dic)}")
    if state_pop:
        print(f"Alabama state pop: {state_pop['Alabama']}")
    print(f"Alabama death density: {sdd('Alabama', dic, state_pop)}%")
    print(f"{round((8166 / 4903185)*100, 3)}%")

# #     #entire country death density percentage
    x = usdd(dic,state_pop)
    if x:
        print(f"Alabama: {x['Alabama']}%")
        # print(x["Texas"])
    pass
###############
# PROBLEM THREE
###############
import math 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
simpson takes a function,beginning and ending points a and b, and the number of intervals
 over which to estimate the integration

 for example, we might define a function

 def some_function(x): 
     return 3*x*x + 1

 and estimate the integral from 0 to 6 with 100 steps

 simpson(some_function,0,6,100)
 """

def simpson(fn,a,b,n):
    """
    Uses the simpson function to calculate the area under a curve on an interval

    Args: (function, int, int, int)
    
    Returns: (float)
    """
    interval = (b - a) / n
    sumList = []
    countOther = 0
    countFull = a
    # print(interval, "interval")
    if a > 0:
        zero = 1
    else:
        zero = 0
    for i in range(a - zero, n + 1):
        i *= interval
        if countFull == a:
            # print(i, "first")
            sumList.append(fn(a))
            countFull += 1
        elif i == n * interval:
            # print(i, "last")
            sumList.append(fn(i + a))
        elif countOther % 2: 
            # print(fn(i + a) * 2, "even")
            sumList.append(fn(i + a) * 2)
            countOther += 1
            countFull += 1
        else:
            # print(fn(i + a) * 4, "odd")
            sumList.append(fn(i + a) * 4)
            countOther += 1
            countFull += 1
    # print(sumList)

    return sum(sumList) * (interval / 3)


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    """

    # data = [[lambda x:3*(x**2)+1, 0,6,2],
    #         [lambda x:x**2,0,5,6],
    #         [lambda x:math.sin(x), 0,math.pi, 4],
    #         [lambda x:1/x, 1, 11, 6]]


    # for d in data:
    #     f,a,b,n = d
    #     print(simpson(f,a,b,n))

    # t = np.arange(0.0, 10.0,.1)
    # fig,ax = plt.subplots()
    # s = np.arange(0,6.1,.1)
    # ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    # plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    # ax.grid()
    # ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
    # title = r"Area under the curve $\int_0^6\,f(x)$")

    # plt.show()