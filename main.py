from tkinter import * 
from tkinter.ttk import Style
import scraping

def main():

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

    basicFrame = Frame(root).pack()
    inputLabel = Label(basicFrame, text = 'Please input the name or zip code of your desired location: ', font=('Kannada MW', 17))
    inputLabel.pack(side=TOP, pady=5)

    # The following variable would be used for storing the post code or name of city that the user requests
    locationVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=locationVar).pack(pady=10)

    # Creating a style variable
    style = Style()
    style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')

    # goofy submit button
    submitButton = Button(basicFrame, text='SUBMIT')
    submitButton.configure(command=lambda: displayData(locationVar.get()))
    submitButton.configure(relief=RAISED, padx=1.5, pady=1.5, font=('Kannada MW', '15'))
    submitButton.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
