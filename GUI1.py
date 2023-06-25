# import tkinter as tk
# from tkinter import *
#
# root = tk.Tk()  # tk is main library and we are calling it's constructor
# root.geometry("500x500")  # setting the width and height of the window
# root.title("Experimentation")  # Setting the title of the window
#
# # Everything in this section as a width and a height and font and text(textbox and entry and label do not have text attribute)
# label = tk.Label(root, text="First GUI", font = ('Arial',20)) # Like a heading of the window
# label.pack() # Packing it in root without padding
# textbox = tk.Text(root,height = 3, font=("Arial",16)) # Creating a text box for user to type in of height 3 lines, no hegith means  infinite textbox
# myentry = tk.Entry(root) # Very small box, not like textbox
# myentry.pack() # can add padding
# textbox.pack() # can add padding
#
#
# button = tk.Button(root,text="Click Me!", font=("Arial",18)) # small button under the text box(because of order)
# button.pack(padx=10,pady=10) # packing button, can add padding if I want to
#
#
#
#
#
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("500x500")
root.title("Small test")
label = tk.Label(root,text="Hello world",font=("Arial",18),fg="red",bg="blue")
label.pack(padx=10,pady=10)

textbox = tk.Text(root,height=3, font=("Arial",16))
textbox.pack(padx=10,pady=10)

def heClicked():
    label = tk.Label(root,text="I got clicked")
    label.pack()
button = tk.Button(root,text="Click me",font=("Arial",20),command=heClicked)
button.pack()
tk.mainloop()
