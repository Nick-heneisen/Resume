"""
    C200 Homework Assignment 7 : PPM Processing

    Name: Nicholas Heneisen

    Date:   10/28/21

    The goal of this assignment is to give you practice working with nested lists
    by writing a program that manipulates the entire image with multiple lines.
"""
def process(lines, rows, cols):
    """
    Processes function's lines and columns

    Args: (list, int, int)

    Returns: (list)
    """
    answer = [None] * rows
    for i in range(rows):
        lines[i] = lines[i].strip()
        answer[i] = lines[i].split()
        for j in range(cols * 3):
            answer[i][j] = int(answer[i][j])
    return answer

def read_ppm(filename):
    """
    Reads from an existing file

    Args: (string)

    Returns: (list)
    """
    ppm = open(filename, 'r')
    ppm = ppm.readlines()
    number = ppm[1].split()
    number = [int(i) for i in number]
    return process(ppm[3:], number[1], number[0])

def write_ppm(image, filename):
    """
    Writes to an existing file or creates a new one

    Args: (list, string)

    Returns: none (writes to a file)
    """
    cols = len(image[0])
    rows = len(image)
    output = open(filename, "w+")
    output.write("P3\n" + str (cols // 3) + " " + str(rows) + "\n" + '255\n')
    for i in image:
        for j in i:
            output.write(str(j) + " ")
        output.write("\n")
    pass

def scale(image, row_scale, col_scale):
    """
    Scales an image to a different size

    Args: (list, int, int)

    Returns: (list)
    """
    answer = []
    final = []
    for i, row in enumerate(image):
        if i % row_scale == 0:
            answer.append(row)
    for row in answer:
        newLine = []
        for j, col in enumerate(row):
            if j // 3 % col_scale == 0:
                newLine.append(col)
        final.append(newLine)
    return final


def main():
    # TODO:
    """
    1. Ask the user for an input file name.
    2. Ask the user for an output file name.
    3. Ask the user for a height scaling factor.
    4. Ask the user for a width scaling factor.
        (Note that you should enforce both scaling factors
        must be positive integers)
    5. The program will read from the input file and create a
    new file with the specified name that contains a copy of the
    input file scaled down by the specified factors.
    """
    inputFile = input("Input file name:")
    outputFile = input("Output file name:")
    height = -1
    width = -1
    while int(height) < 0:
        height = input("Height scaling factor:")
    while int(width) < 0:
        width = input("Width scaling factor:")
    
    write_ppm(scale(read_ppm(inputFile),int(height),int(width)),outputFile)
    
    pass

main()