list1 = [10, 11, 90, 89, 65, 84, 23]

listOdd = []
listEven = []

for num in list1:
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)

print("List Of Even Numbers : ", listEven)
print("List of Odd Numbers :", listOdd)
