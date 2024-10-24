"""Problem Statement:
You want to create a simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

Question:
How can you create a Python program that allows the player to play Rock-Paper-Scissors against the computer?"""

import random

print( "ROCK PAPER SCISSOR GAME! \n"+
      "Game Rules \n"+
      "Rock vs Paper --> Paper wins \n"+
      "Rock vs Scissor --> Rock wins \n"+
      "Paper vs Scissor --> Scissor wins \n")

while True:
  print("Enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissor")

  choice = int(input("Enter the choice:"))

  while choice>3 or choice<1:
    choice= int(input("Enter a valid choice please:"))

    if choice==1:
      choice_name="Rock"
    elif choice==2:
      choice_name="Paper"
    else:
      choice_name=="Scissor"
    
    print ("User choice is:", choice_name)
    print("Now its computers turn!")

    comp_choice= random.randint(1,3)
    while comp_choice ==choice:
      comp_choice=random.randint(1,3)

    if comp_choice==1:
      comp_choice_name ="Rock"
    elif comp_choice==2:
      comp_choice_name="Paper"
    else:
      comp_choice_name="Scissor"

    print("Computer choice is:",comp_choice_name)
    print(choice_name, "VS",comp_choice_name)

    if choice==comp_choice:
      print("Draw",end="")
      result ="Draw"

    if (choice==1 and comp_choice==2):
      print("Paper wins:",end="")
      result ="Paper"

    if (choice==1 and comp_choice==3):
      print("Rock wins:", end="")
      result="Rock"

    elif (choice==3 and comp_choice==1):
      print("Rock wins:",end="")
      result="Rock"

    if(choice==2 and comp_choice==3):
      print("Scissor wins:", end="")
      result="Scissor"
    elif (choice==3 and comp_choice==2):
      print("Scissor wins:",end="")
      result="Scissor"
    
    if result == "Draw":
      print("<==IT is a tie==>")
    if result == choice_name:
      print("<== User wins ==>")

    else:
      print("<== Computer wins ==>")

    answer =input("Do you want to play again? (Y/N):")
    if answer =="N":
      print("Thanks for playing")
      break
    else:
      continue