import tkinter as tk
import time

#Guts of the code

Points=0

#Classes

class AutoClickers:
    def __init__(self,price,counter,multiplier,value):
        self.price=price
        self.counter=counter
        self.multiplier=multiplier
        self.value=value
#Objects

Upgrade_1 = AutoClickers(10,0,1.25,1)

#Functions

def Click():
    #called by click button, adds one to total point each button press
    global Points
    Points += 1
    Points_Label.config(text = Points) #Updates points label

def Upgrade_1_Click(): #Called by tier 1 button
    global Points
    if Points >= Upgrade_1.price: #Checks if you have enough points to buy upgrade
        Points -= Upgrade_1.price #Subtracts cost from total points
        Upgrade_1.price = round(Upgrade_1.price * Upgrade_1.multiplier) #Updates new price by multiplying and then rounding down
        Upgrade_1.counter += 1 #adds 1 to the tier counter
        Tier1.config(text="Tier 1 Autobuyer\nCost:"+str(Upgrade_1.price)+"\n Amount:"+str(Upgrade_1.counter)) #Updates autoclicker label
        Points_Label.config(text = Points) #Updates points value



#Loops

def Autoadder():
    global Points
    #adds the weight of the autoclicker multiplied by the amount bought
    Points += Upgrade_1.value*Upgrade_1.counter
    #Updates Points
    Points_Label.config(text = Points)
    #waits a second and then loops
    window.after(1000,Autoadder)


#GUI

window=tk.Tk()

#Title

Frame1=tk.Frame(master=window)
Title=tk.Label(master=Frame1,text="Clicker Game")
Title.pack()

#Counter
Frame2=tk.Frame(master=window)
Points_Label=tk.Label(master=Frame2,text=Points)
Points_Label.pack()

#Button 1
Frame3=tk.Frame(master=window,)
MainClick=tk.Button(
    master=Frame3,
    text="Click",
    height=5,
    width=30,
    fg="black",
    bg="grey",
    command=Click
)
MainClick.pack()

#Button 2
Frame4=tk.Frame(master=window)
Tier1=tk.Button(
    master=Frame4,
    text="Tier 1 Autobuyer\nCost:"+str(Upgrade_1.price)+"\n Amount:"+str(Upgrade_1.counter),
    height=3,
    width=30,
    fg="black",
    bg="grey",
    command=Upgrade_1_Click
)
Tier1.pack()


Frame1.pack()
Frame2.pack()
Frame3.pack()
Frame4.pack()

Autoadder()

window.mainloop()