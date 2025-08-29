# Title:  Training Funds Tracker
# Purpose  To help keep track of funds available for Training
# like a checkbook register. Written in tkinter
# Creator: Shon Garrison
# Created August 2025
# Last Updated August 2025

import tkinter as tk
from tkinter import *
from ttkbootstrap import Style


window = tk.Tk()
window.geometry("841x516")
window.resizable(width=False, height=False)
window.title("Training Funds Tracker")
window.style = Style(theme = "darkly")

# Defined Functions


# Main Window Framework ==========================================


# Input Framework ================================================


# Output Framework ===============================================
lbl_Cur_ProjID = tk.Label(window, text="Current Project:")
lbl_Cur_ProjID.place(x=25, y=33)
lbl_DateID = tk.Label(window, text="Date:")
lbl_DateID.place(x=25, y=84)
lbl_TypeID = tk.Label(window, text="Type/Check No:")
lbl_TypeID.place(x=25, y=144)
lbl_LocationID = tk.Label(window, text="Location:")
lbl_LocationID.place(x=274, y=33)
lbl_StartID = tk.Label(window, text="Start Date:")
lbl_StartID.place(x=476, y=33)
lbl_EndID = tk.Label(window, text="End Date:")
lbl_EndID.place(x=617, y=33)
lbl_PayID = tk.Label(window, text="Pay to the Order Of:")
lbl_PayID.place(x=154, y=144)
lbl_DebitID = tk.Label(window, text="Debit(-):")
lbl_DebitID.place(x=476, y=144)
lbl_CreditID = tk.Label(window, text="Credit(+):")
lbl_CreditID.place(x=564, y=144)
lbl_BankID = tk.Label(window, text="Bank:")
lbl_BankID.place(x=701, y=101)
lbl_Line = tk.Label(window, text="________", font="Calibri, 16")
lbl_Line.place(x=703, y=175)
lbl_Operator = tk.Label(window, text="(+/-)", font="Calibri, 16")
lbl_Operator.place(x=647, y=166)
lbl_PreviewID = tk.Label(window, text="Preview of Current Transaction:")
lbl_PreviewID.place(x=25, y=251)
Prev_Label = tk.Label(window, borderwidth=2, relief="solid")          
Prev_Label.place(x=25,y=274, width=791, height=113 )
Bank_Label = tk.Label(window, borderwidth=2, relief="solid")
Bank_Label.place(x=703,y=122, width=100, height=23)
Trans_Label = tk.Label(window, borderwidth=2, relief="solid")
Trans_Label.place(x=703,y=162, width=100, height=23)
Results_Label = tk.Label(window, borderwidth=2, relief="solid")
Results_Label.place(x=703,y=210, width=100, height=23)

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

