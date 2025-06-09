import random
secret_number = random.randint(1,100)
while True:
    user_guess = int(input("Guess a number between 1 and 100:"))
    if user_guess > secret_number:
        print("Too High")
    elif user_guess < secret_number:
        print("Too Low")
    else:
        print("Correct!") 
        break