# Palindrome Checker function

def palindrome_check(entry_text):
       
    palindrome = entry_text.lower().replace(" ", "")
    reverse_palindrome = palindrome[::-1]
        
    return palindrome == reverse_palindrome
       
        

