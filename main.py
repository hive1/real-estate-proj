from tkinter import * 

def main():

    WIDTH = 512
    LENGTH = 250

    # Creating a root window for main operations
    root = Tk()

    # root window 
    root.title("Real Estate Collector v1")
    root.geometry(f'{WIDTH}x{LENGTH}')

    def displayData(textarg):
        Label(basicFrame, text=textarg).pack()

    basicFrame = Frame(root).pack()
    inputLabel = Label(basicFrame, text = 'Please input the name or zip code of your desired location: ', font=('Kannada MW', 17))
    inputLabel.pack(side=TOP)

    # The following variable would be used for storing the post code or name of city that the user requests
    locationVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=locationVar).pack()
    
    # goofy submit button
    submitButton = Button(basicFrame, text='SUBMIT')
    submitButton.configure(command=lambda: displayData(locationVar.get()))
    submitButton.configure(relief=SUNKEN, padx=1.5, pady=1.5, font=('Kannada MW', '12'))
    submitButton.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
