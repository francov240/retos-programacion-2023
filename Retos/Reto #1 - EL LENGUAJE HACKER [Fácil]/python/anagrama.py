'''
Escribe una funcion que reciba dos palabras (String) y que retorne 
verdadero o falso (Bool) segun sea o no anagramas.
    - Un anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan. 
    - Dos palabras exactamente iguales no son anagramas. 
'''

def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        print("They are the same word")
        return False
    if(sum_letters(word1) == sum_letters(word2)):
        print("It's an anagram")
        return True
    else:
        print("It's not an anagram")
        return False


def sum_letters(word):
    word = word.lower()
    adder = 0
    for i in range(len(word)):
        adder = adder + ord(word[i])
        #print(ord(word[i]))
    #print(adder)

is_anagram("amor", "aMOr")

sum_letters("Manolo")
