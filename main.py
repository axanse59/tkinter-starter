# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import *
from ttkthemes import ThemedTk
from tkinter import Menu
from tkinter.ttk import Progressbar
#from tkinter import ttk


window = ThemedTk(theme="arc")   
#window = Tk()         # Create the application window

# Add a label with the text "Are you Alex?"
lbl = Label(window, text="Are you Alex?")
 
# Place the label in the window at 0, 0
lbl.grid(column=0, row=1)

bar = Progressbar(window, length=200)
bar['value'] = 100

menu = Menu(window)
 
new_item = Menu(menu)
 
new_item.add_command(label='Alexs Menu')
 
new_item.add_separator()
 
new_item.add_command(label='Edit')

menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)

firstLabel = Label(window, text="Are you Alex?", font=("Arial Bold", 50))
firstLabel.grid(column=0, row=0)     

txt = Entry(window,width=10)
 
txt.grid(column=1, row=0) 

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=3, row=2)

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=3, row=3)

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=4, row=5)

style = Style()
  
style.configure("black.Horizontal.TProgressbar", background='blue')
 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 70
 
bar.grid(column=5, row=6)
 

window.mainloop()     # Keep the window open