# Palindrome Checker

print ("\nPalindromes are words, numbers or phrases that read the same backwards as well as forwards eg. dad, 123321, race car.")
print ("You can use this tool to check if a word, number or phrase is a palindrome.\n")


palindrome = input("Enter the word, number or phrase you would like to check (do not use any punctuation): ").upper()
letters_in_palindrome = list(palindrome.replace(" ",""))
palindrome_no_spaces = "".join(letters_in_palindrome)

letters_in_palindrome.reverse()
reverse_palindrome = "".join(letters_in_palindrome)

print(f"{palindrome_no_spaces} backwards is {reverse_palindrome}\n")

if palindrome_no_spaces == reverse_palindrome:
    print (f"{palindrome} \033[1;32mis\033[0m a palindrome.")

if palindrome_no_spaces != reverse_palindrome:
    print (f"{palindrome} \033[1;31mis not\033[0m a palindrome.\n")



