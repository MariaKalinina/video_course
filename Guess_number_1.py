import random


number = random.randint(1, 100)
# print(number)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input("There are 3 levels \n"
                  "Level 1 - 10 attempts\n"
                  "Level 2 - 5 attempts\n"
                  "Level 3 - 3 attempts\n"
                  "Choose the level: "))
max_count = levels[level]
attempt_left = max_count

user_count = int(input("How many users are going to play?"))
users = []
for user in range(user_count):
    user_name = input(f"Enter user's name {user}: ")
    users.append(user_name)
    print(users)
is_winner = False
winner_name = None
while not is_winner:
    count += 1
    attempt_left -= 1
    if count > max_count:
        print("All users lost :-(")
        break
    print(f"Attempt N {count}")
    for user in users:
        print(f"User {user} tries to guess the number")
        user_num = input("Enter number: ")
        try:
            user_num = int(user_num)
        except ValueError as k:
            print(k)
        if user_num > number:
            print("Your number is bigger than hidden number! Try again.")
            print(f"Attempts left {attempt_left}")
        elif user_num < number:
            print("Your number is smaller than hidden number! Try again.")
            print(f"Attempts left {attempt_left}")
        elif user_num == number:
            is_winner = True
            winner_name = user
            break
else:
    print(f"The winner is {winner_name}!!!")
