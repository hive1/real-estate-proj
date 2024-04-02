from tkinter import * 

def main():
    WIDTH = 1024
    LENGTH = 500

    # Creating a root window for main operations
    root = Tk()

    # root window 
    root.title("Input Data")
    root.geometry(f'{WIDTH}x{LENGTH}')

    # main code
    loc = Label(root, text = 'Please input either the postal code or the name of desired city: ', font=('Kannada MW', 17))
    loc.pack()

    entry = Entry(root)
    entry.pack()



    root.mainloop()

if __name__ == '__main__':
    main()
