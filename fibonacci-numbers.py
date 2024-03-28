"""
The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….. 
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.

 Fn = Fn-1 + Fn-2

with seed values : F0 = 0 and F1 = 1.
"""


n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

# Output: 1 2 3 5 8 13 21 34 55 89 

"""
Fibonacci numbers using Recursion.
The term Recursion can be defined as the process of defining something in terms of itself. 
In simple words, it is a process in which a function calls itself directly or indirectly. 
"""

def Fibonacci(n):
 
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
 
# Driver Program
print(Fibonacci(9))
