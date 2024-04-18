import tkinter as tk


class PalindromeApp(tk.Tk):
    def __init__(self):
        super().__init__() # still not sure what this is doing here
    
        # add title
        self.title = tk.Label(self, text='\nWelcome to the Palindrome Checker!\n', fg='#074173', bg='#9BB0C1', font=('Ariel', 25))
        self.title.pack()
        
        # add palindrome definition
        self.definition = tk.Label(self, text='\n      Palindromes are words, numbers or phrases that read the same backwards as well as forwards     \n', fg='#074173', bg='#9BB0C1', font=('Ariel', 18))
        self.definition.pack()
        
        # add request for input
        self.input = tk.Label(self, text='\nEnter the word, number or phrase you would like to check (do not use any punctuation) \n', fg='#074173', bg='#9BB0C1', font=('Ariel', 18))
        self.input.pack()
        
        # create input entry box
        self.entry = tk.Entry(self, bg='#51829B', font=('Ariel', 18))
        self.entry.pack(padx=(50,50))
       
       # add result of palindrome checker
        self.result = tk.Label(self, fg='#8B322C', bg='#9BB0C1', font=('Ariel', 18))
        self.result.pack()
        
        # create submit button
        self.btn = tk.Button(self, text='Submit', command=self.submit, font=('Ariel', 18))
        self.btn.pack(pady=(0,50))


    def submit(self):
        self.palindrome = self.entry.get().lower().replace(" ","") 
        self.reverse_palindrome = self.palindrome[::-1]      
        
        if self.palindrome != self.reverse_palindrome:
           self.result['text'] = ('Try again.\n' + self.entry.get() + ' is not a palindrome\n')
        else:
           self.result['text'] = ('Good find!\n' + self.entry.get() + ' is a palindrome\n')



if __name__=='__main__':
    root = PalindromeApp()
    root['bg'] = '#9BB0C1'
    root.mainloop()