import numpy as npy
import pyautogui as auto
import tkinter as tk
 

window=tk.Tk()

window.title("Coordinated Auto-Clicker")



def callbackLoad():
    print("der blev vist lige trykket")
    #loade csv fil klar til kørsel

def callbackStart():
    print( "click!")
    #starte kørsels loopet og kører den loadede sti

def callbackStop():
    print( "click!")
    #stoppe hvad end start sætter igang

def callbackNy():
    print("der blev vist lige trykket")
    #funktionalitet udvides og afklares

def callbackOptag():
    print( "click!")
    #tror det her bliver den sværeste funktion at implementere

def callbackRadiusPreview():
    print( "click!")
    lavvindue=tk.Tk()
    #Definer udseendet af vinduet inden "mainloop() køres"
    lavvindue.mainloop()
    

c = tk.Button(window, text="Load", command=callbackLoad)
c.grid(row=3,column=0)

d = tk.Button(window, text="Start", command=callbackStart)
d.grid(row=4,column=0)

b = tk.Button(window, text="Ny", command=callbackNy)
b.grid(row=0, column=0)

c = tk.Button(window, text="Optag", command=callbackOptag)
c.grid(row=1,column=0)

d = tk.Button(window, text="Radius", command=callbackRadiusPreview)
d.grid(row=2,column=0)

e = tk.Label(window,text="Reptition")
e.grid(row=3,column=2)

f = tk.Entry(window)
f.grid(row=4,column=2)

e = tk.Label(window,text="Reference Punkt")
e.grid(row=0,column=2)

f = tk.Entry(window)
f.grid(row=1,column=2)

g = tk.Button(window, text="Stop", command=callbackStop)
g.grid(row=4,column=1)

window.mainloop()



