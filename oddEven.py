def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def getOnlyEvens(lst):
    even_lst = []
    for n in lst:
        if isEven(n):
            even_lst.append(n)
    return even_lst


def getOnlyOdds(lst):
    odd_lst = []
    for n in lst:
        if not isEven(n):
            odd_lst.append(n)
    return odd_lst

lst = range(1,100)

print(getOnlyEvens(lst))
print(getOnlyOdds(lst))