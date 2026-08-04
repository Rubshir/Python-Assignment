import random as ran

print("Select a Level using nummber");
print("Easy : 0 ,Medium : 1,Hard : 2");

a = int(input("Select the level : "));


if(a == 0):
    secret_number = ran.randint(0,100)
    while True:
        guess_number = int(input("Enter the guess number between 1 t0 100 : "));

        if(guess_number > secret_number):
            print("Try a less number ");
        elif guess_number < secret_number:
            print("Try a larger number.")
        else :
            print("Congratulations! You guessed the correct number.")    

if(a == 1):
    secret_number = ran.randint(0,1000)
    while True:
        guess_number = int(input("Enter the guess number between 1 t0 1000 : "));

        if(guess_number > secret_number):
            print("Try a less number ");
        elif guess_number < secret_number:
            print("Try a larger number.")
        else :
            print("Congratulations! You guessed the correct number.") 

if(a == 2):
    secret_number = ran.randint(0,10000)
    while True:
        guess_number = int(input("Enter the guess number between 1 t0 10000 : "));

        if(guess_number > secret_number):
            print("Try a less number ");
        elif guess_number < secret_number:
            print("Try a larger number.")
        else :
            print("Congratulations! You guessed the correct number.") 
        




        