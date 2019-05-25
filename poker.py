import random
from termcolor import colored 
import time
clear = "\n" * 100
def rules():
        print(clear)
        #rules
        print("                                RULES                           ")
        print("the rules are easy, its basicly a round of Rock Paper Scissors")
        print("expect, every player will get three randomly drawn 'cards', and start with 120 chips to bet with(one chip is worth 1000 usd)")
        print("so you can end up with two scissord and one rock")
        print("and since the maker of this game is a bad programmer, the game only has one round")
rules()

print()
def bets():
        bets.yourBet = input("How many do you want to bet? " )
        confirmation = input("you bet {} chips, are you sure? ".format(bets.yourBet))
        bets.yourBet = int(bets.yourBet)
        if confirmation == "no":
                bets()

bets()
print(clear)

def game():
        print()
        #stupid shit that has all the cards and bets
        randomCard1 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
        randomCard2 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
        randomCard3 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])

        CPUrandomCard2 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
        CPUrandomCard3 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
        CPUrandomCard1 = random.choice(["Rock", "Paper", "Scissors","Rock", "Scissors", "Rock", "Paper", "Scissors","Rock", "Scissors" ])
        CPUbet = random.randrange(1, 120)

        #some stupid shit that makes the game work somehow
        cpuCardArray = [CPUrandomCard1, CPUrandomCard2, CPUrandomCard3]
        cpuCard = random.choice(cpuCardArray)

        print(colored("let the game begin", "green"))
        print()
        
        yourHand = print ("you got {}, {}, {}".format(randomCard1,randomCard2,randomCard3))
        yourChoices = [randomCard1, randomCard2, randomCard3]
        yourCard = input("what do you want to draw? ")
        print("we will draw on 3")
        print()
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3!")
        print(colored("SHOW YOUR CARDS!", "red"))
        #some very stupid if statments that hit two cards very hard againts each other and then somehow figures out what the answer will be 

        if yourCard == cpuCard:
                print("both you and your opponent chose the same card")
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("DRAW!", "yellow"))
                print("no one won any chips")
                retry = input("play again? ")
                if retry == "yes":
                        game()
                        
                else:
                        exit()

        elif yourCard == "Rock" and cpuCard == "Paper":
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("you LOST!", "red"))
                print("you lost {} chips, and you opponent gains {} chips".format(bets.yourBet, CPUbet))
                bets.yourBet =  120 - bets.yourBet
                print("your owe {} thousand usd".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()

        elif yourCard == "Rock" and cpuCard == "Scissors":
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("you WIN!", "green"))
                print("you gained {} chips, and you opponent lost {} chips".format(bets.yourBet, CPUbet))
                bets.yourBet =  bets.yourBet + CPUbet
                print("you won {} thousand usd".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()


        elif yourCard == "Paper" and cpuCard == "Scissors":
                print("you chose {}".format(yourCard))
                print("you opponent chose {}".format(cpuCard))
                print(colored("you LOST!", "red"))
                print("you lost {} chips, and you opponent gains {} chips".format(bets.yourBet, CPUbet))
                bets.yourBet =  120 - bets.yourBet
                print("you owe {} thousand usd".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()

        elif yourCard == "Paper" and cpuCard == "Rock":
                print("you chose {}".format(yourCard))
                print("you opponent chose {}".format(cpuCard))
                print(colored("you WIN!", "green"))
                print("you gained {} chips, and you opponent lost {} chips".format(bets.yourBet, CPUbet))
                bets.yourBet =  bets.yourBet + CPUbet
                print("you won {} thousand usd ".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()

                
        elif yourCard == "Scissor" and cpuCard == "Rock":
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("you LOST!", "red"))
                print("you lost {} chips, and you opponent gains {} chips".format(bets.yourBet, CPUbet))
                bets.yourBet =  120 - bets.yourBet
                print("you owe {} thousand usd".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()
                        
        elif yourCard == "Scissors" and cpuCard == "paper":
                print("you chose {}".format(yourCard))
                print("you opponent chose {}".format(cpuCard))
                print(colored("you WIN!", "green"))
                print("you gained {} chips, and you opponent lost {} chips".format(bets.yourBet, CPUbet))
                bets.yourBet =  120 - bets.yourBet
                print("you won {}".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()
                       
game()