import random

secret_num = random.randint(1,10)
attempts = 0
max_attempts = 5

while attempts<max_attempts:
    a=input("Enter num:")

    if not a.isdigit():
        print("Invalid input")
        continue
    b = int(a)
    attempts += 1

    if b == secret_num:
        print("You win")
        break
    elif b < secret_num:
        print("Too low")
    else:
        print("Too high")  
    
    print(f"Attempts left:{max_attempts-attempts}")
else:
    print("You lose . The correct num was:",secret_num)