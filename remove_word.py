sentence  = input("Enter a sentence :>> ")
word = input('enter a word to delete from string :>> ')
#Method : 1
print(f'sentence before Deleting The "{word}" :>> ',sentence)
new_sentence = sentence.replace(word,'')
print(f'sentence After Deleting The "{word}" :>> ',new_sentence)

#Method : 2
def remove_word(sentence,word):
    lst = sentence.split(' ')
    new_sentence = ''
    for i in lst:
        if i == word:
            lst.remove(word)
        else:
            new_sentence += i + ' '

    return new_sentence

print(f'Method : 2 | sentence After Deleting The "{word}" :>> ',remove_word(sentence,word))


