# Title:  Training Funds Tracker
# Purpose  To help keep track of funds available for Training
# like a checkbook register. Written in tkinter
# Creator: Shon Garrison
# Created August 2025
# Last Updated August 2025

import tkinter as tk
from tkinter import *
from ttkbootstrap import Style
from tkinter.ttk import Combobox

window = tk.Tk()
window.geometry("841x516")
window.resizable(width=False, height=False)
window.title("Training Funds Tracker")
window.style = Style(theme = "darkly")

# Defined Functions


# Main Window Framework ==========================================


# Input Framework ================================================
txb_Date = tk.Entry(window)
txb_Date.place(x=25,y=105, width=118, height=30)

reasons = ["Enter No.", "ATM", "Debit", "Dep", "Wthdrw", "Trxns"]
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
lbl_Cur_Proj = tk.Label(window, relief="solid")
lbl_Cur_Proj.place(x=25, y=53, width=241, height=30)

lbl_DateID = tk.Label(window, text="Date:")
lbl_DateID.place(x=25, y=84)
lbl_TypeID = tk.Label(window, text="Type/Check No:")
lbl_TypeID.place(x=25, y=144)

lbl_LocationID = tk.Label(window, text="Location:")
lbl_LocationID.place(x=274, y=33)
lbl_Location = tk.Label(window, relief="solid")
lbl_Location.place(x=274, y=53, width=170, height=30)

lbl_StartID = tk.Label(window, text="Start Date:")
lbl_StartID.place(x=476, y=33)
lbl_Start = tk.Label(window, relief="solid")
lbl_Start.place(x=476, y=53, width=103, height=30)

lbl_DirectionID = tk.Label(window, text="->")
lbl_DirectionID.place(x=590, y=60)

lbl_EndID = tk.Label(window, text="End Date:")
lbl_EndID.place(x=617, y=33)
lbl_EndID = tk.Label(window, relief="solid")
lbl_EndID.place(x=617, y=53, width=103, height=30)

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
Bank_Label = tk.Label(window, borderwidth=2, relief="solid")
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
window.mainloop()
print("\nApplication Terminated")
print("Good-bye")

