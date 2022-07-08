def sum(a,b,c) :
    return a + b + c

def print_board(x_state, z_state) :
    zero = 'X' if x_state[0] else('O' if z_state[0] else 0)
    one = 'X' if x_state[1] else('O' if z_state[1] else 1)
    two = 'X' if x_state[2] else('O' if z_state[2] else 2)
    three = 'X' if x_state[3] else('O' if z_state[3] else 3)
    four = 'X' if x_state[4] else('O' if z_state[4] else 4)
    five = 'X' if x_state[5] else('O' if z_state[5] else 5)
    six = 'X' if x_state[6] else('O' if z_state[6] else 6)
    seven = 'X' if x_state[7] else('O' if z_state[7] else 7)
    eight = 'X' if x_state[8] else('O' if z_state[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|--- ")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|--- ")
    print(f" {six} | {seven} | {eight} ")

def check_win(x_state, z_state ) :
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    
    for win in wins :
        if( sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3 ) :
            print("X won the match !!")
            print_board(x_state, z_state)
            return 1

        if( sum(z_state[win[0]], z_state[win[1]], z_state[win[2]]) == 3 ) :
            print("O won the match !!")
            print_board(x_state, z_state)
            return 0
        
    return -1

try :
    if __name__ == "__main__" :

        print("Welcome to the Tic-Tac-Toe game !!")
        x_state = [0,0,0,0,0,0,0,0,0]
        z_state = [0,0,0,0,0,0,0,0,0]
        turn = 1 #1 for X and 0 for O
        for i in range(9) :

            print_board(x_state, z_state)
            
            if(turn == 1) :
                print(" X's turn !!")
                value = int(input("Please Enter a value : "))
                while(value > 8 or value < 0 or x_state[value] == 1 or z_state[value] == 1) :
                    value = int(input("Please Enter a new value, as it is already occupied or out of range : "))
                
                x_state[value] = 1
            
            else :
                print(" O's turn !!")
                value = int(input("Please Enter a value : "))
                while(value > 8 or value < 0 or x_state[value] == 1 or z_state[value] == 1) :
                    value = int(input("Please Enter a new value, as it is already occupied or out of range : "))
                
                z_state[value] = 1
            
            
            cwin = check_win(x_state, z_state)
            if(cwin != -1) :
                break
            if(cwin == -1 and i == 8) :
                print("Match Tied !!")
            turn = 1 - turn

except Exception as e :
    print("Please enter a proper integer value :)")