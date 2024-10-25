


import random
item_list=["rock","paper","scissor"]

user_choice=input("Chose Your Move ( Rock , Paper , Scissor)= ").lower()
com_choice=random.choice(item_list)
print(f"User Choice={user_choice} And Computer Choice={com_choice}")
if user_choice==com_choice:
    print("Match is Tie")
elif user_choice=="rock":
    if com_choice=="paper":
        print("Paper Cover Rock = Computer Wins")
    else:
        print("Rock Smashes Scissor = User Wins")
elif user_choice=="paper":
    if com_choice=="scissor":
        print("Scissor Cut Paper = Computer Wins")
    else:
        print("Paper Cover Rock = User Wins")
elif user_choice=="scissor":
    if com_choice=="rock":
        print("Rock Smashes Scissor = Computer Wins")
    else:
        print("Scissor Cut Paper = User Wins")
        
