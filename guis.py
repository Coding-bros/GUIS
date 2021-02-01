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

def makeWindow(name = "Tk", geometry = "200x200", color = "white"):
    global window
    """
    This Function makes a window for you,
    For this function to work, you have to do the following:

    guis.makeWindow("name", "geometry", "color")

    eg: guis.makeWindow("Test", "500x300", "orange")

    incase you give:

    guis.makeWindow()
    
    you get the window in 200x200, name as Tk, and color in white.
    """
    # Coniguring Tk() to window
    window = Tk()
    
    # Giving the window a Title
    window.title(name)
    
    # Setting the size / geometry of the window
    window.geometry(geometry)

    # Setting the color of the window
    window.config(bg = color)

# ------------------------------------------------->

def windowColor(color):
    """
    This function lets you change just the background-color of your window

    how to use:
    
    guis.windowColor("color")

    eg: guis.windowColor("orange")
    """
    window.config(bg = color)


def windowBg(bg):
    """
    This function lets you change just the background-color of your window

    how to use:
    
    guis.windowBg("color")

    eg: guis.windowBg("orange")
    """
    window.config(bg = bg)

# ------------------------------------------------->

def windowSize(size):
    """
    This function lets you change just the geometry / size of your window

    how to use:
    
    guis.windowSize("geometry / size")

    eg: guis.windowSize("500x300")
    """
    window.geometry(size)


def windowGeometry(geometry):
    """
    This function lets you change just the geometry / size of your window

    how to use:
    
    guis.windowGeometry("geometry / size")

    eg: guis.windowGeometry"500x300")
    """
    window.geometry(geometry)

# ------------------------------------------------->

def windowTitle(title):
    """
    This function lets you change just the Title of your window

    how to use:

    guis.windowTitle("title")

    eg: guis.windowTitle("test")
    """
    window.title(title)


def windowName(name):
    """
    This function lets you change just the Title of your window

    how to use:

    guis.windowName("title")

    eg: guis.windowName("test")
    """
    window.title(Name)

# ------------------------------------------------->
def makeLabel(text = "Label", bg = "white", fg = "black"):
    """
    This Function Adds A Label on Your Window,
    For this function to work, you have to do the following:

    guis.makeLabel("text", "bg", "fg")
    
    eg: guis.makeLabel("Test", "red", "orange")
    """
    Label(window, text = text, bg = bg, fg = fg).pack()

def makeText(text = "Label", bg = "white", fg = "black"):
    """
    This Function Adds A Label on Your Window,
    For this function to work, you have to do the following:

    guis.makeLabel("text", "bg", "fg")
    
    eg: guis.makeLabel("Test", "red", "orange")

    Incase you keep it as:

    guis.makeLabel()

    You will get the text as "Label", the bg / background color as white, and the fg / foreground / font color as white
    """
    Label(window, text = text, bg = bg, fg = fg).pack()

# ------------------------------------------------>

def makeButton(text = "Button", bg = "grey", fg = "black"):
    """
    This Function Adds A button on Your Window,
    For this function to work, you have to do the following:

    guis.makeButton("text", "bg", "fg")

    eg: guis.makeButton("Click Me", "black", "white")

    Incase you keep it as:

    guis.makeButton()

    you will get the text as "Button", the bg / background color as grey, and the fg / foreground / text color as black
    """
    Button(text = text, bg = bg, fg = fg).pack()
# ------------------------------------------------>

def mainloop():
    """
    This function will mainloop the code so that your code will work.
    For this function to work, you have to keep this function at the end of the code.

    guis.mainloop()
    """
    window.mainloop()
