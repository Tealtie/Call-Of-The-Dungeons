import random

def init():
    print("\nWelcome To Call Of The Dungeons!")
    print("ver: 0.0.0.2\n")
    playerInit()
    spawnBasicEnemy()

def playerInit():
    global playerHealth
    playerHealth = 20
    
def spawnBasicEnemy():
    global enemyHealth
    enemyHealth = random.randint(5,20)

def fight():
    global enemyHealth
    enemyHealth -= random.randint(5,7)

def playerInput():
    print(f"An Enemy Has Spawned With {enemyHealth} HP While You Have {playerHealth} HP")
    choice = input("What Do You Wish To Do?\n")

init()
playerInput()