
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




game = ['rock','paper','scissors']

comp = random.choice(game)

you =str(input("Enter ( 'rock' , 'paper' or 'scissors'):\t"))

print(f'You chose: \t{you}')

print(f'Computer chose :\t{comp}')

if ( you == 'rock' and comp == 'paper'):
  
    print(f'Computer won this round!! You chose:{rock} \ncomputer chose:\n{paper}')

elif( you == 'paper' and comp == 'scissors'):

    print(f'Computer won this round!!You chose:{paper} \ncomputer chose:\n{scissors}')

elif ( you == 'scissors' and comp == 'rock'):

    print(f'Computer won this round!!You chose:{scissors} \ncomputer chose:\n{rock}')    

elif ( you == 'rock' and comp == 'scissors'):

    print(f'You won this round!!You chose:{rock} \ncomputer chose:\n{scissors}')

elif ( you == 'paper' and comp == 'rock'):

    print(f'You won this round!!You chose:{paper} \ncomputer chose:\n{rock}')

elif ( you == 'scissors' and comp == 'paper'):

    print(f'You won this round!!You chose:{scissors} \ncomputer chose:\n{paper}')

elif ( you == comp):

    if ( you == 'rock'):

        print(f'You chose rock You chose:{rock} \ncomputer chose:\n{rock}')

    elif ( you == 'paper'):

        print(f'You chose paper You chose:{paper} \ncomputer chose:\n{paper}') 

    elif ( you == 'scissors'):

        print(f'You chose scissors You chose:{scissors} \ncomputer chose:\n{scissors}')       

    print("It's a draw.")    