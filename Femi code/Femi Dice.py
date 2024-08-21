#python 3.7.1

print ("\t"*15,"Hello, Welcome to Femi's","\n","\t"*18,"Dice Rolling Game", "\n")
import random

min_v = 1
max_v = 6

#............... func roll
def func_roll():
  ans_val = random.randint(min_v,max_v)
  return ans_val


#ans_val = func_roll()
#print(ans_val)

#............... func roll

#....... Enter no of multi-player

while True:
  inp_no_multi_player = input("Enter d Number of Multiplayer? \n")
  if inp_no_multi_player.isdigit():
    inp_no_multi_player = int(inp_no_multi_player)
    if inp_no_multi_player in range(2,5):
      print("Please wait.. I will create a list for the %d MULTIPLAYERS\n" % inp_no_multi_player)
      break 
    else:
      print("Outside range.. Enter Multiplayers BTW 2..and..4")

  else:
    print("U didn't enter a number. Pls, try again\n")
  


#....... Enter no of multi-player
 
#...........pre allocation ........
player_score_li = [0 for _ in range(inp_no_multi_player)] 
print("\t"*15,player_score_li)


#..........pre allocation ........

#............code for 1 player .....



#............code for 1 player .....

#..... Player line Up 


#..... Player line Up 

#....... max player wins
SCORE_LIMIT = 17
while max(player_score_li) < SCORE_LIMIT:
  
  for player_idx in range(inp_no_multi_player):
    print("Player [%d] is ready to play\n " % player_idx ) 
    #print("Player.. ",player_idx,".. Your total score is.. ",player_score_li[player_idx],".. \n")
    current_score = 0
    
    while True:
      
      inp_roll = input("\t\t\t\t\tDo u want to roll dice?\n\t\t\t\t\tType... y... if yes\n")
      
      if inp_roll.lower() !='y':
        break 
      no_on_die = func_roll()
      if no_on_die == 1:
        #current_score = 0
        break
      else:
        current_score += no_on_die
        print("Player Index = %14d\n" % player_idx )
        print("Number on die = %d\n" % no_on_die)
        print("Current Score is = %d\n" % current_score)
          
     
          
        
    player_score_li[player_idx] = current_score
    print("Your final score is: \t"+  str( player_score_li[player_idx] ) +"\n" )
  

max_score = max(player_score_li)
win_idx = player_score_li.index(max_score)
print("Take a look at the Winning List", "\t"*5,player_score_li)
print("Player..",win_idx,"..WoN..","With a max score of.. ",max_score)
#....... max player wins 
