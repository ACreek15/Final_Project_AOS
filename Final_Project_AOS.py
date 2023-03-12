#This is where I began creating the shape and framework of my GUI
from tkinter import *
import tkinter.messagebox
root = Tk()

#This is the coding used to build the program
Frame = Frame(root, width=300, height=200)
root.title("The Army Ordering System")

#This is the message popup window that prompts the user to know they are entering the software
tkinter.messagebox.showinfo('WARNING!', 'You are entering a United States Army Restricted Program')

#This is the coding I used to create my dropdown menu to close the program
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Close Program", command=exit)

#This is where I defined all of my commands, labels and counts
def exit():
    Frame.quit()

def printPatrolCap():
    print("Patrol Cap")

def printOCPBlouse():
    print("OCP Blouse")

def printOCPPants():
    print("OCP Pants")

def printTacticalBoots():
    print("Tactical Boots")

def delete():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')

count1 = 0
count2 = 0
count3 = 0
count4 = 0

def click1():
    global count1
    count1 += 1
    label_4.config(text=count1)

def click2():
    global count2
    count2 += 1
    label_5.config(text=count2)

def click3():
    global count3
    count3 += 1
    label_6.config(text=count3)

def click4():
    global count4
    count4 += 1
    label_7.config(text=count4)

#This is my coding for my entry boxes
label_1 = Label(root, text="Soldiers Last Name:")
label_1.grid(row=0, sticky=E)
entry_1 = Entry(root)
entry_1.grid(row=0, column=1, sticky=W)

label_2 = Label(root, text="Soldiers ID Number:")
label_2.grid(row=1, sticky=E)
entry_2 = Entry(root)
entry_2.grid(row=1, column=1, sticky=W)

#This is where I begin building my buttons and their functions
enter_button = Button(root, text="Complete Order", command=delete)
enter_button.grid(row=3, column=1)

button1 = Button(text="Patrol Cap", fg="red", command=printPatrolCap)
button1.grid(row=7, column=3)
button1.config(command=click1)

button2 = Button(text="OCP Blouse", fg="blue", command=printOCPBlouse)
button2.grid(row=8, column=3)
button2.config(command=click2)

button3 = Button(text="OCP Pants", fg="green", command=printOCPPants)
button3.grid(row=9, column=3)
button3.config(command=click3)

button4 = Button(text="Tactical Boots", fg="purple", command=printTacticalBoots)
button4.grid(row=10, column=3)
button4.config(command=click4)

exit = Button(text="Sign Out", fg="black", command=Frame.quit)
exit.grid(row=0, column=4, sticky=E)


#This is where I created my labels and counters for the equipment
label_3 = Label(root, text="List of Equipment Added to Soldier's Account")
label_3.grid(row=5, column=1)

label_4 = Label(root, text=count1)
label_4.grid(row=7, column=1)

label_5 = Label(root, text=count2)
label_5.grid(row=8, column=1)

label_6 = Label(root, text=count3)
label_6.grid(row=9, column=1)

label_7 = Label(root, text=count4)
label_7.grid(row=10, column=1)

label_8 = Label(root, text="Patrol Cap")
label_8.grid(row=7, column=1, sticky=W)

label_9 = Label(root, text="OCP Blouse")
label_9.grid(row=8, column=1, sticky=W)

label_10 = Label(root, text="OCP Pants")
label_10.grid(row=9, column=1, sticky=W)

label_11 = Label(root, text="Tactical Boots")
label_11.grid(row=10, column=1, sticky=W)


root.mainloop()