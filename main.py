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
    loc = Label(root, text = 'Please input either the postal code or the name of the city', font=('Times New Roman', 17, 'bold'))

    loc.grid(column = 50, row = 5)
    root.mainloop()

if __name__ == '__main__':
    main()
