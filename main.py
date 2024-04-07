from tkinter import * 

def main():

    WIDTH = 512
    LENGTH = 250

    # Creating a root window for main operations
    root = Tk()

    # root window 
    root.title("Real Estate Collector v1")
    root.geometry(f'{WIDTH}x{LENGTH}')

    # main code
    Label(root, text = 'Please input the name or zip code of your desired location: ', font=('Kannada MW', 17)).place(relx=.5, rely=.05, anchor=N)

    def displayData(textarg):
        Label(root, text=textarg).grid()

    # The following variable would be used for storing the post code or name of city that the user requests
    locationVar = StringVar(root, value = None)
    Entry(root, textvariable=locationVar).place(relx=0.3, rely=0.18)
    
    submitButton = Button(root, text='SUBMIT')
    submitButton.configure(command=lambda: displayData(locationVar.get()))
    submitButton.configure(relief=SUNKEN, padx=1.5, pady=1.5, fg='black', font=('Kannada MW', '12'))
    submitButton.place(relx=0.4, rely=0.3)

    root.mainloop()

if __name__ == '__main__':
    main()
