import tkinter as tk
import time

#Guts of the code

def price_increase(self):
    """Increases the price of each auto clicker tier"""
    self.price= self.price * self.price_increment

class AutoClicker:
    def __init__(self,name,price,price_increment,):
        """
        name=Name of the tier
        price=The current price of the tier
        price_increment=The exponent that the price gows at for each upgrade 
        """

        self.name = name
        self.price = price
        self.price_increment = price_increment

Clicker1 = AutoClicker("tier 1",10,1.125)

def increase():
    """Increases point counter with each click"""
    value = int(Count_Label["text"])
    Count_Label["text"] = f"{value + 1}"


def Tier1_click():
    """Checks if you have enough points to buy a clicker"""
    value = int(Count_Label["text"])
    def Auto1():
        global T1
        T1=True
        print(T1)
        return T1
    if value >= 10:
        Count_Label["text"] = f"{value - Clicker1.price}"
        Tier1_click.Tier1Amnt = int(Tier1_Label["text"])
        Tier1_Label["text"] = f"{Tier1_click.Tier1Amnt + 1}"
        Auto1()



#Autoclickers

global T1
T1=False
print(T1)
timeout=1

while T1==True:
    #Tier 1
    print("Running")
    global Count
    Count = int(Count_Label["text"])
    print(Count)
    Count_Label["text"] = (Count + Tier1_click.Tier1Amnt)
    time.sleep(timeout)
            

#GUI

window=tk.Tk()

#Title

Frame1=tk.Frame(master=window)
Title=tk.Label(master=Frame1,text="Clicker Game")
Title.pack()

#Counter

Frame2=tk.Frame(master=window)
Count_Label=tk.Label(master=Frame2,text="0")
Count_Label.pack()

#Button 1
Frame3=tk.Frame(master=window,)
MainClick=tk.Button(
    master=Frame3,
    text="Click",
    height=5,
    width=30,
    fg="black",
    bg="grey",
    command=increase
)
MainClick.pack()

#Button 2
Frame4=tk.Frame(master=window)
Tier1=tk.Button(
    master=Frame4,
    text="Tier 1 Autobuyer\nCost:"+str(Clicker1.price),
    height=2,
    width=30,
    fg="black",
    bg="grey",
    command=Tier1_click
)
Tier1.pack()
Frame5=tk.Frame(master=window)
Tier1_Label=tk.Label(
    master=Frame5,
    text="0"
)
Tier1_Label.pack()

Frame1.pack()
Frame2.pack()
Frame3.pack()
Frame4.pack()
Frame5.pack()

window.mainloop()