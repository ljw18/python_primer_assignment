# vowel and consonant counter function

def vowel_counter(name):

    letters_in_name = list(name.replace(" ",""))
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    numbers_and_punc = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "(", ")", "-", "?", ",", ".", "\'", "\"", ":", ":", "_", "=", "+", "/", " "]

    
# count number of vowels
    count =  0
    for i in range(len(letters_in_name)):
        if letters_in_name[i] in vowels:
            count += 1 

# count number of consonants (not vowels and not number or punc)
    count_1 = 0
    for i in range(len(letters_in_name)):
        if letters_in_name[i] not in vowels and letters_in_name[i] not in numbers_and_punc:
            count_1 += 1

# count number of other characters
    count_2 = 0
    for i in range(len(letters_in_name)):
       if letters_in_name[i] in numbers_and_punc:
            count_2 += 1

    print (f"\n{name} contains {count} vowels, {count_1} consonants and {count_2} other characters.\n")
