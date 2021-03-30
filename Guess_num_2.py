from random import randint


while True:
    leave_game = input("To exit press 'Q'")
    leave_game = leave_game.upper
    if leave_game == "Q":
        break
    else:
        print("Pick a number from 1 to 100 and computer will guess it")
        start = input("If ready press Enter: ")

