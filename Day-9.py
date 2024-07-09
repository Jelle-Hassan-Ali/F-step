# weight converter

weight = input(f"weight: ")

unit = input(f"(L)bs or (K)g ")


weight_lbs = int(weight)*2.20462
weight_kg = int(weight)*0.45

if unit == "L":
    print("You are: ", weight_lbs)
    
elif unit == "K":
    print("You are: ", weight_kg)
    
else:
    print("Invalid input")        
    

weight = int(input('weight: ')) 

unit = (input('(L)bs or (K)g '))  

if unit.upper() == "L":
    converted = weight *0.45
    print(f'You are {converted} kg')
    
elif unit.upper() == "K":
    converted = weight /0.45
    print(f'You are {converted} pounds')
    
else:
    print('Your input is invalid or out of range')       
    

 # while loop
x = 1
 
while x <= 12 :
     print(x)
     x = x + 1
 

num = 16
while num > 4:
    print(num ) 
    num = num - 2
    
print('Done ✔')    



# Game

Secrete_num = 6
Guess_count = 0
Guess_limit = 4

while Guess_count < Guess_limit:
    guess = int(input('Guess: '))
    Guess_count += 1
        
    if guess == Secrete_num:
        print('You Won!')
        break
        
else:
    print('Sorry You Failed try again later')            
    



