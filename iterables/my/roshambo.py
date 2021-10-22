import random

victory_dict={
    ("Rock","Rock"):0,
    ("Rock","Paper"):1,
    ("Rock", "Scissors"):-1,
    ("Scissors","Rock"):1,
    ("Scissors","Paper"):-1,
    ("Scissors","Scissors"):0,
    ("Paper","Paper"):0,
    ("Paper","Rock"):-1,
    ("Paper","Scissors"):1,
}


def main():
    roshambo = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(roshambo)

    num = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    num = int(num) - 1
    user_choice = roshambo[num]

    print("Computer:", computer_choice)
    print("User:", user_choice)
    outcome = victory_dict [ (computer_choice, user_choice)] 
    message_dict = {0:"Вы сыграли вничью",1:"вы выиграли",
                   -1:"вы проиграли"}    
    print(message_dict[outcome])
main()