from tkinter import * 
from tkinter.ttk import Style
from scraping import scrapeData

def main():

    # tests

    WIDTH = 512
    LENGTH = 250

    # Creating a root window for main operations
    root = Tk()

    # Stops the window from being resizable
    root.resizable(0, 0)

    # root window 
    root.title("Real Estate Collector v1")
    root.geometry(f'{WIDTH}x{LENGTH}')

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

    (prices, addresses, baths, baths, avg) = scrapeData(locationVar.get())

    root = Tk()
    root.geometry('1600x800')
    root.title('Real Estate Data')

    '''lowkey a majority of my code was overwritten by some headass commit issues'''

    root.mainloop()


if __name__ == '__main__':
    main()
