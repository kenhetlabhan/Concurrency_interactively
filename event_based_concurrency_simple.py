
from tkinter import *
from tkinter import messagebox

def main_window(root: Tk):
    frame = Frame(root)
    frame.pack()
    Button_1 = Button(frame, text="Button 1", command=show_button_1)#the event handler. When an event takes place, namely you click the button it runs the function show_button().
    Button_1.pack(side=LEFT)
    Button_2 = Button(frame, text="Button 2 ", command=show_button_2)
    Button_2.pack(side=LEFT)
def show_button_2():
    messagebox.showinfo("PP", "Clicking on this button is a different event. Therefore it has a different event handler and thus produces a different text on your screen then button 1.")

def show_button_1():
    messagebox.showinfo("Button 1.","This program uses an event loop and waits for an event, like clicking on this button. After you've exited this button the loop will continue and the program will wait for the next event. ")
if __name__ == "__main__":
    root = Tk()
    root.title("Event Loop Window")
    root.geometry('600x500')
    main_window(root)
    root.mainloop()
