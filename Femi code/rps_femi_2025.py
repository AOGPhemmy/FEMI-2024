# type here
# prompt user to make guess...comp makes choice after...validate user input...run the code once.
# print guess and  computer choice, use EMOJIS...test code....try using a while loop....

import random
ph_dict = {'r':'🪨','p':'📃','s':'✂️'
}
ct = 0

print('-'*40)
print('\t','Author: Adetimehin Olufemi George')
print('\t'*2,'Rock....Paper....Scissors')
print('-'*40)
print()
print('\t'*3,'-'*11)
print('\t'*3,'Game Begins')
running = True

while running:
    print()
    player = None
    comp_choi = random.choice(list(ph_dict.keys()) )
    guess = input('Select any option r || p || s >>>\n').lower()
    ct += 1
    while guess not in ph_dict:
        guess = input('Try again....wrong input >>>\n').lower()

    print(f'player....{ph_dict.get(guess)}')
    print(f'Computer....{ph_dict.get(comp_choi)}')

    if guess == comp_choi:
        print('tie')
    else:
        print('You win')
        running = False

print(f'HURRAY....You won after...{ct} attempt(s)')
print()
print('\t'*3,'Game Over')
print('\t'*3,'-'*9)
