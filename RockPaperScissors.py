#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Rock, Scissors and Paper 

#*Player one picks a symbol/
#player 2 picks a symbol
#or computer picks a symbol

#Rock beats scissors
#scissors beat paper
#paper beats rock.

#output:
#draw
#player 1 won
#player 2 won

#also make the player play against the computer.

#Ask the players for input
import random

game =  ['rock', 'paper', 'scissors']
comp = random.choice(game)

player1 = input("Player 1: Please Choose (Rock, Paper, or Scissors) ")
print("Choose for player2 or Press Enter to play against the computer(Player2).")
player2 = input("Player 2: Please Choose (Rock, Paper, or Scissors) ")


if player2 == '':
    player2 = comp
    print(comp)
    if player1=="rock" and player2=="rock":
        print('Draw')
        print('Play Again')
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 Won!")
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 Won!")
    elif player2 == "rock" and player1 == "scissors":
        print("Player 2 Won!")
    elif player2 == "rock" and player1 == "paper":
        print("Player 1 Won!")
    elif player1=="scissors" and player2=="scissors":
        print('Draw')
        print('Play Again')
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 Won!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 Won!")
    elif player2 == "scissors" and player1 == "rock":
        print("Player 1 Won!")
    elif player2 == "scissors" and player1 == "paper":
        print("Player 2 Won!")
    elif player1=="paper" and player2=="paper":
        print('Draw')
        print('Play Again')
    elif player1 == "paper" and player2 == "rock":
        print("Player 2 Won!")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 Won!")
    elif player2 == "paper" and player1 == "rock":
        print("Player 1 Won!")
    elif player2 == "paper" and player1 == "scissors":
        print("Player 1 Won!")
    else:
        print('You did something wrong. Please choose amongst "Rock, paper or Scissors".')
elif player1=="rock" and player2=="rock":
    print('Draw')
    print('Play Again')
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 Won!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 Won!")
elif player2 == "rock" and player1 == "scissors":
    print("Player 2 Won!")
elif player2 == "rock" and player1 == "paper":
    print("Player 1 Won!")
elif player1=="scissors" and player2=="scissors":
    print('Draw')
    print('Play Again')
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 Won!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 Won!") 
elif player2 == "scissors" and player1 == "rock":
    print("Player 1 Won!")
elif player2 == "scissors" and player1 == "paper":
    print("Player 2 Won!")
elif player1=="paper" and player2=="paper":
    print('Draw')
    print('Play Again')
elif player1 == "paper" and player2 == "rock":
    print("Player 2 Won!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 Won!")
elif player2 == "paper" and player1 == "rock":
    print("Player 1 Won!")
elif player2 == "paper" and player1 == "scissors":
    print("Player 1 Won!")
else:
    print("Be nice and play by the rules")


# In[ ]:





# In[ ]:




