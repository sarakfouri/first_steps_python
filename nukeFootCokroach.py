import random
def subfunction():
    userpoints = 0
    tie = 0
    rounds = 0
    check = True
    while check:     
        print("Foot, Nuke or Cockroach? (Quit ends):",end="")
        user = input() 
        if user.lower() != "quit":
           i = random.randint(1, 3)
           if user.lower() == "foot" and i == 3:
                print("You chose: ", user)
                print("Computer chose: Cockroach")
                userpoints = userpoints + 1
                print("You WIN!")
                rounds = rounds + 1
           elif user.lower() == "cockroach" and i == 2:
                print("You chose: ", user)
                print("Computer chose: Nuke")
                userpoints = userpoints + 1
                print("You WIN!")
                rounds = rounds + 1
           elif user.lower() == "nuke" and i == 1:
                print("You chose: ", user)
                print("Computer chose: Foot")
                userpoints = userpoints + 1
                print("You WIN!")
                rounds = rounds + 1
           elif i == 1 and user.lower() == "cockroach":
                print("You chose: ", user)
                print("Computer chose: Foot")
                print("You LOSE!")
                rounds = rounds + 1
           elif i == 2 and user.lower() == "foot":
                print("You chose: ", user)
                print("Computer chose: Nuke")
                print("You LOSE!")
                rounds = rounds + 1
           elif i == 3 and user.lower() == "nuke":
                print("You chose: ", user)
                print("Computer chose: Cockroach ")
                print("You LOSE!")
                rounds = rounds + 1
           elif i == 1 and user.lower() == "foot":
                print("You chose: ", user)
                print("Computer chose: Foot")
                print("It is a tie!")
                tie = tie + 1
                rounds = rounds + 1
           elif i == 2  and user.lower() == "nuke":
                print("You chose: ", user)
                print("Computer chose: Nuke")
                print("Both LOSE!")
                rounds = rounds +1 
           elif i == 3 and user.lower() == "cockroach":
                print("You chose: ", user)
                print("Computer chose: Cockroach")
                print("It is a tie!")
                tie = tie + 1
                rounds = rounds + 1
           else :
                print("Incorrect selection.")
        elif user.lower() == "quit":
            print("You played ", rounds, "rounds, and won ",
            userpoints, " rounds, playing tie in", tie, "rounds.")
            check = False


subfunction()