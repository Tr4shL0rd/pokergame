import random
from termcolor import colored 
import time
clear = "\n" * 100

def rules():
        print(clear)
        #rules
        print("                                RULES                                                                                       ")
        print("the rules are easy, its basically a round of Rock Paper Scissors                                                            ")
        print("expect, every player will get three randomly drawn 'cards', and start with 120 chips to bet with(one chip is worth 1000 usd)")
        print("so you can end up with two scissord and one rock                                                                            ")
rules()

print()
def bets():
        bets.chips = 120
        bets.yourDebt = 0
        bets.yourBet = input("How many do you want to bet? " )
        bets.yourBet = int(bets.yourBet)
        bets.chips = bets.chips - bets.yourBet
        if bets.yourBet > 120: 
                print("you dont have {} chips".format(bets.yourBet))
                bets()
        elif bets.yourBet < 1:
                print("its not fun unless you bet something.")
                bets()
        print("you have {} chips left".format(bets.chips))
        confirmation = input("you bet {} chips, are you sure? ".format(bets.yourBet)).lower()
        if confirmation == "no":
                bets()
bets()
print(clear)
print()
def game():
        print()
        #stupid shit that has all the cards and bets
        randomCard1 = random.choice(["rock", "paper", "scissors","rock", "scissors", "rock", "paper", "scissors","rock", "scissors", "paper", "paper"])
        randomCard2 = random.choice(["rock", "paper", "scissors","rock", "scissors", "rock", "paper", "scissors","rock", "scissors", "paper", "paper"])
        randomCard3 = random.choice(["rock", "paper", "scissors","rock", "scissors", "rock", "paper", "scissors","rock", "scissors", "paper", "paper"])

        CPUrandomCard2 = random.choice(["rock", "paper", "scissors","rock", "scissors", "rock", "paper", "scissors","rock", "scissors", "paper", "paper"])
        CPUrandomCard3 = random.choice(["rock", "paper", "scissors","rock", "scissors", "rock", "paper", "scissors","rock", "scissors", "paper", "paper"])
        CPUrandomCard1 = random.choice(["rock", "paper", "scissors","rock", "scissors", "rock", "paper", "scissors","rock", "scissors", "paper", "paper"])
        CPUbet = random.randrange(1, 120)

        #some stupid shit that makes the game work somehow
        cpuCardArray = [CPUrandomCard1, CPUrandomCard2, CPUrandomCard3]
        cpuCard = random.choice(cpuCardArray)
        print("your money: {} thousand usd".format(bets.yourBet)) 
        print(colored("let the game begin", "green"))
        print()
        
        yourHand = print ("you got {}, {}, {}".format(randomCard1,randomCard2,randomCard3))
        yourChoices = randomCard1, randomCard2, randomCard3
        yourCard = input("what do you want to draw? ").lower()
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

        elif yourCard == "rock" and cpuCard == "paper":
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("you LOST!", "red"))
                print(colored("you lost {} chips, and you opponent gains {} chips".format(bets.yourBet, CPUbet)), "red")
                bets.chips = bets.chips - bets.yourBet
                print("you have {} chips left".format(bets.chips))
                bets.yourDebt = bets.yourDebt + bets.yourBet * 1000
                bets.yourBet =  120 - bets.yourBet
                print("your owe {} usd".format(bets.yourDebt))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()

        elif yourCard == "rock" and cpuCard == "scissors":
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("you WIN!", "green"))
                print(colored("you gained {} chips, and you opponent lost {} chips".format(bets.yourBet, CPUbet)), "green")
                bets.chips = bets.chips + bets.yourBet
                print("you have {} chips left".format(bets.chips))
                bets.yourBet =  bets.yourBet + CPUbet * 1000
                print("you won {} usd".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()


        elif yourCard == "paper" and cpuCard == "scissors":
                print("you chose {}".format(yourCard))
                print("you opponent chose {}".format(cpuCard))
                print(colored("you LOST!", "red"))
                print(colored("you lost {} chips, and you opponent gains {} chips".format(bets.yourBet, CPUbet)), "red")
                bets.chips = bets.chips - bets.yourBet
                print("you have {} chips left".format(bets.chips))
                bets.yourDebt = bets.yourDebt + bets.yourBet * 1000
                bets.yourBet =  120 - bets.yourBet
                print("your owe {} usd".format(bets.yourDebt))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()

        elif yourCard == "paper" and cpuCard == "rock":
                print("you chose {}".format(yourCard))
                print("you opponent chose {}".format(cpuCard))
                print(colored("you WIN!", "green"))
                print(colored("you gained {} chips, and you opponent lost {} chips".format(bets.yourBet, CPUbet)), "green")
                bets.chips = bets.chips + bets.yourBet
                print("you have {} chips left".format(bets.chips))
                bets.yourBet =  bets.yourBet + CPUbet * 1000
                print("you won {}  usd ".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()

                
        elif yourCard == "scissors" and cpuCard == "rock":
                print("you chose {}".format(yourCard))
                print("your opponent chose {}".format(cpuCard))
                print(colored("you LOST!", "red"))
                print(colored("you lost {} chips, and you opponent gains {} chips".format(bets.yourBet, CPUbet)), "red")
                bets.chips = bets.chips - bets.yourBet
                print("you have {} chips left".format(bets.chips))
                bets.yourDebt = bets.yourDebt + bets.yourBet * 1000
                bets.yourBet =  120 - bets.yourBet
                print("your owe {} usd".format(bets.yourDebt))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()
                        
        elif yourCard == "scissors" and cpuCard == "paper":
                print("you chose {}".format(yourCard))
                print("you opponent chose {}".format(cpuCard))
                print(colored("you WIN!", "green"))
                print(colored("you gained {} chips, and you opponent lost {} chips".format(bets.yourBet, CPUbet)), "green")
                bets.chips = bets.chips + bets.yourBet
                print("you have {} chips left".format(bets.chips))
                bets.yourBet =  120 - bets.yourBet * 1000
                print("you won {}".format(bets.yourBet))
                retry = input("play again? ")
                if retry == "yes":
                        game()
                else:
                        exit()
                       
game()