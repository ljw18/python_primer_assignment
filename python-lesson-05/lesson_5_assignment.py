# Palindrome Checker

print ("\nWelcome to the Palindrome Checker!\n")

while True: # this will loop the checker back to the start after each result
    
    print ("Palindromes are words, numbers or phrases that read the same backwards as well as forwards eg. dad, 123321, race car\n")
    
    palindrome = input("Enter the word, number or phrase you would like to check (do not use any punctuation): ").upper()
    

    letters_in_palindrome = list(palindrome.replace(" ",""))
    palindrome_no_spaces = "".join(letters_in_palindrome)
    letters_in_palindrome.reverse()
    reverse_palindrome = "".join(letters_in_palindrome)
    is_not_palindrome = (palindrome_no_spaces != reverse_palindrome)

    print(f"\n{palindrome_no_spaces} backwards is {reverse_palindrome}\n")



    if is_not_palindrome is True:
        print (f"\033[1;31m{palindrome} is not a palindrome.\033[0m Try checking another word, number or phrase.\n\n")
    else:
        print (f"\033[1;32mGood find! {palindrome} is a palindrome.\033[0m\n\n")
        
    
