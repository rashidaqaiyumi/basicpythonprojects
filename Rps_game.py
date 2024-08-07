import random 
#defining two variabls 
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
#making dictionary
youDict = {"R": 1, "P": -1, "S": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "scissors"}

you = youDict[youstr]

#If and else statements 
if(computer == you):
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you win!")
    else:
        print("invalid")


