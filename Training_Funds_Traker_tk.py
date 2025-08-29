# Title:  Training Funds Tracker
# Purpose  To help keep track of funds available for Training
# like a checkbook register. Written in tkinter
# Creator: Shon Garrison
# Created August 2025
# Last Updated August 2025

import tkinter as tk
from tkinter import ttk
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
lbl_Line = tk.Label(window, text="__________", font="Calibri, 16")
lbl_Line.place(x=695, y=182)
lbl_Operator = tk.Label(window, text="(+/-)", font="Calibri, 16")
lbl_Operator.place(x=647, y=166)
label1 = tk.Label(window, text="Preview of Current Transaction:")
label1.place(x=25, y=251)
Prev_Label = tk.Text(window, bg="#DAD4D4")  # TODO: Check for text or label for this fill
Prev_Label.place(x=25,y=272, width=791, height=113 )

# Button Framework ===============================================
button = tk.Button(window, text = "Clear", command=lambda: print("Clear Button was pressed"))
button.place(x=25, y=420, width=86, height=41)
button1 = tk.Button(window, text = "Calculate", command=lambda: print("Calculate Button was pressed"))
button1.place(x=186, y=420, width=86, height=41)
button2 = tk.Button(window, text = "Apply", command=lambda: print("Apply Button was pressed"))
button2.place(x=366, y=420, width=86, height=41)
button3 = tk.Button(window, text = "Reconcile", command=lambda: print("Reconcile Button was pressed"))
button3.place(x=546, y=420, width=86, height=41)
button4 = tk.Button(window, text = "Close", command=window.destroy)
button4.place(x=730, y=420, width=86, height=41)


# Run Application ================================================
window.mainloop()
print("\nApplication Terminated")
print("Good-bye")

