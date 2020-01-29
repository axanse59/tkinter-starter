# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Are you Alex?"
lbl = Label(window, text="Are you Alex?")
 
# Place the label in the window at 0, 0
lbl.grid(column=0, row=1)

firstLabel = Label(window, text="Are you Alex?", font=("Arial Bold", 50))
firstLabel.grid(column=0, row=0)      

txt = Entry(window,width=10)
 
txt.grid(column=1, row=0) 

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=3, row=2)


window.mainloop()     # Keep the window open