import random

def rps_rules(user_no, comp_no, comp_input, user_input):
    if user_no == comp_no:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("It is a tie!!")
    elif user_no == 1 and comp_no == 3:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("User Won")
    elif user_no == 1 and comp_no == 2:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("Computer Won")
    elif user_no == 2 and comp_no == 1:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("User Won")
    elif user_no == 2 and comp_no == 3:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("Computer Won")
    elif user_no == 3 and comp_no == 1:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("User Won")
    elif user_no == 3 and comp_no == 2:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("Computer Won")


comp_no = random.randrange(1, 4)
match comp_no:
    case 1:
        comp_input = "Rock"
    case 2:
        comp_input = "Scissor"
    case 3:
        comp_input = "Paper"


print("1. Rock")
print("2. Paper")
print("3. Scissors")
user_no = int(input("Enter your choice: "))

match user_no:
    case 1:
        user_input = "Rock"
    case 2:
        user_input = "Scissor"
    case 3:
        user_input = "Paper"


rps_rules(user_no, comp_no, comp_input, user_input)

