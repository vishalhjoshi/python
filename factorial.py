def fact1(n):
	return 1 if (n==1 or n==0) else n * fact1(n - 1)

def fact2(num):
    fact = 1
    if num == 0 or num == 1:
        fact = 1
    else:
        for i in range(1, num + 1):
            fact = fact * i
    return fact
if __name__ == '__main__':
    num = int(input('Enter a Number : >>'))
    print("(Using Recursion ) Factorial of", num, "is", fact1(num))
    print("(Using loop ) Factorial of", num, "is", fact2(num))





