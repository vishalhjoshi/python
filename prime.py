# check prime number from given list (all Number)

list1 = [1, 3, 5, 6, 7, 11, 12, 13, 14, 15, 17, 18, 19, 23, 25, 29, 30, 31, 36]

newList = []

for num in list1:
    if num >= 2:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            newList.append(num)

print(newList)




