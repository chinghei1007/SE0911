import functions
player_count = 0
properties = {
    'Start' : 0,
    'Central' : 800,
    'Wan Chai' : 700,
    'Income Tax' : -10,
    'Stanley' : 600,
    'Jail Position' : 0,
    'Shek O' : 400,
    'Mong Kok' : 500,
    '? Chance' : 0,
    'Tsing Yi' : 400,
    'Free Parking' : 0,
    'Shatin' : 700,
    '? Chance' : 0,
    'Tuen Mun' : 400,
    'Tai Po' : 500,
    'Go to Jail' : 0,
    'Sai Kung' : 400,
    'Yuen Long': 400,
    '? Chance': 0,
    'Tai O': 600

}
defaultpropertycost = (-1,800,700,-1,600,-1,400,500,-1,400,-1,700,-1,400,500,-1,400,400,-1,600)
class character():
    def __init__(self):
        self.coins = 1500
        self.property = []
        self.injail = False
        self.injailrounds = -1
        self.position = 0
    def throws_dice(self):
        dice1, dice2 = functions.draw()
        if (self.injail):
            return dice1==dice2


    def go_to_jail(self):


class property_LinkedList:
