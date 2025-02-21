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
    global playerHealth, playerDefense
    playerHealth = 20
    playerDefense = 2

def spawnBasicEnemy():
    global enemyHealth, enemyAttack, newEnemy
    enemyHealth = random.randint(5, 20)
    enemyAttack = random.randint(2, 5)
    newEnemy = True  # Flag that a new enemy has been spawned

def fight():
    global enemyHealth, playerHealth
    damage = random.randint(5, 7)
    enemyHealth -= damage
    print(f"\nWell Done!")
    print(f"You Dealt {damage} Damage!")
    print(f"The Enemy Has {enemyHealth} HP Left!\n")
    
    if enemyHealth > 0:
        enemy_damage = max(0, enemyAttack - playerDefense)
        playerHealth -= enemy_damage
        print(f"Enemy strikes back for {enemy_damage} damage!")
        print(f"You have {playerHealth} HP left!\n")
        if playerHealth <= 0:
            print("Game Over! You have been defeated!")
            exit()

def run():
    escape_chance = random.random()
    if escape_chance > 0.3:
        print("You Successfully Ran Away!")
        spawnBasicEnemy()  # Spawn new enemy instead of exiting
    else:
        print("Failed to escape!")
        global playerHealth
        playerHealth -= enemyAttack
        print(f"Enemy hits you for {enemyAttack} damage!")
        if playerHealth <= 0:
            print("Game Over! You have been defeated!")
            exit()

def playerInput():
    global newEnemy  # Declare global to access newEnemy
    if enemyHealth <= 0:
        print("Enemy defeated!")
        spawnBasicEnemy()
        return
    
    if playerHealth <= 0:
        print("Game Over! You have been defeated!")
        exit()
        
    # Print enemy spawn message only once when a new enemy appears
    if newEnemy:
        print(f"An Enemy Has Spawned With {enemyHealth} HP While You Have {playerHealth} HP!")
        newEnemy = False  # Reset flag after printing message
    
    ask = True
    while ask:
        if os.environ.get('GITHUB_ACTIONS') == 'true':
            choice = "fight"
        else:
            choice = input("What Do You Wish To Do?\n")
        
        choice = choice.lower()
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
while True:
    if playerHealth <= 0:
        print("Game Over! You have been defeated!")
        exit()
    playerInput()