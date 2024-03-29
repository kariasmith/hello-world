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

    A lot of memory and time is taken through recursive calls which makes it expensive for use.
    Recursive functions are challenging to debug.
    The reasoning behind recursion can sometimes be tough to think through.

"""


# Program to print the fibonacci series upto n_terms
 
# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
n_terms = 10
 
# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))

