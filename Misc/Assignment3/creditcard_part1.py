"""
    C200 Assignments 3: Credit Cards, Part 1

    Name: Nicholas Heneisen
   
    Date:   9/21/21

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""

def last_digit(num):
    """Computes the last digit of the num

    Args:
        num (int): A positive integer

    Returns:
        (int) : The last digit of num (123 -> 3)
    """
    return(num % 10)

# Right shifts num by one digit
#  123 -> 12



def decimal_right_shift(num):
    """
divides the number by 10, and since integers
don't take decimals, gives you
all but the last number
"""
    return num // 10


# Sum digits of the input -- assume there
# are exactly three digits
"""
uses previous functions to add all digits of
the inputted number together.
"""

def sum_digits(num):
    number0 = last_digit(num)
    number1 = decimal_right_shift(num)
    number2 = last_digit(number1)
    number3 = decimal_right_shift(number1)
    return number0 + number2 + number3


# Ask the user for input and print a message
# Three possible messages:
#    "Number must be all digits"
#    "Number must be three digits"
#    "The sum of the digits of <num> is <result>"
def main():
    num = int(input("Please enter a 3-digit positive number:\n\t"))
    if  num > 999 or num < 100:
        print("Number must be three digits")
    else:
        print("The sum of the digits of", (num), "is", sum_digits(num))
    pass

if __name__ == "__main__":
    main()

