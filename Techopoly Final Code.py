import RPi.GPIO as GPIO

from tkinter import *

from random import randint

from time import sleep

# initiate switches fo GPIO input
switch1 = 17
switch2 = 16
switch3 = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
# initiate properties as a list
Properties = ["GO","Bookstore","Library","Bulldog Railroad","Clocktower","The Quad",

              "Tolliver","South Hall","Graham Hall","Dudley Hall","Aswell Hall","Adams Hall",

              "Free Wifi","IESB","Wyly Tower","Tech Express","Nethken Hall","Davison Hall",

              "Bogard Hall","Pass A Class","TAC","Lambright","Joe Aillet Stadium","Love Shack"]

 
# establish a Buy and Rent value for each property
Prop_BUY  = [0,60,60,200,100,100,120,0,140,160,180,200,0,220,240,200,260,260,280,0,300,300,350,450]

Prop_RENT = [0,30,30,100,50,50,60,0,70,80,90,100,0,110,120,100,130,130,140,0,150,150,175,275]

 
# Establishes the Unowned / Owned Lists

Unowned = ["Bookstore","Library","Bulldog Railroad","Clocktower","The Quad",

           "Tolliver","Graham Hall","Dudley Hall","Aswell Hall","Adams Hall",

           "IESB","Wyly Tower","Tech Express","Nethken Hall","Davison Hall",

           "Bogard Hall","TAC","Lambright","Joe Aillet Stadium","Love Shack"]

Owned = []
 
# creates the Player class
class Player():

    def __init__(self,name):

        self.name = name

        self.money = 1000

        self.location = ["GO"]

        self.inventory = []

       

    # getter and setter for name

    @property

    def name(self):

        return self._name

   

    @name.setter

    def name(self, value):

        self._name = value

 

    # getter and setter for money

    @property

    def money(self):

        return self._money

   

    @money.setter

    def money(self, value):

        self._money = value

 

    # getter and setter for location

    @property

    def location(self):

        return self._location

   

    @location.setter

    def location(self, value):

        self._location = value

 

    # getter and setter for inventory

    @property

    def inventory(self):

        return self._inventory

   

    @inventory.setter

    def inventory(self, value):

        self._inventory = value

 

    def addInventory(self, item):

        self._inventory.append(item)

 
# string function to display the game status
    def __str__(self):

        s = "{}'s Turn\n".format(self.name)

        s += "You are at {}\n".format(self.location)

        s += "You have ${}\n".format(self.money)

        s += "You own {}\n".format(self.inventory)

 

        return s
  
# Gameplay

class Game(Frame):

 

    def __init__(self,parent):

        Frame.__init__(self,parent)

       
# creates each player and gives them default values

    def createPlayers(self):

        global currentTurn

        global P1

        global P2

        global P3

       

        P1 = Player("Player 1")

        P2 = Player("Player 2")

        P3 = Player("Player 3")

 

        Game.currentTurn = P1

# Player 1's Turn
    def player1Turn(self,name):

        Game.currentTurn = P1

        roll = randint(0,23)

        location = Properties[roll]
        
        # When landing at South Hall, the Player pays $25
        if (location == "South Hall"):

                P1.money -= 25

                exit
        # When landing at GO, the Player recieves $200
        if (location == "GO"):

                P1.money += 200

                exit
        # These properties are free spaces
        if (location == "Free Wifi" or "Pass A Class"):

                pass

                exit

        # Checks if the property owned by another
        # and pays rent to that Player
        if (location in Owned):

            if (location in P1.inventory):

                pass

           

            if (location in P2.inventory):

                P1.money -= Prop_RENT[roll]

                P2.money += Prop_RENT[roll]

                   

            if (location in P3.inventory):

                P1.money -= Prop_RENT[roll]

                P3.money += Prop_RENT[roll]

               
        # checks if the property is unowned and buys the location
        if (location in Unowned):

           

            P1.money -= Prop_BUY[roll]

            P1.addInventory(Properties[roll])

            Owned.append(Properties[roll])

            Unowned.remove(Properties[roll])

           
        # These lines manage the player's properties and inventory
        del P1.location[-1]

        P1.location.append(Properties[roll])

        self.setStatus(Game.currentTurn)
        self.setP1Image()
        self.checkforWin()
       
# Player 2's Turn
    def player2Turn(self,name):

        Game.currentTurn = P2

        roll = randint(0,23)

        location = Properties[roll]
        
        # When landing at South Hall, the Player pays $25
        if (location == "South Hall"):

                P2.money -= 25

                exit

        # When landing at GO, the Player recieves $200
        if (location == "GO"):

                P2.money += 200

                exit

        # These properties are free spaces
        if (location == "Free Wifi" or "Pass A Class"):

                pass

                exit

        # Checks if the property owned by another
        # and pays rent to that Player
        if (location in Owned):

            if (location in P2.inventory):

                pass

           

            if (location in P1.inventory):

                P2.money -= Prop_RENT[roll]

                P1.money += Prop_RENT[roll]

                   

            if (location in P3.inventory):

                P2.money -= Prop_RENT[roll]

                P3.money += Prop_RENT[roll]

               
        # checks if the property is unowned and buys the location
        if (location in Unowned):


            P2.money -= Prop_BUY[roll]

            P2.addInventory(Properties[roll])

            Owned.append(Properties[roll])

            Unowned.remove(Properties[roll])

           

            
        # These lines manage the player's properties and inventory
        del P2.location[-1]

        P2.location.append(Properties[roll])

        self.setStatus(Game.currentTurn)

        self.setP2Image()

        self.checkforWin()
       

# Player 3's Turn
    def player2Turn(self,name):

        Game.currentTurn = P3

        roll = randint(0,23)

        location = Properties[roll]
        
        # When landing at South Hall, the Player pays $25
        if (location == "South Hall"):

                P3.money -= 25

                exit

        # When landing at GO, the Player recieves $200
        if (location == "GO"):

                P3.money += 200

                exit

        # These properties are free spaces
        if (location == "Free Wifi" or "Pass A Class"):

                pass

                exit

        # Checks if the property owned by another
        # and pays rent to that Player
        if (location in Owned):

            if (location in P3.inventory):

                pass

           

            if (location in P1.inventory):

                P3.money -= Prop_RENT[roll]

                P1.money += Prop_RENT[roll]

                   

            if (location in P2.inventory):

                P3.money -= Prop_RENT[roll]

                P2.money += Prop_RENT[roll]

               
        # checks if the property is unowned and buys the location
        if (location in Unowned):


            P3.money -= Prop_BUY[roll]

            P3.addInventory(Properties[roll])

            Owned.append(Properties[roll])

            Unowned.remove(Properties[roll])

           
        # These lines manage the player's properties and inventory
        del P3.location[-1]

        P3.location.append(Properties[roll])

        self.setStatus(Game.currentTurn)

        self.setP3Image()

        self.checkforWin()

        
    # In case of a win, this checks for the overall winner
    def checkforWinner(self):

        if (P1.money > P2.money and P3.money):


            self.setWinImage()

            self.setPlayer1WinStatus("")

            self.update()

            sleep(5)

            exit()

 

        if (P2.money > P1.money and P3.money):


            self.setWinImage()

            self.setPlayer2WinStatus("")
            
            self.update()

            sleep(5)

            exit()

 

        if (P3.money > P1.money and P2.money):


            self.setWinImage()

            self.setPlayer3WinStatus("")

            self.update()

            sleep(5)

            exit()

 
    # Establishes a loser in the game
    def lose(self):

        if (P1.money < P2.money and P3.money):

            print("LOSE")

            self.setLoseImage()

            self.setPlayer1LoseStatus("")

            self.update()

            sleep(3)
            
            self.checkforWinner()
            

                    

            

        if (P2.money < P1.money and P3.money):

            print("LOSE")

            self.setLoseImage()

            self.setPlayer2LoseStatus("")

            self.update()

            sleep(3)

            self.checkforWinner()
            
            

            

        if (P3.money < P2.money and P1.money):

            print("LOSE")

            self.setLoseImage()

            self.setPlayer3LoseStatus("")

            self.update()

            sleep(3)
            
            self.checkforWinner()
           
    # Checks for end of game scenario
    def checkforWin(self):

       

        if P1.money <= 0:

            self.lose()

 

        elif P2.money <= 0:

            self.lose()

 

        elif P3.money <= 0:

            self.lose()

 

        print("CHECKED")

       
    # Sets the Win Image on GUI
    def setWinImage(self):

        Game.img = PhotoImage(file="win.gif")

        Game.image.config(image=Game.img)

        Game.image.image = Game.img

 
    # Sets the Lose Image on GUI
    def setLoseImage(self):

        Game.img = PhotoImage(file="lose.gif")

        Game.image.config(image=Game.img)

        Game.image.image = Game.img
        
    # Sets the Player 1 Image on GUI
    def setP1Image(self):

        Game.img = PhotoImage(file="tplayer1.gif")

        Game.image.config(image=Game.img)

        Game.image.image = Game.img
        
    # Sets the Player 2 Image on GUI
    def setP2Image(self):

        Game.img = PhotoImage(file="tplayer2.gif")

        Game.image.config(image=Game.img)

        Game.image.image = Game.img
        
    # Sets the Player 3 Image on GUI
    def setP3Image(self):

        Game.img = PhotoImage(file="tplayer3.gif")

        Game.image.config(image=Game.img)

        Game.image.image = Game.img
        
    # Sets the Player 1 Win Statement on GUI
    def setPlayer1WinStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Congrats! Player 1 Won.")

        Game.text.config(state=DISABLED)

 
    # Sets the Player 2 Win Statement on GUI
    def setPlayer2WinStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Congrats! Player 2 Won.")

        Game.text.config(state=DISABLED)

 
    # Sets the Player 3 Win Statement on GUI
    def setPlayer3WinStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Congrats! Player 3 Won.")

        Game.text.config(state=DISABLED)

 
    # Sets the Player 1 Lose Statement on GUI
    def setPlayer1LoseStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Game Over!\n"+"Player 1 went Bankrupt.")

        Game.text.config(state=DISABLED)

 
    # Sets the Player 2 Lose Statement on GUI
    def setPlayer2LoseStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Game Over!\n"+"Player 2 went Bankrupt.")

        Game.text.config(state=DISABLED)

 
    # Sets the Player 3 Lose Statement on GUI
    def setPlayer3LoseStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Game Over!\n"+"Player 3 went Bankrupt.")

        Game.text.config(state=DISABLED)
        
    # Sets the Opening Game Statement on GUI
    def setBegStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,"Welcome to Techopoly!.\n"+"Player 1 begin your turn by pressing P1.")

        Game.text.config(state=DISABLED)

        

    # Sets up GUI
    def setupGUI(self):

    #organize and pack the GUI

        self.pack(fill=BOTH,expand=1)

    # setup image on the left

        img = None

        Game.image = Label(self, width=WIDTH//2,image = img)

        Game.image.pack(side=LEFT, fill=Y)

        Game.image.pack_propagate(False)

       

    # setup text output on the right

        text_frame = Frame(self, width=WIDTH//2)

        Game.text = Text(text_frame, bg="lightblue", state=DISABLED)

        Game.text.pack(fill=Y, expand=1)

        text_frame.pack(side=RIGHT, fill=Y)

        text_frame.pack_propagate(False)
 
    # Sets Game image
    def setGameImage(self):

        Game.img = PhotoImage(file="techopoly.gif")

        Game.image.config(image=Game.img)

        Game.image.image = Game.img

 
    # Sets Player Status
    def setStatus(self,status):

        Game.text.config(state=NORMAL)

        Game.text.delete("1.0",END)

        Game.text.insert(END,str(Game.currentTurn))

        Game.text.config(state=DISABLED)

    # Establishes the Game
    def play(self):

        self.setupGUI()

        self.setGameImage()

        self.createPlayers()

        self.setStatus("")

        self.setBegStatus("")


#### main code (construct a display and begin game)####

# define default screen size

WIDTH = 800

HEIGHT = 600

 

# create the window

window = Tk()

window.title("Techopoly")

 

# create the GUI as a canvas

g = Game(window)

g.play()

window.update()

# Run the Game till the end
while True:
    if (GPIO.input(switch1) == GPIO.HIGH):
        pressed = True
        g.player1Turn(P1)
        sleep(0.25)
        g.setStatus(Game.currentTurn)
                
            

    elif (GPIO.input(switch2) == GPIO.HIGH):
        pressed = True
        g.player2Turn(P2)
        sleep(0.25)
        g.setStatus(Game.currentTurn)
                
                    

    elif (GPIO.input(switch3) == GPIO.HIGH):
        pressed = True
        g.player3Turn(P3)
        sleep(0.25)
        g.setStatus(Game.currentTurn)
    window.update()


GPIO.cleanup()
 
