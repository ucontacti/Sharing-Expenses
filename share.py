from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from numpy import *
import settlements

# Global and first initiations
GlobalRow = 1
GlobalColumn = 3
master = Tk().title("Sharing Expenses")
Matrices = [[0 for x in range(100)] for y in range(100)]
Persons = []
Expenses = [[0 for x in range(100)] for y in range(2)]

def addPerson():
    #Add a person to expenditures
    global GlobalColumn
    GlobalColumn = GlobalColumn + 1
    e1 = Entry(master, justify=CENTER, font=Texts)
    Persons.append(e1)
    e1.grid(row=0, column=GlobalColumn)
    for i in range(0,GlobalRow):
        Matrices[i][GlobalColumn-3] =  IntVar()
        Checkbutton(master, variable=Matrices[i][GlobalColumn-3]).grid(row=i+1, column=GlobalColumn)
        Matrices[i][GlobalColumn-3].set(1)

def addExpense():
    #Add new expense
    global GlobalRow
    GlobalRow = GlobalRow + 1
    e = Entry(master, justify=CENTER, font=Texts).grid(row=GlobalRow, column=0)
    e = Entry(master, justify=CENTER, font=Texts)
    Expenses[0][GlobalRow-1] = e
    e.grid(row=GlobalRow, column=1)
    e = Entry(master, justify=CENTER, font=Texts)
    Expenses[1][GlobalRow-1] = e
    e.grid(row=GlobalRow, column=2)
    for i in range(0,GlobalColumn-2):
        Matrices[GlobalRow-1][i] = IntVar()
        Checkbutton(master, variable=Matrices[GlobalRow-1][i]).grid(row=GlobalRow, column=i+3)
        Matrices[GlobalRow-1][i].set(1)

def getData():
    #Calculate data and state settlements
    a = [list(map(lambda x: x.get(), x)) for x in array(Matrices)[0:GlobalRow,0:GlobalColumn-2].tolist()]
    if [i for i, x in enumerate(a) if sum(x) == 0]:
        tkinter.messagebox.showwarning('Warning', "There is an expense not shared with anyone.")
        return 0
    b = list(map(lambda x:x.get(),Persons[0:GlobalColumn-2]))
    if True in (p == '' for p in b):
        tkinter.messagebox.showwarning('Warning', "There is an empty field in persons.")
        return 0
    c = [list(map(lambda x: x.get(), x)) for x in array(Expenses)[0:3,0:GlobalRow].tolist()]
    if True in(p == "" for p in c[0]):
        tkinter.messagebox.showwarning('Warning', "There is an empty field in amounts.")
        return 0
    if True in(p == "" for p in c[1]):
        tkinter.messagebox.showwarning('Warning', "There is an empty field in payers.")
        return 0
    if False in(p.isdigit() for p in c[0]):
        tkinter.messagebox.showwarning('Warning', "Amounts should be numbers only.")
        return 0
    Dialoge = settlements.calculateAllocation(a, b, c)
    tkinter.messagebox.showinfo('Settlements', Dialoge)

#Design layout in the main
Header = tkFont.Font(family="Helvetica bold", size=12)
Texts = tkFont.Font(family="Helvetica", size=10)

Label(master, text="Description", font=Header).grid(row=0, column=0)
Label(master, text="Amount", font=Header).grid(row=0, column=1)
Label(master, text="Who Paid?", font=Header).grid(row=0, column=2)

Entry(master, justify=CENTER, font=Texts).grid(row=1, column=0)
e = Entry(master, justify=CENTER, font=Texts)
Expenses[0][0] = e
e.grid(row=1, column=1)
e = Entry(master, justify=CENTER, font=Texts)
Expenses[1][0] = e
e.grid(row=1, column=2)
e = Entry(master, justify=CENTER, font=Texts)
Persons.append(e)
e.grid(row=0, column=3)

Button(master, text="Add Person", justify=CENTER, font=Texts, command=addPerson).grid(row=0, column=100)
Button(master, text="Add Expense", justify=CENTER, font=Texts, command=addExpense).grid(row=100, column=0)
Button(master, text="Calculate", justify=CENTER, font=Header, fg="red", command=getData).grid(row=100, column=100)
Matrices[0][0] = IntVar()
Checkbutton(master, variable=Matrices[0][0]).grid(row=1, column=3)
Matrices[0][0].set(1)

mainloop( )
