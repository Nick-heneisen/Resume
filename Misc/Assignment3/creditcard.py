"""
    C200 Assignment 3: Credit Cards

    Author: Nicholas Heneisen

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""

from random import randint, random
from creditcard_part1 import last_digit, decimal_right_shift

def verify(number13):
    """
    Verifies that the inputted number is a valid credit card

    Args:
        (int): 13 integers

    Returns:
        (int) : True or false
    """

    thirteen = last_digit(number13)
    twelve = last_digit(decimal_right_shift(number13)) * 2
    eleven = last_digit(decimal_right_shift(decimal_right_shift(number13)))
    ten = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))) * 2
    nine = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))
    eight = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))) * 2
    seven = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))
    six = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))) * 2
    five = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))))
    four = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))))) * 2
    three = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))))))
    two = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))))))) * 2
    one = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number13)))))))))))))

    answer = one + (last_digit(two) + decimal_right_shift(two)) + three + ((last_digit(four)) + decimal_right_shift(four)) + five + (last_digit(six) + decimal_right_shift(six)) + seven + (last_digit(eight) + decimal_right_shift(eight)) + nine + (last_digit(ten) + decimal_right_shift(ten)) + eleven + (last_digit(twelve) + decimal_right_shift(twelve)) + thirteen

    if last_digit(answer) == 0:
        return True
    else:
        return False

def generate(number6):
    """
    Generates a 13 number sequence with the 
    first 6 digits entered in the terminal

    Args:
        (int): 6 numbers

    Returns:
        (int) : 13 numbers that are a valid card number
    """
    six = last_digit(number6)
    five = last_digit(decimal_right_shift(number6)) * 2
    four = last_digit(decimal_right_shift(decimal_right_shift(number6)))
    three = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(number6)))) * 2
    two = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number6)))))
    one = last_digit(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(decimal_right_shift(number6)))))) * 2

    firstHalf = one + (last_digit(two) + decimal_right_shift(two)) + three + ((last_digit(four)) + decimal_right_shift(four)) + five + (last_digit(six) + decimal_right_shift(six))

        #make variable exist before loop
    bothAdded = 1

    while verify(bothAdded) != True:

        rand_1 = randint(0, 9)
        rand_2 = (randint(0, 9) * 2)
        rand_3 = randint(0, 9)
        rand_4 = (randint(0, 9) * 2)
        rand_5 = randint(0, 9)
        rand_6 = (randint(0, 9) * 2)
        rand_7 = randint(0, 9)

        answer = firstHalf + rand_1 + (last_digit(rand_2) + decimal_right_shift(rand_2)) + rand_3 + (last_digit(rand_4) + decimal_right_shift(rand_4)) + rand_5 + (last_digit(rand_6) + decimal_right_shift(rand_6)) + rand_7
            
        if last_digit(answer) == 0:
                bothAdded = True
        else:
                bothAdded = False
        break

    return one, two, three, four, five, six, rand_1, rand_2, rand_3, rand_4, rand_5, rand_6, rand_7

# Possible return values
#
# "<num> is not all digits"
#
# "<num> is not six digits"
#
# "Three valid numbers:"
# "\t<num1>"
# "\t<num2>"
# "\t<num3>"
def main():
    num = (input("Enter a 6 digit number:\n"))

    if num > 999999 or num < 100000:
        print("Number is not 6 digits")
    else:
        return generate(num)

pass
    
if __name__ == "__main__":
    main()
