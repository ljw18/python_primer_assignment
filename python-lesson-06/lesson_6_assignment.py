# Who knows me best

print('Who Knows Me Best?\nIf you can get these questions right then you know me pretty well!\n')

leanne = {
    'favourite colour': 'yellow', 
    'favourite holiday destination': 'Mexico',
    'favourite food': 'icecream',
    'favourite season': 'Autumn'
    }

fav_colour = input ('What is my favourite colour? ')

if fav_colour.lower() == leanne['favourite colour']:
    print (f'\033[0;34mThat is CORRECT! My favourite colour is {leanne['favourite colour']}.\033[0m\n')
else:
    print(f'That is incorrect. My favourite colour is {leanne['favourite colour']}.\n')     

  
fav_holiday_dest = input ('What is my favourite holiday destination? ')
if fav_holiday_dest.title() == leanne['favourite holiday destination']:
    print (f'\033[0;34mThat is CORRECT! My favourite holiday destination is {leanne['favourite holiday destination']}.\033[0m\n')
else:
    print(f'That is incorrect. My favourite holiday destination is {leanne['favourite holiday destination']}.\n')     


fav_food = input ('What is my favourite food? ')

# change fav food to lasagne
leanne['favourite food'] = 'lasagne'  

if fav_food.lower() == leanne['favourite food']:
    print (f'\033[0;34mThat is CORRECT! My favourite food is {leanne['favourite food']}.\033[0m\n')
else:
    print(f'That is incorrect. My favourite food is {leanne['favourite food']}.\n')     

# add shoe size
leanne['shoe size']='9'
shoe_size = input ('What is my shoe size? ')
if shoe_size == leanne['shoe size']:
    print (f'\033[0;34mThat is CORRECT! My shoe size is {leanne['shoe size']}.\033[0m\n')
else:
    print(f'That is incorrect. My shoe size is {leanne['shoe size']}.\n')  

# remove fav season 
leanne.pop('favourite season')

# summary of answers
print (f'\033[0;32mSo how well do you know me?\033[0m See below to find out some extra things about me.\n')


leanne_extras = {'hair colour': 'black', 'height': '165cms', 'eye colour': 'brown'}
leanne.update(leanne_extras)

for key, value in leanne.items():
    
    print (f'\033[1mMy {key} is {value}\033[0m\n')

