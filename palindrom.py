def isPalindrome(string):
    string = str(string)
    rev = string[::-1]
    if string == rev:
        return True
    else:
        return False


number = int(input('Enter a Number : >>'))

if isPalindrome(number):
    print(f'Given Number "{number}" is a Palindrome NUmber')
else:
    print(f'Given Number "{number}" not a Palindrome NUmber')

string  = input('Enter a String : >>')

if isPalindrome(string):
    print(f'Given String  "{string}" is a Palindrome String')
else:
    print(f'Given String "{string}" not a Palindrome String')










