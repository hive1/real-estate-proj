from tkinter import * 
from tkinter.ttk import Style
from PIL import Image, ImageTk
import requests
import json
#from scraping import scrapeData
from functions import findAvg

def main():

    InpWidth = 512
    InpHeight = 250

    # Creating a root window for main operations
    root = Tk()

    # Stops the window from being resizable
    root.resizable(0, 0)

    # root window 
    root.title("Real Estate Collector v1")
    root.geometry(f'{InpWidth}x{InpHeight}')

    def displayData(textarg):
        Label(basicFrame, text=textarg).pack()
        root.destroy()

    basicFrame = Frame(root).pack()
    inputLabel = Label(basicFrame, text = 'Please input the name or zip code of your desired location: ', font=('Kannada MW', 14))
    inputLabel.pack(side=TOP, pady=5, padx=5)

    # The following variable would be used for storing the post code or name of city that the user requests
    locationVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=locationVar).pack(pady=10)

    # Creating a style variable
    # style = Style()
    # style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')

    # goofy submit button
    submitButton = Button(basicFrame, text='SUBMIT')
    submitButton.configure(command=lambda: displayData(locationVar.get()))
    submitButton.configure(relief=RAISED, padx=1.5, pady=1.5, font=('Kannada MW', '12'))
    submitButton.pack()

    root.mainloop()

    # Collecting data from the backend
    prices = []
    addresses = []
    beds = []
    baths = []
    avg = None

    (prices, addresses, beds, baths, avg) = scrapeData(locationVar.get())

    root = Tk() 

    disWidth = 1600
    disHeight = 800
    root.geometry(f'{disWidth}x{disHeight}')
    root.title('Real Estate Data')

    '''starting the construction of the average frame to the right of the screen'''
    average = Frame(root, 
                    height = (disHeight-20), 
                    width = (disWidth/5), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    average.pack(side='right', padx=30, pady=30)
    info = Frame(root, 
                    height = (disHeight-20), 
                    width = (disWidth-(disWidth/5+30)), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    info.pack(side='left', padx=30, pady=30)
    avgHead = Label(average, 
                    text = 'Averages',
                    font = ('Fixedsys', 25))
    avgHead.place(relx = 0.5, rely = 0.05, anchor = 'center')

    textAvg = Text(average,
                   height = 45,
                   width = 30,
                   font = ('Fixedsys', 12)) # this value specifically keeps turning into a str and idk why
    textAvg.place(relx = .5, rely = .5, anchor='center')
    textAvg.insert(END, beds)


    root.mainloop()


if __name__ == '__main__':
    main()
