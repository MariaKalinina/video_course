while True:
    number = input("Enter number from 0 to 10: ")
    try:
        number = int(number)
        if 0 < number < 10:
            result = number ** 2
            print(result)
            break
        else:
            print("Number must be more then 0 and less then 10")
    except ValueError as v:
        print(v)
