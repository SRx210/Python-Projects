import random

def rps_rules(user_no, comp_no, comp_input, user_input):
    if user_no == comp_no:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("It is a tie!!\n")        #Rock vs Rock = Tie (same inputs for both i.e comp and user results in tie
    elif user_no == 1 and comp_no == 3:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("User Won\n")             #Rock vs Scissor = Rock
    elif user_no == 1 and comp_no == 2:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("Computer Won\n")         #Rock vs Paper = Paper
    elif user_no == 2 and comp_no == 1:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("User Won\n")             #Paper vs Rock = Paper
    elif user_no == 2 and comp_no == 3:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("Computer Won\n")         #Paper vs Scissor = Scissor
    elif user_no == 3 and comp_no == 2:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("User Won\n")             #Scissor vs Paper = Scissor
    elif user_no == 3 and comp_no == 1:
        print(f"User Chose {user_input} and Computer Chose {comp_input}")
        print("Computer Won\n")         #Scissor vs Rock = Rock


while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    user_no = int(input("Enter your choice: "))

    comp_no = random.randrange(1, 4)  # Computer chooses number between 1 to 3
    match comp_no:
        case 1:
            comp_input = "Rock"
        case 2:
            comp_input = "Paper"
        case 3:
            comp_input = "Scissor"

    match user_no:
        case 1:
            user_input = "Rock"
        case 2:
            user_input = "Paper"
        case 3:
            user_input = "Scissor"
        case 4:
            print("Exiting...")
            exit(0)

    rps_rules(user_no, comp_no, comp_input, user_input)
    ch = input("Do you want to continue? (y/n): ")
    if ch == 'n' or ch == 'N':
        print("Exiting...")
        break
