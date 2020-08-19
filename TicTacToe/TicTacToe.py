import sys
import os
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox as mb

window = tk.Tk()
window.title("Tic Tac Toe by psjpark")

window.rowconfigure([0, 1, 2], minsize=100, weight=1)
window.columnconfigure([0, 1, 2], minsize=100, weight=1)

current_player = "O"
btn_font = font.Font(size=30)

btn_0x0 = tk.Button(master=window, command=lambda: mark(btn_0x0), font=btn_font)
btn_0x0.grid(row=0, column=0, sticky="nsew")

btn_0x1 = tk.Button(master=window, command=lambda: mark(btn_0x1), font=btn_font)
btn_0x1.grid(row=0, column=1, sticky="nsew")

btn_0x2 = tk.Button(master=window, command=lambda: mark(btn_0x2), font=btn_font)
btn_0x2.grid(row=0, column=2, sticky="nsew")

btn_1x0 = tk.Button(master=window, command=lambda: mark(btn_1x0), font=btn_font)
btn_1x0.grid(row=1, column=0, sticky="nsew")

btn_1x1 = tk.Button(master=window, command=lambda: mark(btn_1x1), font=btn_font)
btn_1x1.grid(row=1, column=1, sticky="nsew")

btn_1x2 = tk.Button(master=window, command=lambda: mark(btn_1x2), font=btn_font)
btn_1x2.grid(row=1, column=2, sticky="nsew")

btn_2x0 = tk.Button(master=window, command=lambda: mark(btn_2x0), font=btn_font)
btn_2x0.grid(row=2, column=0, sticky="nsew")

btn_2x1 = tk.Button(master=window, command=lambda: mark(btn_2x1), font=btn_font)
btn_2x1.grid(row=2, column=1, sticky="nsew")

btn_2x2 = tk.Button(master=window, command=lambda: mark(btn_2x2), font=btn_font)
btn_2x2.grid(row=2, column=2, sticky="nsew")

all_btn = (btn_0x0, btn_0x1, btn_0x2, btn_1x0, btn_1x1, btn_1x2, btn_2x0, btn_2x1, btn_2x2)

row_1 = (btn_0x0, btn_0x1, btn_0x2)
row_2 = (btn_1x0, btn_1x1, btn_1x2)
row_3 = (btn_2x0, btn_2x1, btn_2x2)
row_4 = (btn_0x0, btn_1x0, btn_2x0)
row_5 = (btn_0x1, btn_1x1, btn_2x1)
row_6 = (btn_0x2, btn_1x2, btn_2x2)
row_7 = (btn_0x0, btn_1x1, btn_2x2)
row_8 = (btn_2x0, btn_1x1, btn_0x2)
all_row = (row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8)


def switch_player():
    global current_player
    if current_player == "O":
        current_player = "X"
    else:
        current_player = "O"


def mark(button):
    button["text"] = current_player
    button["state"] = "disabled"
    check_bingo()
    check_draw()
    switch_player()


def check_bingo():
    bingo = False
    for r in all_row:
        chk = []
        for b in r:
            if b["text"] == "O":
                chk.append(1)
            elif b["text"] == "X":
                chk.append(9)
        if sum(chk) == 3 or sum(chk) == 27:
            bingo = True
    if bingo:
        draw_ok = mb.showinfo("GG", f"Player {current_player} won!")
        if draw_ok == 'ok':
            restart_program()


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def check_draw():
    btn_state = []
    for n in all_btn:
        btn_state.append(n["state"] == "disabled")
    if all(btn_state):
        draw_ok = mb.showinfo("GG", "Draw")
        if draw_ok == 'ok':
            restart_program()


window.mainloop()

