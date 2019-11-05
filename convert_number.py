num = 24

# convert decimal to binary using recursion
def decToBin(n):
    if n > 0:
        return decToBin(n//2) + str(n%2)
    else:
        return ''

# convert decimal to binary using predefine function bin()
def decToBin2(n):
    return bin(n)[2:]

# convert decimal to octal using predefine function bin()

def decToOct(n):
    return oct(n)[2:]


# convert decimal to hexadecimal using predefine function bin()

def decToHex(n):
    return hex(n)[2:]


print(decToHex(15))


