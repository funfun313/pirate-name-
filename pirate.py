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
        x = ord(self.first[0].upper())-65
        y = ord(self.second[0].upper())-65
        z = ord(self.third[0].upper())-65
        pirateName = self.firstList[x % len(self.firstList)] + " " + self.secondList[y % len(self.secondList)] + " " + self.thirdList[z % len(self.thirdList)]
        return pirateName

def addnew():
    #get values out of text boxes
    fn = fBox.get()
    sn = sBox.get()
    tn = tBox.get()
    #create the pirate instance and initialize the values
    mypirate = Pirate(fn, sn, tn)
    #generate name
    newname = mypirate.name()
    #show name
    output.config(text=newname, compound=CENTER)
    #erase text boxes
    fBox.delete(0,"end")
    sBox.delete(0,"end")
    tBox.delete(0,"end")

    
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
btn= Button(root, text ="Show Me My Name!", font="Arial 16 bold", bg="#eeddff", command=addnew)
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
