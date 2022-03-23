
from mimetypes import init
import random
class Dice:
    
    def __init__(self):
        self.result = ""
    
    def roll(self):
        dice =  str(random.randrange(1,7,1))
        self.result = dice
        return self.result 
        
    
    def show(self):
        return print(self.result)




play = Dice()
play.roll()
play.show()

