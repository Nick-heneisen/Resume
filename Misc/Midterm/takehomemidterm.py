import random as rn
import numpy as np

"""
Problem 1
""" 
def unique_words(xstring):
    """Problem 1.  Find the unique words in a string

    Args: (string)

    Returns: (list)

    """
    words = []
    lowered = xstring.lower()
    xlst = lowered.split()

    for i in xlst:
        strip = i.strip(".,!?")
        if strip not in words:
            words.append(strip)

    return words

def put_list(str):
    """Custom helper function. Changes a string to a list

    Args: (string)

    Returns: (list)

    """
    words = []
    lowered = str.lower()
    xlst = lowered.split()
    for i in xlst:
        strip = i.strip(".,!?")
        words.append(strip)
    return words

def get_transition_matrix(xtr):
    """Problem 1.  Generate the transition matrix

    Args: (string)

    Returns: (list)
    """
    diction = {}
    for i in unique_words(xtr):
        if i not in diction:
            diction[i] = 0
    sentList = put_list(xtr)

    matrix = []
    for i in unique_words(xtr):
        tempList = []
        for j in (range(len(sentList) - 1)):
            if i == sentList[j]:
                diction[sentList[j + 1]] += 1
            
        for k in diction:
            tempList.append(diction[k])
            diction[k] = 0
        matrix.append(tempList)
    return matrix

"""
Problem 2
"""
def rand_list(listSize):
    randList = []
    for i in range(listSize):
        randNumber = rn.randint(1, 99)
        randList.append(randNumber)

    return randList

def running_average(xlist,per):
    """Problem 2.  Compute the running average

    Args: (list, integer)

    Returns: (list)

    """
    results = []
    for i in range(len(xlist) - (per - 1)):
        sums = []
        counter = 0
        for j in range(per):
            sums.append(xlist[i + counter])
            counter += 1
        average = 0
        for k in sums:
            average += k
        average /= per
        results.append(average)

    return results

##########################################################################
if __name__ == "__main__":
    # Fill in with code to test your functions for both problems
    # Note that the np.array() function converts the list that is returned to 
    # a numpy array. This is only done for display/print purposes, so be sure that
    # your function returns a list.

    print("\nPROBLEM 1 \n=================================")
    text = "The cat is in the house. The dog is outside playing with the kids. Both the dog and the cat need a bath. The kids need to come in and eat dinner."
    uniText = unique_words(text)
    print(unique_words(text))
    print("There are {0} unique words in the text.".format(len(uniText)))
    print("The Transition Matrix is Below:")
    print(np.array(get_transition_matrix(text)))

    print("\nPROBLEM 2 \n=================================")
    listSize = rn.randint(3, 9)
    data = rand_list(listSize)
    print(data)
    period = 3
    runningAverage = running_average(data, period)
    print("The {0}-day running average is: {1}".format(period, runningAverage))
    pass
