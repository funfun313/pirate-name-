import random
class Pirate:
    first = ""
    second = ""
    third = ""
    firstList = ["Captain","Fluffbucket","Peg Leg", "Lady", "Buccaneer", "Sharkbait", "Miss", "Matey" ]
    secondList = ["Storm","Sea","Gold","Patch","Legs","Frost","Thunder","Spot"]
    thirdList = ["Byrd", "Kidd", "Hornswaggle", "of Dark Water", "of Atlantis", "Rivers", "Three Gates", "Sea Wolf", "Swashbuckler"]
    
    def __init__(self,first, second, third):
        x=0
        self.first = first
        self.second = second
        self.third = third
        #put parameters into properties
    def name(self):
        #this function will figure out and return the name
        x = random.randint(0,len(self.firstList)-1)
        y = random.randint(0,len(self.secondList)-1)
        z = random.randint(0,len(self.thirdList)-1)
        pirateName = self.firstList[x] + " " + self.secondList[y] + " " + self.thirdList[z]
        return pirateName
        
