import random

choices =['rock','paper','scissors']

while True:
    print("choose your choice")
    print("1.rock")
    print("2.paper")
    print("3.scissors")

    choice = int(input("choose your choice:"))
    if choice < 1 or choice > 3:
      print("invalid choice")
      continue

    user_choice=choices[choice -1]

    print("user choice is :",user_choice)

    print("now its computer's turn")

    computer_choice=random.randint(1,3)

    computer_choice =choices[computer_choice - 1]

    print("computer choice is: ",computer_choice)

    if user_choice == computer_choice:
        print("its a tie")
    elif choice==1 and computer_choice==3:
        print("user wins")
    elif choice==2 and computer_choice==1:
        print("user wins")
    elif choice==3 and computer_choice==2:
        print("user wins")
    else:
        print("computer wins")

    play_again =input("do you want to play again? (y/n):")

    if play_again =="y" or play_again =="Y":
      continue

    elif play_again == "n"or play_again =="N":
      print("thank you for playing")
      break





