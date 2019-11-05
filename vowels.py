sentence = input("Enter a Sentence : >>")
string = sentence.lower()
vowels = ['a','e','i','o','u']
count = 0
for char in string:
    if char in vowels:
        count += 1

print(f"Number of Vowels in the Sentence is {count}")
