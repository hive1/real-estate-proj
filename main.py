from tkinter import * 

def main():

    WIDTH = 1024
    LENGTH = 500

    # Creating a root window for main operations
    root = Tk()

    # root window 
    root.title("Input Data")
    root.geometry(f'{WIDTH}x{LENGTH}')

    # useless quit button
    Button(root, text='leave!!', command=root.quit).place(relx=.05, rely=.05, anchor=NW)

    # main code
    Label(root, text = 'Please input either the postal code or the name of desired city: ', font=('Kannada MW', 17)).place(relx=.5, rely=.05, anchor=N)

    def displayData(textarg):
        Label(root, text=textarg).grid()

    # The following variable would be used for storing the post code or name of city that the user requests
    locationVar = StringVar(root, value = None)
    Entry(root, textvariable=locationVar).grid()
    

    # submitButton = Button(root, text='submit', command=lambda: displayData(locationVar.get()))
    # submitButton.grid()

    root.mainloop()

if __name__ == '__main__':
    main()
