# Title:  Training Funds Tracker
# Purpose  To help keep track of funds available for Training
# like a checkbook register. Written in tkinter
# Creator: Shon Garrison
# Created August 2025
# Last Updated September 2025

import tkinter as tk
from tkinter import *
from ttkbootstrap import Style
from tkinter.ttk import Combobox
import os
from datetime import date

window = tk.Tk()
window.geometry("841x516")
window.resizable(width=False, height=False)
window.title("Training Funds Tracker")
window.style = Style(theme = "darkly")

today = date.today()   # get current date.  TODO: this may move later in project.

# Defined Functions
def Preview_Calculations():  # may need to enter parameters: reason, ctaken, cearned

    # get floatvar values

    # sets up variables and gets Earned or Taken Values
    bank = gBank
    dte = get_Date()

    print()
    print("Calculating New Daily Balance...")
    print()

    # convert string variables to decimal(float) for calculation
    cearned = float(cearned) * 1.5
    ctaken = float(ctaken)
    newbal = cearned - ctaken
    newbank = newbal + float(bank)
    gBank = str(newbank)

    # convert to back to string to display in label
    newbal = str(newbal)
    newbank = str(newbank)
    print()
    print("Setting Preview of New Balance Applied...")
    print()
    print()

    # shows current preview of time entry prior to writing text file
    print("Total time to enter on affidavit = " + newbal + " hrs\n"
          + "-" * 100 + "\n"
          + "Date" + " " * 18 
          + "Reason" + " " * 16 
          + "Earned" + " " * 18 
          + "Taken" + " " * 17 + "Balance\n"
          + "-" * 10 + " " * 12 + "-" * 10 + " " * 12 
          + "-" * 12 + " " * 12 + "-" * 10
          + " " * 12 + "-" * 10 + "\n" 
          + str(dte) + " " * 12 
          + reason + " " * 12
          + str(cearned) + " " * 21 
          + str(ctaken) + " " * 19
          + newbank + "\n"
          + "-" * 100) 
    print()

    # What gets put into run file on applying calc
    gPreview = (str(dte) + " " * 7 
                + reason + " " * 6 
                + str(cearned)
                + " " * 19 
                + str(ctaken) + " " * 17
                + newbank + "\n"
                + "-" * 100 + "\n")
    

def Apply_Calculations():
    
    # get floatvar values

    print()
    print("Applying New Daily Balance to Bank...")
    print()

    # incorporate to opening file
    bank2 = float(gBank)
    newDaybal = float(gDaily_Bank)  # get daily balance text
    newbank2 = float(newDaybal) + bank2

    gBank = (str(newbank2))  # update global variable with new balance
    newbank2 = str(newbank2)  # convert to string to put into label and file

    # writes to runfile
    f2 = open("D:\Temp/test2.txt", "a")
    f2.write(gPreview)
    f2.close()

def Ready_Form():
    pass

def Reconcile():
    pass

def Separation():
    pass

def New_Training():   
    
    # Training Inforamtion Form to be passed to main form 
    trainingID_Window = Toplevel(window)
    trainingID_Window.title("Training Tracker Basic Info")
    trainingID_Window.resizable(width=False, height=False)
    trainingID_Window.geometry("387x312")

    lbl_TrainingName = tk.Label(trainingID_Window, text="Training Name:")
    lbl_TrainingName.place(x=27,y=42)
    lbl_TrainingLocation = tk.Label(trainingID_Window, text="Location:")
    lbl_TrainingLocation.place(x=27,y=79)
    lbl_TrainingStart = tk.Label(trainingID_Window, text="Start Date:")
    lbl_TrainingStart.place(x=27,y=130)
    lbl_TrainingEnd = tk.Label(trainingID_Window, text="End Date:")
    lbl_TrainingEnd.place(x=27,y=171)
    
    txt_TrainingEntry = tk.Entry(trainingID_Window)
    txt_TrainingEntry.config(font="Calibri, 12", fg="#EEF2F5")
    txt_TrainingEntry.place(x=125,y=34, width=221,height=26)
    txt_TrainingLoc = tk.Entry(trainingID_Window)
    txt_TrainingLoc.config(font="Calibri, 12", fg="#EEF2F5")
    txt_TrainingLoc.place(x=125,y=74, width=199,height=26)
    txt_TrainingStart = tk.Entry(trainingID_Window)
    txt_TrainingStart.config(font="Calibri, 12", fg="#EEF2F5")
    txt_TrainingStart.place(x=125,y=122, width=122,height=26)
    txt_TrainingEnd = tk.Entry(trainingID_Window)
    txt_TrainingEnd.config(font="Calibri, 12", fg="#EEF2F5")
    txt_TrainingEnd.place(x=125,y=163, width=122,height=26)

    btn_Submit= tk.Button(trainingID_Window, text="Submit", command=lambda: update_labels(txt_TrainingEntry.get(), 
                                                                                          txt_TrainingLoc.get(), 
                                                                                          txt_TrainingStart.get(), 
                                                                                          txt_TrainingEnd.get()))
    btn_Submit.place(x=27,y=250, width=91,height=40)  
    btn_Done = tk.Button(trainingID_Window, text="Done", command=trainingID_Window.destroy)
    btn_Done.place(x=267,y=250, width=91,height=40) 

def update_labels(nam_val, loc_val, std_val, end_val):
    trainingName.set(nam_val)
    trainingLoc.set(loc_val)
    trainingStd.set(std_val)
    trainingEnd.set(end_val)


# Main Window Framework ==========================================

# Input Framework ================================================
trainingName = StringVar()
trainingLoc = StringVar()
trainingStd = StringVar()
trainingEnd = StringVar()
gbank = DoubleVar()
gpreview = DoubleVar()

txb_Date = tk.Entry(window)
txb_Date.place(x=25,y=105, width=118, height=30)

reasons = ["Enter No.", "ATM", "Debit", "Credit", "Deposit", "Wthdrw", "Trxns"]
cmb_Type = Combobox(window, values = reasons, width=15)
cmb_Type.current(0)
cmb_Type.place(x=25, y=167)

txb_Pay = tk.Entry(window)
txb_Pay.place(x=157,y=167, width=300, height=30)
txb_Debit = tk.Entry(window) 
txb_Debit.place(x=479,y=167, width=74, height=30)
txb_Credit = tk.Entry(window)
txb_Credit.place(x=567,y=167, width=74, height=30)

# Output Framework ===============================================
lbl_Cur_ProjID = tk.Label(window, text="Current Training:")
lbl_Cur_ProjID.place(x=25, y=33)
lbl_Cur_Proj = tk.Label(window, relief="solid", textvariable=trainingName)
lbl_Cur_Proj.config(font="Calibri, 12", fg="#66B2FF")  
lbl_Cur_Proj.place(x=25, y=53, width=241, height=30)

lbl_LocationID = tk.Label(window, text="Location:")
lbl_LocationID.place(x=274, y=33)
lbl_Location = tk.Label(window, relief="solid", textvariable=trainingLoc)
lbl_Location.config(font="Calibri, 12", fg="#66B2FF")
lbl_Location.place(x=274, y=53, width=170, height=30)

lbl_StartID = tk.Label(window, text="Start Date:")
lbl_StartID.place(x=476, y=33)
lbl_Start = tk.Label(window, relief="solid", textvariable=trainingStd)
lbl_Start.config(font="Calibri, 12", fg="#66B2FF")
lbl_Start.place(x=476, y=53, width=103, height=30)

lbl_DirectionID = tk.Label(window, text="->")
lbl_DirectionID.place(x=590, y=60)

lbl_EndID = tk.Label(window, text="End Date:")
lbl_EndID.place(x=617, y=33)
lbl_End = tk.Label(window, relief="solid", textvariable=trainingEnd)
lbl_End.config(font="Calibri, 12", fg="#66B2FF")
lbl_End.place(x=617, y=53, width=103, height=30)

lbl_DateID = tk.Label(window, text="Date:")
lbl_DateID.place(x=25, y=84)
lbl_TypeID = tk.Label(window, text="Type/Check No:")
lbl_TypeID.place(x=25, y=144)
lbl_PayID = tk.Label(window, text="Pay to the Order Of:")
lbl_PayID.place(x=154, y=144)
lbl_DebitID = tk.Label(window, text="Debit(-):")
lbl_DebitID.place(x=476, y=144)
lbl_CreditID = tk.Label(window, text="Credit(+):")
lbl_CreditID.place(x=564, y=144)
lbl_BankID = tk.Label(window, text="Bank:")
lbl_BankID.place(x=701, y=101)
lbl_Operator = tk.Label(window, text="(+/-)", font="Calibri, 16")
lbl_Operator.place(x=647, y=166)
lbl_PreviewID = tk.Label(window, text="Preview of Current Transaction:")
lbl_PreviewID.place(x=25, y=251)

# Bank Process of Transaction -------------------------------------
Bank_Label = tk.Label(window, borderwidth=2, relief="solid", textvariable=gbank)
Bank_Label.config(font="Calibri, 12", fg="#EEF2F5")
Bank_Label.place(x=703,y=128, width=100, height=30)

Trans_Label = tk.Label(window, borderwidth=2, relief="solid")
Trans_Label.place(x=703,y=167, width=100, height=30)

lbl_Line = tk.Label(window, text="___________________")
lbl_Line.place(x=703, y=198, width=100, height=15)

Results_Label = tk.Label(window, borderwidth=2, relief="solid")
Results_Label.place(x=703,y=225, width=100, height=30)

# Preview Transaction --------------------------------------------
Prev_Label = tk.Label(window, borderwidth=2, relief="solid")          
Prev_Label.place(x=25,y=274, width=791, height=113 )

# Button Framework ===============================================
btn_Info = tk.Button(window, text="Info", command=New_Training)
btn_Info.place(x=25,y=8, width=86,height=15)
btn_Clear = tk.Button(window, text = "Clear", command=lambda: print("Clear Button was pressed"))
btn_Clear.place(x=25, y=420, width=86, height=41)
btn_Calc = tk.Button(window, text = "Calculate", command=lambda: print("Calculate Button was pressed"))
btn_Calc.place(x=186, y=420, width=86, height=41)
btn_Apply = tk.Button(window, text = "Apply", command=lambda: print("Apply Button was pressed"))
btn_Apply.place(x=366, y=420, width=86, height=41)
btn_Reconcile = tk.Button(window, text = "Reconcile", command=lambda: print("Reconcile Button was pressed"))
btn_Reconcile.place(x=546, y=420, width=86, height=41)
btn_Close = tk.Button(window, text = "Close", command=window.destroy)
btn_Close.place(x=730, y=420, width=86, height=41)


# Run Application ================================================
if os.path.isdir("D:/Temp") and os.path.isfile("D:/Temp/test2.txt"):
    f = open("D:/Temp/test2.txt", "r")
    my_list = []
    for line in f:
        for char in line:
            if char[-1] == "\n" and line.__contains__("."):
                t = float(line[-7:-1].lstrip(" "))
                my_list.append(t)
    gBank = my_list[-1]
    f.close()

else:
    # if bank file doesn't exist, it creates it with a 0.0 balance then
    # reads from it.
    startBal = "0.00"
    gBank = float(startBal)

    # Creates running file skeleton
    f = open("D:/Temp/test2.txt", "w")
    f.write("Orange County Juvenile Probation Dept\n"
            + "-" * 40 + "\n"
            + "Personal Comptime Sheet for: Shon Garrison\n"
            + "\n"
            + "Date" + " " * 13 
            + "Reason" + " " * 11 
            + "Earned" + " " * 16 
            + "Taken" + " " * 15 
            + "New Balance\n"
            + "-" * 9 + " " * 7 + "-" * 12 
            + " " * 6 + "-" * 7 + " " * 15
            + "-" * 6 + " " * 14 + "-" * 12 + "\n")
    f.close()

window.mainloop()
print("\nApplication Terminated")
print("Good-bye")

