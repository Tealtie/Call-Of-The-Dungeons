import random

def init():
    print("\nWelcome To Call Of The Dungeons!")
    print("ver: 0.0.0.2\n")

def playerInit():
    global playerHealth
    playerHealth = 20
    

def spawnBasicEnemy():
    global enemyHealth
    enemyHealth = random.randint(5,20)

init()