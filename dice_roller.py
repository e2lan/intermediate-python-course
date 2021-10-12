import numpy as np


def main():
   
    dice_rolls = 2
    dice_sum = 0
    n_games=0
    game = int(input ('wich game do you want to play \n1) get the sum of 12 with 2 dices \n2) guest the sum of the dices\n'))
    
    if game==1:

        while (dice_sum!=12):
            dice_sum=0
            for i in range(0,dice_rolls):
                
                roll = np.random.randint(1,7)
                dice_sum += roll
                if roll == 1:
                    print(f'You rolled a {roll}! Critical Fail')
                elif roll == 6:
                    print(f'You rolled a {roll}! Critical Success!')
                else:
                    print(f'You rolled a {roll}')
            
            print(f'You have rolled a total of {dice_sum}')
            n_games+=1
           
    
    elif game==2:
        
        guestnum=int(input('what number do you want to guest from 2 to 12'))
        while (guestnum <2 or guestnum>12):
            guestnum=int(input('insert a right number from 2 to 12'))
        while (dice_sum!=guestnum):
            dice_sum=0
            for i in range(0,dice_rolls):
                roll = np.random.randint(1,7)
                dice_sum += roll
            print(f'You have rolled a total of {dice_sum}')
            n_games+=1
            
    print(f'you win! number of tryes is equal to {n_games}')       
   
        
        
        

if __name__== "__main__":
    main()