import random
print("Hello! there Welcome")
while True:
    random_number = random.randint(1, 6)
    initial = input("Roll the dice? Y/N:").lower()
    if initial == "y":
        print(random_number)
    elif initial == "n":
        print("you press no")
        break
    else:
        print("Invalid command")
