# reverse a list

list1 = [10, 20, 30, 40, 50, 60]
list2 = ["Vishal","Shubham","Pradip","Rizwan"]

# using slicing in List

def rev_list(lst):
    return lst[::-1]  #[start:end:step]


def rev_list2(lst):
    list2 = []
    for i in range(1, len(lst) + 1):
        list2.append(lst[-i])
    return list2


print(rev_list(list1))
print(rev_list2(list2))
