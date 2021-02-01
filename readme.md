## With Our Module

```py
import guis
guis.makeWindow("myWindow", "500x500", "red")

guis.mainloop()
```

## Without Our Module
```py
from tkinter import *

window = Tk()

window.title("My Window")
window.geometry("500x500")
window.config("red")

window.mainloop()