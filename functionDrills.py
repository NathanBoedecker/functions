'''
@author: amayamunoz
'''
from builtins import True

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract_two_numbers(num1, num2):
    differenceOfTwoNumbers = num1 - num2
    return differenceOfTwoNumbers
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def func2(num1):
    a = num1 / 2 
    b = a * 77
    c = b + 10000
    return c 
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def func3(num1, num2):
    if num1 = num2:
        return True
    else
        return False
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def func4(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 = num2:
        return num1
    
#5) Define a function that takes in two words and returns a string that contains both words combined.
def funct5(string1, string2):
    ans5 = string1 + string2
    return ans5
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def func6(num1, num2, num3):
    if num1 = num2 or num1 = num3:
        return True
    else:
        return False
#7) Define a function that prints your name.
def func7(name):
    print(name)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def func8(favColor):
    if favColor = "Red":
        print("That's my favorite color")
    else:
        print("That is not my favorite color. Try again")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def func9(num1):
    while num1 > 0:
        num1 = num1 - 1
        
'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.
def func10(num1, num2, num3):
    if num1 = num2 and num2 - num3:
        return True
    else
        return False