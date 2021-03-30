name = input("Your name: ")
surname = input("Your surname: ")
age = int(input("Your age: "))
body_mass = int(input("Your body mass: "))

if age <= 30 and 50 <= body_mass <= 120:
    print(name, surname, age, "years, body mass = ", body_mass, "- good state of health")
elif 40 <= age < 40 and 50 > body_mass > 120:
    print(name, surname, age, "years, body mass = ", body_mass, "- you should take care of yourself")
elif age > 40 and 50 > body_mass > 120:
    print(name, surname, age, "years, body mass = ", body_mass, "- you should go to the doctor")
elif body_mass >= 300:
    print(name, surname, age, "years, body mass = ", body_mass, "- you need bariatric surgery")
