import random
while True:
    item_list=["rock","paper","scissor"]
    user_choice=input("\nEnter your choice(rock,paper or scissor):")
    comp_choice=random.choice(item_list)

    print(f"User choice={user_choice}.\nComputer choice={comp_choice}.")

    if user_choice==comp_choice:
        print("Tie")
    elif user_choice=="rock" and comp_choice=="paper":
        print("Computer won")
    elif user_choice=="rock" and comp_choice=="scissor":
        print("You won")
    elif user_choice=="paper" and comp_choice=="rock":
        print("You won")
    elif user_choice=="paper" and comp_choice=="scissor":
        print("Computer won")
    elif user_choice=="scissor" and comp_choice=="paper":
        print("You won")
    elif user_choice=="scissor" and comp_choice=="rock":
        print("Computer won")

