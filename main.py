#By EvilGen3301
#This code is for beginners only / easy to understand 

import time

def game(): 
    string = "Are you sure u will type this in 15s??"        # < --- Text here is what u will type ingame
    word_count = len(string.split())        
    
    while True:
        print(f'{string}')
        start_time = time.time()                             #  <---|
        player_input = str(input("Enter your text: "))       #      |  this is how code knows how much time u need to finish
        end_time = time.time()                               #  <---|
        
        time_taken = end_time - start_time                   # overall time u needed to finish text
        print(f'Time: {time_taken}')


    

print('            --------TYPEFASTER--------')
print('-' * 50)

game()
