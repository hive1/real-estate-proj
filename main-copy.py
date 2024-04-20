from tkinter import * 
from tkinter.ttk import Style
from PIL import Image, ImageTk
import requests
import json

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
    inputLabel = Label(basicFrame, text = 'Please input the zip code of your desired location: ', font=('Kannada MW', 14))
    inputLabel.pack(side=TOP, pady=5, padx=5)

    # The following variable would be used for storing the post code or name of city that the user requests
    locationVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=locationVar).pack(pady=10)

    # goofy submit button
    submitButton = Button(basicFrame, text='SUBMIT')
    submitButton.configure(command=lambda: displayData(locationVar.get()))
    submitButton.configure(relief=RAISED, padx=1.5, pady=1.5, font=('Kannada MW', '12'))
    submitButton.pack()

    root.mainloop()

    # Collecting data from the backend
    images = ["https://ssl.cdn-redfin.com/photo/269/islphoto/605/genIslnoResize.3540605_0.jpg"]
    prices = ["$5,000,000"]
    addresses = ["190 My Balls"]
    beds = ["10 beds"]
    baths = ["3 baths"]
    sqft = ["2382389 sq ft"]
    acres = ["4.0 acres"]
    avg = None

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
                   height = 35,
                   width = 28,
                   font = ('Fixedsys', 15)) # this value specifically keeps turning into a str and idk why
    textAvg.place(relx = .5, rely = .55, anchor='center')
    textAvg.insert(END, 'Average price: $500000')
    textAvg.insert(END, 'Average beds: 2 beds\n')
    textAvg.insert(END, 'Average baths: 10 baths\n')
    textAvg.config(state = DISABLED)
    
    textInfo = Text(info,
                   height = 15,
                   width = 95,
                   font = ('Fixedsys', 15))
    textInfo.place(relx = 0.5, rely = 0.8, anchor='center')

    # making everything 
    style = Style()
    style.configure('W.TButton', font = ('calibri', 14, 'bold', 'underline'), foreground = 'blue')

    '''House Image Shit'''
    url = images[0]
    image = Image.open(requests.get(url, stream=True).raw)
    photo = ImageTk.PhotoImage(image)
    house_image = Canvas(info, width=640/1.2, 
            height=460/1.2)
    house_image.create_image(320/1.2,230/1.2, image=photo)
    house_image.image = photo
    house_image.place(relx = 0.29, rely = .303, anchor='center')

    '''Info Textbox'''
    textInfo.insert(END,prices[0])
    textInfo.insert(END,"\n"+addresses[0])
    textInfo.insert(END,"\n"+beds[0])
    textInfo.insert(END,"\n"+baths[0])
    textInfo.insert(END,"\n"+sqft[0])
    textInfo.insert(END,"\n"+acres[0])

    '''Next & Back Buttons'''
    next_button=Button(text="next")
    next_button.place(relx = 0.38, rely = .58, anchor='center')
    back_button=Button(text="back")
    back_button.place(relx = 0.07, rely = .58, anchor='center')


    root.mainloop()


if __name__ == '__main__':
    main()
