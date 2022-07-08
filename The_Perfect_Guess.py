import random

rand_num = random.randint(1,100)
guess = 0
user = None
while(user != rand_num) :
    user = int(input("Enter your guess :"))
    guess += 1
    if(user == rand_num):
        print("Congratulations !! You guessed it right !")
    else :
        if user > rand_num :
            print("OOPS !! You guessed it wrong ! Please Enter a smaller number.")
        else :
            print("OOPS !! You guessed it wrong ! Please Enter a larger number.")

print(f"You guessed the number in {guess} guesses !!")

with open("hiscore.txt","r") as f :
    hiscore = int(f.read())

if(hiscore > guess) :
    with open("hiscore.txt","w") as f :
        f.write(str(guess))
