import random
from tkinter import *
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
myfont="Arial 14 bold"
root = Tk()
#register image
banner= PhotoImage(file="pirate-banner.gif")
banner = banner.subsample(2,2)

#creating controls
title = Label(root, text="Discover Your Pirate Name", font="Arial 20 bold")
fLabel =Label(root, text="First name:", font=myfont)
sLabel =Label(root, text="Second name:", font=myfont)
tLabel =Label(root, text="Third name:", font=myfont)
fBox= Entry(root, font=myfont)
sBox= Entry(root, font=myfont)
tBox= Entry(root, font=myfont)
btn= Button(root, text ="Show Me My Name!", font="Arial 16 bold", bg="#eeddff")
output = Label(root, font="Gabriola 26", image=banner)


#adding them to screen
title.grid(row=0,column=0,columnspan=2)
fLabel.grid(row=1,column=0)
sLabel.grid(row=2,column=0)
tLabel.grid(row=3,column=0)
fBox.grid(row=1, column=1)
sBox.grid(row=2, column=1)
tBox.grid(row=3, column=1)
btn.grid(row=4,column=0, columnspan=2)
output.grid(row=5,column=0, columnspan=2)

root.mainloop()
