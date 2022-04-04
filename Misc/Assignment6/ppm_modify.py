import os
"""
    C200 Homework Assignment 6 : ppm modify

    Author: Nicholas Heneisen

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.
"""
from math import sqrt

def put_list(i): 
    """
    Puts the values in the string into a list

    Input: (string)

    returns: (list)
    """
    listOfNums = []
    value = 0
    counter = 0
    for j in i:
        if counter >= 3:
            j.strip()
            value = j.split()
            listOfNums.append(value)
        else:
            counter += 1
    return listOfNums

def to_string(list):
    """
    Converts a list to a string

    Input: (list)

    return: (string)
    """
    string = " "
    width = 0
    for i in list:
        width = -1
        i.append("\n")
        for j in i:
            string += str(j)
            string += " "
            width += 1
    height = len(list)
    width = (width / 3)
    return string

def color_translate(line):
    """
    decodes the inputted string and returns it

    input: (string)

    returns: (string)
    """
    bigList = put_list(line)
    
    for i in bigList:
        for j in range(len(i)):
            if int(i[j]) % 3 == 0:
                i[j] = 0
            elif int(i[j]) % 3 == 1:
                i[j] = 153
            elif int(i[j]) % 3 == 2:
                i[j] = 255
    return to_string(bigList)

def process_ppm(in_filename, out_filename, filter):
    """
    processes the given file's for inputting and outputting the ppm

    Args: (string, string, function)

    Returns: (file)
    """
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement the process function as specified in the handout
    with open(in_filename, "r") as inputFile:
        input = inputFile.readlines()

    prefix1 = input[0]
    prefix2 = input[1]
    prefix3 = input[2]

    with open(out_filename, "w") as outputFile:
        output = outputFile.write((prefix1 + prefix2 + prefix3 + filter(input)))
    return output

def main_part1():
    """
    processes the files "part1.ppm" into "part1_output.ppm"

    Args: (none)

    Returns: (none)
    """
    # TODO: call the <decode> function you developed to decode
    #  the image <files/part1.ppm>
    process_ppm("Assignment6/files/part1.ppm", "Assignment6/files/part1_output.ppm", color_translate)
    pass

def grey_scale(line):
    """
    turns the inputted string into greyscale ppm format

    Args: (string)

    Returns: (string)
    """
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement the grey_scale function as specified in the handout
    bigList = put_list(line)
    # grey = sqrt((r**2+g**2+b**2))
    count = 0
    for i in bigList:
        for j in range(len(i)):
            i[j] = int(i[j])**2
            if count == 2:
                grey = int(sqrt(int(i[j]) + int(i[j - 1]) + int(i[j - 2])))
                count = 0
                if grey > 255:
                    grey = 255
                    i[j] = grey
                    i[j - 1] = grey
                    i[j - 2] = grey
                else:
                    i[j] = grey
                    i[j - 1] = grey
                    i[j - 2] = grey
            else:
                count += 1
    return to_string(bigList)

def main():
    """
    turns inputted ppm file into greyscale

    Args: (none)

    Returns: (none)
    """
    # TODO: implement the following required items:
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. Perform grey_scale conversion on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    4. Write the complete docstring
    """
    inputFile = input("input file:")
    outputFile = input("output file:")
    process_ppm(inputFile, outputFile, grey_scale)
    print("done")


if __name__ == '__main__':
   # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
