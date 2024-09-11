import functions
player_count = 0
defaultpropertytuple = ("first","Central","Wan Chai", "Income Tax: Pay 10%", "Stanley", )
#-1:start -2:chance -3:free_parking -4:gotojail -5jail -6income_tax
defaultpropertycost = (-1,800,700,-1,600,-1,400,500,-1,400,-1,700,-1,400,500,-1,400,400,-1,600)
class character():
    def __init__(self):
        self.coins = 1500
        self.property = []
        self.injail = False
    def throws_dice(self):
        dice1, dice2 = functions.draw()
        if (self.injail):
            return dice1==dice2


    def go_to_jail(self):


class property_LinkedList:
