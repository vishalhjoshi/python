def sum_of_digit(digit):
    digit = str(digit)
    sum = 0
    for i in digit:
        sum = sum+int(i)
    return sum


try :
    digit = int(input("Enter any digit : >>"))
    print(f'sum of "{digit}" is {sum_of_digit(digit)}')
except ValueError:
    print('Invalid Input')



