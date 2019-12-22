#import tkinter modules
from tkinter import * 
from tkinter import  messagebox
import tkinter as tk
#creating main tkinter window
tk = Tk()
tk.title("Tic Tac Toe Tkinter") #window title

#SringVar() Holds a string; default value
playera = StringVar()
playerb=StringVar()
p1= StringVar()
p2= StringVar()

#building the player dashboard
player1_name = Entry(tk, textvariable = p1, bd = 5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable = p2, bd = 5)
player2_name.grid(row = 2, column=1, columnspan = 8)

label = Label(tk, text = " Player 1:", font='Times 15 bold', bg='grey', fg='black', height=1, width=8)
label.grid(row=1 , column= 0)
         
label = Label(tk, text = " Player 2:", font='Times 15 bold', bg='grey', fg='black', height=1, width=8)
label.grid(row=2 , column= 0)


#button configurations.
buttonclick = True
counter = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
 
    
def btnClick(buttons):
    global buttonclick,flag,player1_name, player2_name,playera,playerb
    if len(p1.get()) == 0:
        messagebox.showinfo("Tic Tac Toe Tkinter", "Enter Name for Player 1")
    elif len(p2.get()) == 0:
        messagebox.showinfo("Tic Tac Toe Tkinter", "Enter Name for Player 2")
    elif buttons["text"] == " " and buttonclick == True:
        buttons["text"] = "X"
        buttonclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        ApplyWinRule()
        counter +=1
    elif buttons["text"] == " " and buttonclick == False:
        buttons["text"] ="O"
        buttonclick = True
        ApplyWinRule()
        counter +=1
    else:
        messagebox.showinfo("Tic Tac Toe Tkinter", "This Button is already clicked.")

#making the rules to determine or check for wins.
def ApplyWinRule():
     if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        messagebox.showinfo("Tic Tac Toe Tkinter", playera)
     elif(flag == 8):
        messagebox.showinfo("Tic Tac Toe Tkinter", "It is a Tie")
     elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
        button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        messagebox.showinfo("Tic Tac Toe Tkinter",playerb)
        

#configuring buttons to build the actual tic tac toe game outlook
button1 = Button(tk, text=" ", font='Times 20 bold', bg='yellow', fg='black', height=4, width=8, command = lambda: btnClick(button1))
button1.grid(row=3, column=0) #position of button1.

button2 = Button(tk, text=" ", font='Times 20 bold', bg='yellow', fg='black', height=4, width=8, command = lambda: btnClick(button2))
button2.grid(row=3, column=1) #position of button2.

button3 = Button(tk, text=" ", font='Times 20 bold', bg='yellow', fg='black', height=4, width=8, command = lambda: btnClick(button3))
button3.grid(row=3, column=2) #position of button3.

button4 = Button(tk, text=' ', font='Times 20 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0) #position of button4.

button5 = Button(tk, text=' ', font='Times 20 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1) #position of button5.

button6 = Button(tk, text=' ', font='Times 20 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2) #position of button6.

button7 = Button(tk, text=' ', font='Times 20 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0) #position of button7.

button8 = Button(tk, text=' ', font='Times 20 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1) #position of button8.

button9 = Button(tk, text=' ', font='Times 20 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2) #position of button9.



tk.mainloop()
