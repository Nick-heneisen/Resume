import math
import itertools

##FOR ME ==== COMMAND + K + C (COMMENT), COMMAND + K + U (UNCOMMENT)

##########################################################################
#PROBLEM 1
##########################################################################
#
#INPUT positive number n
#RETURN log of number base 2
def log_2(n):
    """
    returns the log base 2 of (input)

    input: (integer)

    returns: (integer)
    """
    if n == 0:
        return 0
    elif n < 0:
        return "Value must not be negative."
    else:
        return math.log2(n)

#INPUT list of immutable objects
#RETURN probability distribution
s0 = ["a", "b", "a", "c", "c", "a"]

def makeProbability(xlst):
    """
    returns probability of selecting a value 
    in a list

    input: (list)

    returns: (list)
    """
    values = {}
    total = 0
    ratio = []
    for i in xlst:
        if i in values:
            values[i] += 1
            total += 1
        else:
            values[i] = 1
            total += 1

    for i in values:
        ratio.append(values[i] / total)
    return ratio

#INPUT probability distribution
#RETURN non-negative number entropy
def entropy(xlst):
    """
    returns the entropy of the numbers 
    in the inputted list

    input: (list)

    returns: (float)
    """
    final = 0
    sums = []
    for i in xlst:
        result = (i * log_2(i))
        sums.append(result)
    for i in sums:
        final += i

    if final == 0:
        return 0.0
    else:
        return final * -1
    

         



##########################################################################
#PROBLEM 2
##########################################################################
#INPUT positive integer
#RETURN positive integer
def magick(x):
    """
    returns your input

    input: (integer)

    returns: (integer)
    """
    x += 15
    x *= 3
    x -= 9
    x /= 3
    x -= 12
    return x

##########################################################################
#PROBLEM 3
##########################################################################
#INPUT a list of lists of three positive integers [[a,b,c],[d,e,f],[g,h,i]]
#RETURN True if the input is a magic square
#You can create other functions to help you--they will 
#not be unit tested

def is_magic_square(s3):
    """
    returns whether or not the inputted list 
    is a magic square or not

    inputs: (list)

    returns: (boolean)
    """
    length = len(s3)
    sum1 = 0
    sum2 = 0
    for i in range(length):
        sum1 += s3[i][0]
    for i in range(length):
        for j in range(length):
            sum2 += s3[i][j]
        if sum1 != sum2:
            return False
        sum2 = 0
    one = s3[2][0]
    two = s3[1][1]
    three = s3[0][2]
    if one + two + three != sum1:
        return False
    for i in range(1, length):
        for j in range(length):
            sum2 += s3[j][i]
        if sum1 != sum2:
            return False
        sum2 = 0
    for i in range(length):
        sum2 += s3[i][i]
    if sum1 != sum2:
        return False
    if sum1 != 15:
        return False

    return True

#INPUT nothing
#RETURN list of solutions to magic square size 3
"""
returns a list of lists that are magic 
squares

input: none

returns: (list)
"""
def generate_3_square():
    list_1 = []
    for i in itertools.permutations(range(1, 10)):
        a = list(i)
        temp = []
        temp.append(a[0:3])
        temp.append(a[3:6])
        temp.append(a[6:9])
        if is_magic_square(temp):
            list_1.append(temp)
    return list_1



##########################################################################
# PROBLEM 4
##########################################################################

#INPUT takes a letter and shift
#RETURN new letter shifted 
def encrypt(letter, n):
    """
    shifts the inputted letter by n letters to the left

    inputs: (string, integer)

    returns: (string)
    """
    newLetter = chr(ord(letter) + n)
    return newLetter

#INPUT takes a letter and shift
#RETURN original letter
def decrypt(letter, n):
    """
    shifts the inputted letter by n letters to the right

    inputs: (string, integer)

    returns: (string)
    """
    oldLetter = chr(ord(letter) - n)
    return oldLetter

#INPUT takes a sentence of lowercase letters and spaces and shift
#RETURN caeser cypher
def encrypt_sentence(sentence, shift):
    """
    encrypts the inputted sentence

    inputs: (string, integer)

    returns: (string)
    """
    newSentence = sentence.replace(" ", "{")
    encryptedSentence = ""
    for i in newSentence:
        encryptedSentence += encrypt(i, shift)
    return encryptedSentence

#INPUT takes an encrypted sentence and shift
#RETURN decrypted sentence
def decrypt_sentence(sentence, shift):
    """
    decrypts the inputted sentence

    inputs: (string, integer)

    returns: (string)
    """
    decryptedSentence = ""
    for i in sentence:
        decryptedSentence += decrypt(i, shift)
    oldSentence = decryptedSentence.replace("{", " ")
    return oldSentence

##########################################################################
# PROBLEM 5
##########################################################################

#INPUT non-negative integer and non-negative integer > 1
#RETURN Wild Number [string, base]
#string is encoding of number in base, base is integer
def make_number(decimal, base):
    """
    Converts a base 10 decimal number to 
    a binary base 2 number

    input: (integer, integer)

    returns: (string, integer)
    """
    answer = ""
    if decimal == 0:
        return ["0", base]
    list = []
    while decimal:
        list.append(str(int(decimal % base)))
        decimal //= base
    for i in list:
        answer += i
    return [answer[::-1], base]


#INPUT Wild number 
#RETURN new wild number in new base
def convert(number, base):
    """
    Converts a base 2 binary number to 
    a decimal base 10 number

    input: (integer, integer)

    returns: (string, integer)
    """
    result = int(number[0], number[1])
    answer = make_number(result, base)
    return answer

#INPUT two wild numbers
#RETURN product as a (possibly new) base
def mul_(number1, number2, base):
    """
    returns the product of two wild numbers at the 
    given base

    input: (integer, integer, integer)

    returns: (integer)
    """
    num1 = int(number1[0], number1[1])
    num2 = int(number2[0], number2[1])
    answer = make_number(num1 * num2, base)
    return answer

#INPUT two wild numbers
#RETURN sum as a (possibly new) base
def add_(number1, number2, base):
    """
    returns the product of two wild numbers at the 
    given base

    input: (integer, integer, integer)

    returns: (integer)
    """
    num1 = int(number1[0], number1[1])
    num2 = int(number2[0], number2[1])
    answer = make_number(num1 + num2, base)
    return answer

# Problem 6

#INPUT path to amino acid file
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
def get_amino_acids(file_path):
    file = open(file_path, "r")
    result = {}
    for line in file:
        index = tuple(line.split(", ")[2:])
        index = tuple(element.strip() for element in index)
        result[index] = [line.split(",")[0], line.split(", ")[1]]
    return result


#INPUT path to DNA file
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
def get_DNA(file_path):
    file = open(file_path, "r")
    answer = []
    string = ""
    answer.append(file.readline().strip())
    for i in file:
        string += i.strip()
    answer.append(string)

    return answer

#INPUT FAST file
#RETURN a string representing the protein
#using the dictionary
def translate(DNA_d):
    acids = get_amino_acids("amino_acids.txt")
    result = ""
    for i in range(0, len(DNA_d[1]), 3):
        temporary = ""
        temporary += DNA_d[1][i]
        temporary += DNA_d[1][i + 1]
        temporary += DNA_d[1][i + 2]
        for key in acids:
            for item in key:
                if item == temporary:
                    result += acids[key][1]
    return result

#Do not modify these statements

aa_d = {}   #the dictionary for the transation
DNA_d = []  #the FASTA file
protein = ''

def init_data(amino_acids_file, dna_file):
    global aa_d
    global DNA_d
    global protein
    aa_d = get_amino_acids(amino_acids_file)
    DNA_d = get_DNA(dna_file)
    protein = translate(DNA_d)


##########################################################################
if __name__ == "__main__":
    print("For your use...")
    actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"
    init_data("amino_acids.txt","DNA.txt")
    print("Please comment the code you want to run. Make sure it is inside of this if statement")
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")

    
    print("*"*10 + "Problem 1"+"*"*10 +  "\n")
    s0 = ["a", "b", "a", "c", "c", "a"]
    s1 = ['a','b','a','b','a','b','b','b']
    s2 = [(1),(2),(3),(4)]
    s3 = [1]
    s4 = [1,2,1,2]

    xlst = [s0, s1,s2,s3,s4]

    for i in xlst:
        p = makeProbability(i) 
        e = entropy(p)
        print(f"{p} has entropy {e}")

    print("*"*10 + "Problem 3"+"*"*10 +  "\n")
    s1 = [[2,7,6],[9,5,1],[4,3,8]] #True
    s2 = [[8,1,6],[3,5,7],[4,9,2]] #True
    s3 = [[8,6,1],[3,6,7],[4,9,2]] #False
    s4 = [[1,1,1],[1,1,1],[1,1,1]] #False
    s = [s1,s2,s3,s4]
    for i in s:
        print("{0} is ".format(i) + "not "*(not is_magic_square(i)) + "a magic square." )
    print(generate_3_square())

    print("*"*10 + "Problem 4"+"*"*10 +  "\n")
    sentence = "this is a secret message about the class"
    shift = 5
    secret = encrypt_sentence(sentence, shift)
    decode_secret = decrypt_sentence(secret, shift)
    
    print(f"original: {sentence}")
    print(f"encrypted: {secret}")
    print(f"decrypted: {decode_secret}")

    print("*"*10 + "Problem 5"+"*"*10 +  "\n")    
    n1,n2 = 5,4
    base2, base10 = 2,10

    x1, y1 = make_number(n1,base2), make_number(n2,base2)
    print(x1,y1)
    print(convert(x1,base10))
    print(add_(x1,y1,base10))
    print(add_(x1,y1,base2))
    print(convert(add_(x1,y1,base2), base10))
    print(mul_(x1,y1,base2))
    print(convert(mul_(x1,y1,base2),base10))

    print("*"*10 + "Problem 6"+"*"*10 +  "\n") 

    print("Dictionary")
    print(aa_d)
    print("FASTA file")
    print(DNA_d)
    print("Translations match:", str(protein == actual))

    # should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"]))

    # should return "D-"
    # print(translate(["nothing", "GACTAA"]))