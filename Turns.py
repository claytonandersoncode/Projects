import random
import time
from random import randint

"""A turn based program where players fight a 
simple computer in a gladiator style game"""

def main():
    try:
        monsters = ['Tiger', 'Bear', 'Lion', 'Croc']
        monsternow = random.choice(monsters)
        health = 100
        monhealth = 100
        moves = ['A','Z','X']
        turn = ['player', 'comp']

        #introduction
        name = str(input('What is your name Gladiator?: '))
        print ('Welcome to the arena', name,'. Today you will be fighting a', monsternow,'. Good luck!')
        print ('---------------------------------------------')

        #while both players are alive 
        while health > 0 and monhealth > 0:
            #for each turn
            for user in turn: 
                #that both players have health
                if health > 0 and monhealth > 0:

                    #player moves
                    if user == 'player':
                        print ('A) Quick attack. Z) Heavy attack. X) Defend & Heal')
                        move = str(input('Choose a move:'))
                        print ('---------------------------------------------')
                        time.sleep(1)
                        if move == 'A' and user == 'player':
                            dmg = randint(18,25)
                            print (name, 'darts forward and swings at the', monsternow)
                            print (name, 'hits the', monsternow, 'for', dmg,'dmg')
                            monhealth = monhealth - dmg
                        elif move == 'Z' and user == 'player':
                            dmg = randint(10,35)
                            print (name, 'swings at the', monsternow, 'with all his might.')
                            print (name, 'hits the', monsternow, 'for', dmg,'dmg')
                            monhealth = monhealth - dmg
                        elif move == 'X' and user == 'player':
                            heal = randint(18,25)
                            print (name, 'raises his guard.')
                            print (name, 'heals himself for', heal,'HP')
                            health = health + heal
                        print ('[',name,':', health, 'HP',';', monsternow,':', monhealth,'HP',']')
                        print ('---------------------------------------------')

                    #computer moves  
                    elif user == 'comp':
                        move = random.choice(moves)
                        time.sleep(3)
                        if move == 'A':
                            dmg = randint(18,25)
                            print (monsternow, 'suddenly attacks', name)
                            print (monsternow, 'hits', name, 'for', dmg,'dmg')
                            health = health - dmg
                        elif move == 'Z':
                            dmg = randint(10,35)
                            print (monsternow, 'ferociously attacks', name)
                            print (monsternow, 'hits', name, 'for', dmg,'dmg')
                            health = health - dmg
                        elif move == 'X':
                            heal = randint(18,25)
                            print (monsternow, 'guards itself.')
                            print (monsternow, 'heals itself for', heal,'HP')
                            monhealth = monhealth + heal
                        print ('[',name,':', health, 'HP',';', monsternow,':', monhealth,'HP',']')
                        print ('---------------------------------------------')
                        
        #when one player has died
        else:
            if health <= 0:
                print ('The', monsternow, 'has killed you!')
            elif monhealth <= 0:
                print ('The', monsternow, 'is dead. You have slayed the beast. Congratulations', name,'!')
            print('_______________GAME OVER___________________')
    except ValueError:
        print('Please input a valid integer. Starting Over')
        print('___________________________________________')
main()
