#WarSim June 9
#The purpose of this program is to take 2 players and play war
#Outcomes are what is desired, for example how many turns the 
#longest game took and translate that into time taken to play the game
#Also on the chooping block is how to do recursion on the game
#By Phillip Chaboya

#TODO
#IMPLEMENT WAR
#WHEN PLAYER DOES NOT HAVE ANOTHER CARD AND A POT, PLAYER logic needed.

import random

class Deck:
    def __init__(self):
        """Creates the deck and shuffles it"""
        self.deck = [2,3,4,5,6,7,8,9,10,11,12,13,14,
                     2,3,4,5,6,7,8,9,10,11,12,13,14,
                     2,3,4,5,6,7,8,9,10,11,12,13,14,
                     2,3,4,5,6,7,8,9,10,11,12,13,14]
        print("Deck Created")
        self.shuffle()
        
        
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.deck)
        print("Deck Shuffled")
        
    def deal(self,players):
        """Distbutes cards to players"""
        #players are player one and player two
        while self.deck:
            players[0].playercards.append(self.deck.pop())
            players[1].playercards.append(self.deck.pop())
        print("Deck Distbuted")

    
class Player:
    
    players = []
    
    def printcards(self):
        """Displays cards player is currently holding"""
        print("%s cards are :" % self.name, len(self.playercards))
        print(self.playercards)
        
    def printpot(self):
        """Displays pot , cards that are in the game"""
        print("%s pot(s) are :" % self.name, len(self.playerpot))
        print(self.playerpot)
    
    def __init__(self,name):
        #Assigns theplayers name
        self.name = name
        print("Player %s created" % self.name)
        #Creats players cards and players pot
        self.playercards = []
        self.playerpot = []
        
        #adds self to players list for easy win methods
        self.players.append(self)
        
    def newgame(self):
        #after a game is over resets variables for more testing
        self.playercards = []
        self.playerpot = []
        
    def sayhello(self):
        #player says hello!
        print("%s says hello!" % self.name)
        
    def player_wins(self):
        """player wins takes the pot of all the players and appends
        the pot to the player hands, player wins always appends player
        one's hand first"""
        print("%s wins pot!" % self.name) 
        for aplayer in self.players:
            while aplayer.playerpot:
                self.playercards.append(aplayer.playerpot.pop())
        
        
class WarSim:
    
    def __init__(self):
        print("Game Started")
        self.playerone = Player("Phillip")
        self.playertwo = Player("Amber")
        self.players = [self.playerone,self.playertwo]
        playingdeck = Deck()
        playingdeck.deal(self.players)
        
    def gameround(self):
        
        print()
        self.playerone.printcards()
        self.playertwo.printcards()
        self.playerone.printpot()
        self.playertwo.printpot()
        print()
        
        print("NEW ROUND")
        
        self.playerone.playerpot.insert(0,self.playerone.playercards.pop(0))
        self.playertwo.playerpot.insert(0,self.playertwo.playercards.pop(0))
        
        print("%s card %d " % (self.playerone.name,self.playerone.playerpot[0]))
        print("%s card %d " % (self.playertwo.name,self.playertwo.playerpot[0]))
                
        if self.playerone.playerpot[0] > self.playertwo.playerpot[0] :
            self.playerone.player_wins()
            return 
        
        if self.playerone.playerpot[0] == self.playertwo.playerpot[0] :
            print("Players tie and go to war!")
            return
            
        if self.playerone.playerpot[0] < self.playertwo.playerpot[0] :
            self.playertwo.player_wins()
            return
        
    def gowar(self):
        """This should be a recursion function, war can occur over and over,
        recursion ends when one player wins or if a player runs out of cards"""
            
        
    def loopgame(self):
        count = 0
        while self.playerone.playercards and self.playertwo.playercards:
                count = count + 1
                self.gameround()
        print(count)
        
    
War = WarSim()
War.loopgame()


