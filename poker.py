import random
from termcolor import colored 
import time

#rules
print("the rules are easy, its basicly a game of Rock Paper Scissors")
print("expect, you will get thee randomly drawn 'cards'")
print("so you can end up with 2 scissord and one rock")

print()
def bets():
    bet = input("How many do you want to bet? " )
    confirmation = input("you bet %s chips, are you sure? " % bet)
    if confirmation == "no":
        bets()

bets()


#cards = (["Rock", "Paper", "Scissors"])
print()

randomCard1 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
randomCard2 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
randomCard3 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])

CPUrandomCard2 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
CPUrandomCard3 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
CPUrandomCard1 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])


cpuCardArray = [CPUrandomCard1, CPUrandomCard2, CPUrandomCard3]
cpuCard = random.choice(cpuCardArray)
print(cpuCard)
print(colored("let the game begin", "green"))
print()
#cpuSingleCard =  
yourHand = print ("you got {}, {}, {}".format(randomCard1,randomCard2,randomCard3))
yourChoices = [randomCard1, randomCard2 ,randomCard3]
yourCard = input("what do you want to draw? ")
print(yourChoices)
print(yourCard)
#if yourChoices != yourCard:
#        print("thats not a valid card!")
#        exit()
#time.sleep(100)
print("we will draw on 3")
print()
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print("3!")
if yourCard == cpuCard:
        print("DRAW!")
        print("your opponent drew {}".format(CPUrandomCard1))

if yourCard == cpuCard:
        print("both you and your opponent chose the same card")
        print("you chose {}".format(yourCard))
        print("your opponent chose {}".format(cpuCard))
        print(colored("DRAW!", "yellow"))
        exit()
elif yourCard == "Rock" and cpuCard == "Paper":
        print("you chose {}".format(yourCard))
        print("your opponent chose {}".format(cpuCard))
        print(colored("you LOST!", "red"))
        exit()
elif yourCard == "Rock" and cpuCard == "Scissors":
        print("you chose {}".format(yourCard))
        print("your opponent chose {}".format(cpuCard))
        print(colored("you WIN!", "green"))
        exit()
elif yourCard == "Paper" and cpuCard == "Rock":
        print("you chose {}".format(yourCard))
        print("you opponent chose {}".format(cpuCard))
        print(colored("you WIN!", "green"))
        exit()
elif yourCard == "Paper" and cpuCard == "Scissors":
        print("you chose {}".format(yourCard))
        print("you opponent chose {}".format(cpuCard))
        print(colored("you LOST!", "red"))
        exit()
elif yourCard == "Scissors" and cpuCard == "paper":
        print("you chose {}".format(yourCard))
        print("you opponent chose {}".format(cpuCard))
        print(colored("you WIN!", "green"))
elif yourCard == "Scissor" and cpuCard == "Rock":
        print("you chose {}".format(yourCard))
        print("your opponent chose {}".format(cpuCard))
        print(colored("you LOST!", "red"))
        exit()

        

