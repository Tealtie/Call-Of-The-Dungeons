import random
import sys
from time import sleep as wait

def init():
    play = input("Would You Like To Play Call Of The Dungeons? (y/n)\n")
    play = play.lower()
    if play == "y":
        print("Loading...")
    wait(1)
    if play == None or play == "n":
        print("Exiting...")
        exit()
    print("\nWelcome To Call Of The Dungeons!")
    print("ver: 0.0.0.31\n")
    playerInit()
    spawnBasicEnemy()
    global main
    main = True

def playerInit():
    global playerHealth
    playerHealth = 20
    
def spawnBasicEnemy():
    global enemyHealth
    enemyHealth = random.randint(5,20)

def fight():
    global enemyHealth
    damage = random.randint(5,7)
    enemyHealth -= damage
    print(f"\nWell Done!")
    print(f"You Dealt {damage} Damage!")
    print(f"The Enemy Has {enemyHealth} HP Left!\n")

def run():
    print("You Ran Away!")
    exit()

def playerInput():
    print(f"An Enemy Has Spawned With {enemyHealth} HP While You Have {playerHealth} HP!")
    ask = True
    while ask:
        choice = input("What Do You Wish To Do?\n")
        choice =  choice.lower()
        if choice == "fight":
            fight()
            ask = False
        elif choice == "run":
            run()
            ask = False
        else:
            print('\nThat Is Not A Valid Option!')
            print('Try "Fight or "Run"\n')

init()

class mainloop():
    while main:
        playerInput()