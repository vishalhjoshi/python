import factorial # import factorial module
from fib import fib # import fib module from fib package

num = int(input("Enter Number To Calculate Factorial :>>"))
print(f'Factorial of {num} is {factorial.fact2(num)}')

num2 = int(input("Enter Number To Print Fibonacci Sequence :>>"))
fib.fibonacci(num2)