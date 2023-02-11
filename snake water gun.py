#snake water and Gun
import random
name = input("Enter Your Name: ")
print(f"Hey {name} welcome to Snake Water Gun Game")
input("Press any key to start your game")
print('...............Starting................')
game=['S','W','G']
user_point=0
system_point=0
i=0
while(i<10):
    user = input("Enter your choice: ").upper()
    system = random.choice(game)
    if (user == 'S' and system == 'W') or (user == 'G' and system == 'S') or (user == 'W' and system == 'G'):
        print(f"system Choice: {system}")
        user_point+=1
        print("You Won")

    if (user == 'W' and system == 'S') or (user == 'S' and system == 'G') or (user == 'G' and system == 'W'):
        print(f"system Choice: {system}")
        system_point+=1
        print("You Loss")
    if user == system:
        print(f"system Choice: {system}")
        print("Tie")
    else:
        print('Enter the Valid choice')
    i+=1
print(f'(Your score: {user_point})')
print(f'(Your score: {system_point})')
if user_point > system_point:
    print("You Won The Game")
if user_point < system_point:
    print("You Lost The Game")
if user_point == system_point:
    print("The Game is Tie")
