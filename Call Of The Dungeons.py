import random
import sys
from time import sleep as wait
import os

def init():
    play = "y"  # Automatically set to 'y' for testing
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        play = "y"  # Automatically proceed with 'yes' on GitHub Actions
    else:
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
    enemyHealth = random.randint(5, 20)

def fight():
    global enemyHealth
    damage = random.randint(5, 7)
    enemyHealth -= damage
    print(f"\nWell Done!")
    print(f"You Dealt {damage} Damage!")
    print(f"The Enemy Has {enemyHealth} HP Left!\n")

def run():
    print("You Ran Away!")
    exit()

def playerInput():
    if enemyHealth <= 0:
        print("You Won!")
        exit()
    print(f"An Enemy Has Spawned With {enemyHealth} HP While You Have {playerHealth} HP!")
    ask = True
    while ask:
        if os.environ.get('GITHUB_ACTIONS') == 'true':
            choice = "fight"  # Default action for non-interactive mode (GitHub Actions)
        else:
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
            print('Try "Fight" or "Run"\n')

init()

class mainloop():
    while main:
        playerInput()