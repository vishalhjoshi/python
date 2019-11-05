#Given Number is armstrong or not
n = input("Enter Number : >> ")

def checkArmstrong(n):
    number = str(n)
    result = number
    sum  = 0
    for i in number:
        sum += int(i) ** len(number)

    if result == str(sum):
        return True
    else:
        return False

for i in range(1700):
    if checkArmstrong(i):
        print(i)




