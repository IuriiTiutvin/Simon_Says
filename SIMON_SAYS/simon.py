from tkinter import *
import random
import time

def menu():
    master.geometry("180x170")
    clear()
    play_button = Button(master, width=20, height=5, text='Play', command=lambda:play())
    rules_button = Button(master, width=20, height=5, text='Rules', command=lambda:rules())
    play_button.grid(row=0, column=0)
    rules_button.grid(row=1, column=0)

def play():
    global t
    global level
    global pattern
    global mistakes
    t = 1.00
    level = 1
    pattern = []
    mistakes = 0
    master.geometry("213x330")
    buttons()
    disable()
    engine()

def buttons():
    global mistakes
    global t
    clear()
    red_button.grid(row=0, column=0)
    green_button.grid(row=0, column=1)
    blue_button.grid(row=1, column=0)
    yellow_button.grid(row=1, column=1)
    messanger.grid(row=2, column=0, columnspan=2)
    messanger.insert('1.0', '>Pay attention to messages\n')
    return_button.grid(row=3, column=0, columnspan=2)
    master.update()
    time.sleep(3)
    messanger.insert('1.0', f'>You have {3-mistakes} lives\n')
    master.update()
    time.sleep(1.5)

def engine():
    master.update()
    if mistakes < 3:
        messanger.insert('1.0', f'>Wait for the pattern...\n')
        master.update()
        time.sleep(2)
        for i in range(level):
            number = random.randint(1, 4)
            pattern.append(number)
            print(pattern)
            light(number, t)
        messanger.insert('1.0', f'>Repeat the pattern...\n')
        enable()

def user(num):
    disable()
    global t
    global level
    global mistakes
    global pattern
    if pattern[0] == num:
        del pattern[0]
        light(num, 0.5)
        enable()
    else:
        mistakes += 1
        messanger.insert('1.0', f'>You failed!\n')
        master.update()
        time.sleep(1)
        messanger.insert('1.0', f'>You have {3-mistakes} lives left\n')
        master.update()
        time.sleep(2)
        pattern = []
        engine()
        if mistakes == 3:
            clear()
            master.geometry("200x170")
            messanger2.grid(row = 0, column = 0)
            messanger2.insert('1.0', '>Great Job!!\n')
            messanger2.insert('1.0', f'>You beat {level-1} levels!\n')
            back_button.grid(row = 1, column=0)


    if pattern == []:
        messanger.insert('1.0', f'>Good job!\n')
        master.update()
        time.sleep(1)
        messanger.insert('1.0', f'>You beat level {level}\n')
        level += 1
        master.update()
        time.sleep(1)
        if t > 0.60:
            t = t - 0.02
        colors(t)
        disable()
        engine()

def colors(wait):
    global t
    red_button.config(image=red)
    green_button.config(image=green)
    blue_button.config(image=blue)
    yellow_button.config(image=yellow)
    master.update()
    if wait == 0.5:
        time.sleep(0.20)
    else:
        time.sleep(wait)

def light(num, wait):
    global t
    if num == 1:
        red_button.config(image=active_red)
    elif num == 2:
        green_button.config(image=active_green)
    elif num == 3:
        blue_button.config(image=active_blue)
    elif num == 4:
        yellow_button.config(image=active_yellow)
    master.update()
    time.sleep(wait)
    colors(wait)


def disable():
    red_button.config(state=DISABLED)
    green_button.config(state=DISABLED)
    blue_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)

def enable():
    red_button.config(state=NORMAL)
    green_button.config(state=NORMAL)
    blue_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)

def rturn():
    global z
    global level
    global mistakes
    global pattern
    global t
    z += 1
    if z == 1:
        messanger.insert('1.0', '\ns')
        messanger.insert('1.0', f'>If you leave, you will lose all progress\n')
        messanger.insert('1.0', f'>Press the button again to leave\n')
    else:
        clear()
        t = 1.00
        level = 1
        mistakes = 0
        pattern = []
        menu()

def rules():
    clear()
    master.geometry("180x200")
    message.grid(row=0, column=0)
    back_button.grid(row=1, column=0)

def clear():
    for widget in master.winfo_children():
        widget.grid_forget()


if __name__ == '__main__':
    level = 1
    mistakes = 0
    pattern = []
    t = 1.00
    z = 0

    master = Tk()
    master.geometry("180x170")
    #master.resizable(False, False)
    master.title("Simon")

    red = PhotoImage(file='red.gif')
    green = PhotoImage(file='green.gif')
    blue = PhotoImage(file='blue.gif')
    yellow = PhotoImage(file='yellow.gif')
    active_red = PhotoImage(file='active_red.gif')
    active_green = PhotoImage(file='active_green.gif')
    active_blue = PhotoImage(file='active_blue.gif')
    active_yellow = PhotoImage(file='active_yellow.gif')

    red_button = Button(master, width=103, height=103, image=red, command=lambda:user(1))
    green_button = Button(master, width=103, height=103, image=green, command=lambda:user(2))
    blue_button = Button(master, width=103, height=103, image=blue, command=lambda:user(3))
    yellow_button = Button(master, width=103, height=103, image=yellow, command=lambda:user(4))


    message = Label(master, height=7, width=20, text='''When you press play
colors will light up
in different order.
You must repeat the
pattern to win.
You will lose after
three mistakes.''')
    back_button = Button(master, width=20, height=5,text='Back', command=lambda:menu())
    messanger = Text(master, width=28, height=5)
    messanger2 = Text(master, width=28, height=5)
    return_button = Button(master, width=10, height=2, text='Back', command=lambda:rturn())

    menu()
    master.mainloop()
