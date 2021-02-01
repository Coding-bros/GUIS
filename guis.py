"""
Hi, This is a Tkinter Based Module create by the Coding-bros Organization,

For this modle to work, you need to install few dependencies:
    1) python3
    2) Tkinter

This module is called GUIS which means GUI Simplified / Graphial User Interface Simplified.

This module helps you in making your Tkinter GUI, Fast and Easy, and our module doesn't need .pack at the end :O

People involved:
    Karthik: bkp.karthi@gmail.com
    Jaideep: jaideep1163@gmail.com
    Eshan Sistla: greatesh2006@gmail.com

Started on:
    1st February, 2021
"""

#Importing Tkinter
from tkinter import *

def makeWindow(name, geometry, color):
    global window
    """
    This Function makes a window for you,
    For this function to work, you have to do the following:

    guis.makeWindow("name", "geometry", "color")

    eg: guis.makeWindow("Test", "500x300", "orange")
    """
    # Coniguring Tk() to window
    window = Tk()
    
    # Giving the window a Title
    window.title(name)
    
    # Setting the size / geometry of the window
    window.geometry(geometry)

    # Setting the color of the window
    window.config(bg = color)

def makeLabel(text, bg, fg):
    """This Function Adds A Label on Your Window,
    For this function to work, you have to do the following:

    guis.label("text", "bg", "fg")
    
    eg: guis.label("Test", "red", "orange")
    """
    
    Label(window, text=text, bg=bg, fg=fg).pack()
def mainloop():
    """
    This function will mainloop the code so that your code will work.
    For this function to work, you have to keep this function at the end of the code.

    guis.mainloop()
    """
    window.mainloop()
