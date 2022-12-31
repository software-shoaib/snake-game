
import random
from secrets import choice


def swg (you, mine):
   
    if (you==mine):
        return None
    if (you=='s' and mine=='g'):
        return True
    elif (you=='w' and mine=='s'):
        return True
    elif(you=='g' and mine=='w'):
        return True 
    else:
        return False

'''
choice= ('s', 'w', 'g')
comp= random.randint(0,2)
comp= comp[]
'''

you = input('PLAYER-2 choose either s, w , or g: ')
mine = input(' PLAYER-1 CHOOSE EITHER s, w or g: ')


win = swg(you, mine)
print(f"Player-1 Chose '{mine}' and the PLAYER-2 chose '{you}' ")

if win is None:
    
    print("Match Drawn")

if win is True:
    
    print("PLAYER-1 Won")
if win is False:
   print("PLAYER-2 won")

