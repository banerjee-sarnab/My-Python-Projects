from operator import truediv
import random


def game_win(a,b) :
    if(a == b) :
        res = None
    elif(a == 'r') :
        if(b == 'p') : res = True
        elif(b == 's') : res = False
    elif a == 'p' :
        if(b == 'r') : res = False
        elif(b == 's') : res = True 
    elif a == 's' :
        if(b == 'p') : res = False
        elif(b == 'r') : res = True 
    return res

print("I have given my turn :)")
a = random.randint(1,3)
if a == 1   : p1 = 'r'
elif a == 2 : p1 = 'p'
elif a == 3 : p1 = 's'

p2 = input("Now your's turn : Rock(r) , paper(p) or scissor(s) : ")
print(f"Computer's Choice : {p1}")
print(f"Your's Choice : {p2}")
result = game_win(p1,p2)
if(result == None) : print("Shit !!, Its a TIE ! :|")
elif result == True : print("Wow !!, You Won :)")
elif result == False : print("OOPs !!, You Lose :(")
