## What Does GUIS Mean?
#

### GUIS is **GUI / Graphical User Interface Simplified**

### This is a module based on Tkinter, This helps you make you Tkinter code **Fast, Easy**, and our **Module doesn't need .pack() for Labels, Buttons, etc...**
#
### You can also get this module from github:
 www.github.com/Coding-bros/GUIS
 #

## **Installation**

```python
pip install guis
```
### or

```python
pip3 install guis
```
#


# Use of GUIS

## Using guis

```python
import guis

guis.makeWindow("Window-Title", "200x200", "orange")

guis.makeLabel("This is a Label", "black", "white")

guis.makeButton("Click me", "white", "black")

guis.mainloop()
```

## Using Tkinter

```python
from tkinter import *

Window = Tk()

window.title("Window-Title")

window.geometry("200x200")

window.configure(bg = "orange")

Label(text = "This is a Label", bg = "black", fg = "white").pack()

Button(text = "Click me", bg = "white", fg = "black").pack()


window.mainloop()
```

## **If any problems, Feel Free to Contact Us:**
> ## bkp.karthi@gmail.com
> ## jaideep1163@gmail.com

# ----------Thank You--------