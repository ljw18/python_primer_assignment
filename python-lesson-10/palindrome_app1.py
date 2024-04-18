import tkinter as tk
from palindrome_checker import palindrome_check 


class PalindromeApp(tk.Tk):
    def __init__(self):
        super().__init__() # still not sure what this is doing here
    
        # add title
        self.title = tk.Label(self, text='\nWelcome to the Palindrome Checker!\n', fg='#074173', bg='#9BB0C1', font=('Arial', 25))
        self.title.pack()
        
        # add palindrome definition
        self.definition = tk.Label(self, text='\n      Palindromes are words, numbers or phrases that read the same backwards as well as forwards     \n', fg='#074173', bg='#9BB0C1', font=('Arial', 18))
        self.definition.pack()
        
        # add request for input
        self.input = tk.Label(self, text='\nEnter the word, number or phrase you would like to check (do not use any punctuation) \n', fg='#074173', bg='#9BB0C1', font=('Arial', 18))
        self.input.pack()
        
        # create input entry box
        self.entry = tk.Entry(self, bg='#51829B', font=('Arial', 18))
        self.entry.pack(padx=(50,50))
       
       # add result of palindrome checker
        self.result = tk.Label(self, fg='#8B322C', bg='#9BB0C1', font=('Arial', 18))
        self.result.pack()
        
        # create submit button
        self.btn = tk.Button(self, text='Submit', command=self.submit, font=('Arial', 18))
        self.btn.pack(pady=(0,50))
    
    # create function for when you hit submit button
    def submit(self): 
        entry_text = self.entry.get()
        is_palindrome = palindrome_check(entry_text) 
        
        # if is_palindrome is true then.. else..
        if is_palindrome: 
            self.result['text'] = ('\nGreat work!\n ' + entry_text + ' is a palindrome\n')
        else:
            self.result['text'] = ('\nTry again!\n ' + entry_text + ' is not a palindrome\n')


        
if __name__=='__main__':
    root = PalindromeApp()
    root['bg'] = '#9BB0C1'
    root.mainloop()