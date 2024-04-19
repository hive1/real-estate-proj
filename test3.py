import tkinter
from PIL import Image, ImageTk
from scraping import scrapeData
from functions import findAvg, next, back
from tkinter.ttk import Button, Style

root = tkinter.Tk()
root.geometry('800x600')

style = Style()
style.configure('W.TButton', font = ('calibri', 12), borderwidth = '4')

# Changes will be reflected by the movement of mouse
style.map('W.TButton', foreground = ['active', '!disabled', 'green'],
                        background = [('active', 'black')])

next_button = Button(root, text = "next", style = 'W.TButton')
next_button.place(relx = 0.37, rely = .1, anchor='center')
back_button = Button(root, text = "back", style = 'W.TButton')
back_button.place(relx = 0.27, rely = .1, anchor='center')

root.mainloop()