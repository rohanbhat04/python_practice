import random

def roll_dice():
    list_num = []
    num = random.randint(1,6)
    list_num.append(num)
    num = random.randint(1,6)
    list_num.append(num)
    return list_num


while True:
    choice = input("Roll a dice ? (Y/N) : ")
    if(choice == "Y" or choice == "y"):
        num_on_dice = roll_dice()
        print(num_on_dice)
    elif(choice == "N" or choice == "n"):
        print("Thank You for playing with me :)")
        quit()
    else:
        print("Please enter valid choice")
