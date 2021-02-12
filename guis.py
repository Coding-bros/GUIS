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
    """
\033[1;36;1mThese are all the commands,

\033[1;33;1mmakeWindow()

    \033[1;32;1mThis Function makes a window for you,
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
\033[1;33;1mwindowColor()

    \033[1;32;1mThis function lets you change just the background-color of your window

    how to use:
    
    guis.windowColor("color")

    eg: guis.windowColor("orange")
    """
    window.config(bg = color)


def windowBg(bg):
    """
\033[1;33;1mwindowBg()

    This function lets you change just the background-color of your window

    how to use:
    
    guis.windowBg("color")

    eg: guis.windowBg("orange")
    """
    window.config(bg = bg)

# ------------------------------------------------->

def windowSize(size):
    """
\033[1;33;1mwindowSize() / windowGeometry()

    \033[1;32;1mThis function lets you change just the geometry / size of your window

    how to use:
    
    guis.windowSize("geometry / size")

    eg: guis.windowSize("500x300")
    """
    window.geometry(size)


def windowGeometry(geometry):
    """
\033[1;33;1mwindowGeometry() / windowSize()

    This function lets you change just the geometry / size of your window

    how to use:
    
    guis.windowGeometry("geometry / size")

    eg: guis.windowGeometry"500x300")
    """
    window.geometry(geometry)

# ------------------------------------------------->

def windowTitle(title):
    """
\033[1;33;1mwindowTitle() / windowName()

    \033[1;32;1mThis function lets you change just the Title of your window

    how to use:

    guis.windowTitle("title")

    eg: guis.windowTitle("test")
    """
    window.title(title)


def windowName(name):
    """
\033[1;33;1mwindowName() / windowTitle()

    This function lets you change just the Title of your window

    how to use:

    guis.windowName("title")

    eg: guis.windowName("test")
    """
    window.title(Name)

# ------------------------------------------------->
def makeLabel(text = "Label", bg = "white", fg = "black"):
    """
\033[1;33;1mmakeLabel() / makeText()

    \033[1;32;1mThis Function Adds A Label on Your Window,
    For this function to work, you have to do the following:

    guis.makeLabel("text", "bg", "fg")
    
    eg: guis.makeLabel("Test", "red", "orange")
    """
    Label(window, text = text, bg = bg, fg = fg).pack()

def makeText(text = "Label", bg = "white", fg = "black"):
    """
\033[1;33;1mmakeText() / makeLabel()

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
\033[1;33;1mmakeButton()

    \033[1;32;1mThis Function Adds A button on Your Window,
    For this function to work, you have to do the following:

    guis.makeButton("text", "bg", "fg")

    eg: guis.makeButton("Click Me", "black", "white")

    Incase you keep it as:

    guis.makeButton()

    you will get the text as "Button", the bg / background color as grey, and the fg / foreground / text color as black
    """
    Button(text = text, bg = bg, fg = fg).pack()
# ------------------------------------------------>

def insertBlank(bg = "white", times = 1):
    """
\033[1;33;1minsertBlank()

    \033[1;32;1mThis Function Adds A blank space in your Window,
    This helps in moving your items away from each other.

    For this function to work, you have to do the following:

    guis.insertBlank("background color", "how many blanks")

    eg: guis.insertBlank("orange", 3)

    Incase you kept it as:

    guis.insertBlank()

    you will get, 1 white blank space.
    """

    for i in range(times):
        Label(text = " ", bg = bg).pack()
# ------------------------------------------------>

def mainloop():
    """
\033[1;33;1mmainloop()

    \033[1;32;1mThis function will mainloop the code so that your code will work.
    For this function to work, you have to keep this function at the end of the code.

    guis.mainloop()
    """
    window.mainloop()

# ------------------------------------------------>

def commands():
    print(makeWindow.__doc__)
    print(" ")
    print(makeButton.__doc__)
    print(" ")
    print(makeLabel.__doc__)
    print(" ")
    print(windowColor.__doc__)
    print(" ")
    print(windowSize.__doc__)
    print(" ")
    print(windowTitle.__doc__)
    print(" ")
    print(insertBlank.__doc__)
    print(" ")
    print(mainloop.__doc__)
