# import modules and libraries
import tkinter as tk
from tkinter import ttk
import random

# Build the window
window = tk.Tk()
# Give the window a name to display on top
window.title("RPG Dice")
# set a window size
window.geometry('1525x100')
# make this size not alterable
# window.resizable(width=False, height=False)

## TODO ##
# Set a background image
# bgPic = PhotoImage(file = "C:/Users/Zach/PycharmProjects/RPGDICE/otherFantasy.jpg")
# background_label = Label(top, image=bgPic)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# window.pack()

#set global values and variables
global history1
global history2
result = "Waiting to roll..."
history1 = ""
history2 = ""

# what happens when the roll button is clicked
def clicked():
    # get sides and quantity from dropdown menus
    sides = int(combo.get())
    quant = int(quantCombo.get())
    modifierNum = int(modifier.get())
    # update the history list
    # history2 = lblH1['text']
    # history1 = lbl['text']

    # create an empty list to collect the rolls
    theList = []
    # set increment counter
    counter = 1
    # if there is no modifier
    if modifier == 0:
        # for all of the dice to be rolled...
        for each in range(0, int(quant)):
            if sides == 20: # If it's 20-sided...
                result = random.randint(1, sides)
                if result == 20: # and the result is 20... CRITICAL HIT!
                    theList.append("# " + str(counter) + " is : " + str(result) + " ... Critical Success!")
                    counter += 1 # increment up
                elif result == 1: # or if the result is 1... CRITICAL MISS!
                    theList.append("# " + str(counter) + " is : " + str(result) + " ... Critical Failure!")
                    counter += 1 # increment up
                else: # otherwise its just a regular roll
                    theList.append("# " + str(counter) + " is : " + str(result))
                    counter += 1
            else: # if the die is not 20-sided, collect the roll and increment up
                result1 = str(random.randint(1, int(sides)))
                theList.append("# " + str(counter) + " is : " + str(result1))
                counter += 1
        endString = "\n".join(theList)  # joint the list together with newline characters in between
    else: # if there IS a modifier
        score = 0
        for each in range(0, int(quant)):
            if sides == 20: # If it's 20-sided...
                result = random.randint(1, sides)
                score += result
                if result == 20: # and the result is 20... CRITICAL HIT!
                    theList.append("# " + str(counter) + " is : " + str(result) + " ... Critical Success!\n")
                    counter += 1 # increment up
                elif result == 1: # or if the result is 1... CRITICAL MISS!
                    theList.append("# " + str(counter) + " is : " + str(result) + " ... Critical Failure!\n")
                    counter += 1 # increment up
                else: # otherwise its just a regular roll
                    theList.append("# " + str(counter) + " is : " + str(result) + "\n")
                    counter += 1
            else: # if the die is not 20-sided, collect the roll and increment up
                result1 = str(random.randint(1, int(sides)))
                score += int(result1)
                theList.append("# " + str(counter) + " is : " + str(result1) + "\n")
                counter += 1
        score += modifierNum
        theList.append(" plus modifier of " + str(modifierNum)+ " = total: " + str(score) + "\n")
        endString = "\n".join(theList)  # joint the list together with newline characters in between

    # lblH2['text'] = history2
    # lblH1['text'] = history1

    rollList = [endString, history1, history2]
    endResult = "\n".join(rollList)
    # update the current roll and histories
    lbl.insert(0,endResult)

# Current roll
scrollbar = tk.Scrollbar(window)
# scrollbar.grid(row=0,column=6,ipady=50)
scrollbar.pack(side = tk.RIGHT, fill=tk.BOTH)

# Most recent history
# lblH1 = tk.Label(window, text=history1)
# lblH1.grid(column=5, row=1)

# Second most recent history
# lblH2 = tk.Label(window, text=history2)
# lblH2.grid(column=5, row=2)

# dropdown menu for quantity of dice
quantCombo = ttk.Combobox(window)
quantCombo['values'] = (1,2,3,4,5,6,7,8,9,10)
quantCombo.current(0) # set the selected item
# quantCombo.grid(column=0, row=0, sticky=tk.N) # grid placement and 'sticky' qualities
quantCombo.pack(side = tk.LEFT)

# the 'd' in 2d6
d = tk.Label(window, text=" d ")
# d.grid(column=1, row=0, sticky=tk.N)
d.pack(side = tk.LEFT)

# dropdown menu for sides of dice
combo = ttk.Combobox(window)
combo['values'] = ( 2, 4, 6, 8, 10, 12, 20, 100)
combo.current(6)
# combo.grid(column=2, row=0, sticky=tk.N)
combo.pack(side=tk.LEFT)

# This lets the user know what the combobox is for
modLabel = tk.Label(window, text="Modifier")
# modLabel.grid(column=2,row=1, sticky=tk.N+tk.W)
modLabel.pack(side=tk.LEFT)

# Modifier
modifier = ttk.Combobox(window)
modifier['values'] = (-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6)
modifier.current(6)
# modifier.grid(column=0, row=1, sticky=tk.N)
modifier.pack(side=tk.LEFT)

# The roll button
btn = tk.Button(window, text="Roll", command=clicked)
# btn.grid(column=4, row=0, sticky=tk.N)
btn.pack(side=tk.LEFT)

lbl = tk.Listbox(window, bg="white", yscrollcommand=scrollbar.set, width=165)
lbl.pack(side=tk.LEFT, fill=tk.X)
# lbl.grid(column=5, row=0)
lbl.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command = lbl.yview)

# run program
window.mainloop()