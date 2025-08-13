# import random
# print("Hello! there Welcome")
# while True:
#     random_number = random.randint(1, 6)
#     initial = input("Roll the dice? Y/N:").lower()
#     if initial == "y":
#         print(random_number)
#     elif initial == "n":
#         print("you press no")
#         break
#     else:
#         print("Invalid command")
import random
while True:
    test = input("Hello Everyone, do you want to roll the dice? Y/N").lower()
    if test == "y":
        print(
            f"Your random number is ({random.randint(1, 6)}, {random.randint(1, 6)})")
    elif test == "n":
        print("you choose not to roll")
        break
    else:
        print("Invalid input, Please enter Y or N")
