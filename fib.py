def fibonacci(n):
    a = 0
    b = 1
    if n<0:
        print("Invalid Input!")
    elif n ==1:
        print(a, end=' ')
    else:
        print(a, end=' ')
        print(b, end=' ')
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end=' ')

num2 = int(input("Enter Number To Print Fibonacci Sequence :>>"))
fibonacci(num2)

