from tkinter import * 
from tkinter.ttk import Style
from PIL import Image, ImageTk
import requests
import json
from scraping import scrapeData
from functions import findAvg, next, back

def main():
    '''
    TODO:
        - Compare the values of each house to the average, give eaching average an individualized ranking
        - Give a ranking based out of 5
    '''

    # InpWidth = 512
    # InpHeight = 250

    # # Creating a root window for main operations
    # root = Tk()

    # # Stops the window from being resizable
    # root.resizable(0, 0)

    # # root window 
    # root.title("Real Estate Collector v1")
    # root.geometry(f'{InpWidth}x{InpHeight}')

    # def displayData(textarg):
    #     Label(basicFrame, text=textarg).pack()
    #     root.destroy()

    # basicFrame = Frame(root).pack()
    # inputLabel = Label(basicFrame, text = 'Please input the zip code of your desired location: ', font=('Kannada MW', 14))
    # inputLabel.pack(side=TOP, pady=5, padx=5)

    # # The following variable would be used for storing the post code or name of city that the user requests
    # locationVar = StringVar(basicFrame, value = None)
    # Entry(basicFrame, textvariable=locationVar).pack(pady=10)

    # # goofy submit button
    # submitButton = Button(basicFrame, text='SUBMIT')
    # submitButton.configure(command=lambda: displayData(locationVar.get()))
    # submitButton.configure(relief=RAISED, padx=1.5, pady=1.5, font=('Kannada MW', '12'))
    # submitButton.pack()

    # root.mainloop()

    # Collecting data from the backend
    images = []
    prices = []
    addresses = []
    beds = []
    baths = []
    sqft = []
    acres = []
    avg = None

    #(images, prices, addresses, beds, baths, sqft, acres, avg) = scrapeData(locationVar.get())
    (images, prices, addresses, beds, baths, sqft, acres, avg) = scrapeData('11934')

    root = Tk() 
    root.resizable(0, 0)
    
    disWidth = 1000
    disHeight = 700
    root.geometry(f'{disWidth}x{disHeight}')
    root.title('Real Estate Data')

    '''starting the construction of the average frame to the right of the screen'''
    '''
    average = Frame(root, 
                    height = (disHeight/2.5), 
                    width = (1600/5), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    average.pack(side='right')
    '''
    rankFrame = Frame(root, 
                    height = (disHeight/2.5), 
                    width = (1600/5), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    rankFrame.place(anchor='ne',relx=0,rely=0)

    info = Frame(root, 
                    height = (disHeight-20), 
                    width = (1600-(1600/5+30)), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    info.pack(side='left', padx=5, pady=30)

    avgHead = Label(average, 
                    text = 'Averages',
                    font = ('Fixedsys', 25))
    avgHead.place(relx = 0.5, rely = 0.15, anchor = 'center')

    textAvg = Text(average,
                   height = 12.4,
                   width = 36,
                   font = ('Fixedsys', 15)) # this value specifically keeps turning into a str and idk why
    textAvg.place(relx = 0.03, rely = 0.3, anchor='nw')

    # Implementation of our ranking systems involving comparison with the rest of our data
    avgPrice = '{:,}'.format(round(avg, 2))
    avgBeds = round(findAvg(beds), 2)
    avgBaths = round(findAvg(baths), 2)
    avgAcres = round(findAvg(acres), 2)
    avgAcres = round(findAvg(sqft), 2)
    avgSqft = round(findAvg(sqft), 2)

    # This is where we insert data into the textbox
    textAvg.insert(END, f'Average price: ${avgPrice}\n')
    textAvg.insert(END, f'Average beds: {avgBeds}\n')
    textAvg.insert(END, f'Average baths: {avgBaths}\n')
    textAvg.insert(END, f'Average Acreage: {avgAcres}\n')
    textAvg.insert(END, f'Average Square Footage: {avgSqft}')
    textAvg.config(state = DISABLED)

    textInfo = Text(info,
                   height = 12.4,
                   width = 52,
                   font = ('Fixedsys', 15))
    textInfo.place(relx = 0.5, rely = .81, anchor='center')

    # making everything 
    style = Style()
    style.configure('W.TButton', font = ('calibri', 14, 'bold', 'underline'), foreground = 'blue')

    '''House Image'''
    url = images[0]
    image = Image.open(requests.get(url, stream=True).raw)
    resized_image=image.resize((int(776/1.5),int(500/1.5)))
    photo = ImageTk.PhotoImage(resized_image)
    house_image = Canvas(info, width=776/1.5, 
            height=500/1.5) 
    house_image.create_image(0,0,image=photo,anchor=NW)
    house_image.image = photo
    house_image.place(relx = 0.5, rely = .3, anchor='center')
    
    '''Info Textbox'''
    textInfo.insert(END,prices[0])
    textInfo.insert(END,"\n"+addresses[0])
    textInfo.insert(END,"\n"+beds[0])
    textInfo.insert(END,"\n"+baths[0] + "\n")
    textInfo.insert(END,f"{sqft[0]}\n")
    textInfo.insert(END,f"{acres[0]} acres\n")
    
    '''Next & Back Buttons'''
    next_button=Button(text="next",command=lambda:next(images, prices, addresses, beds, baths, sqft, acres, house_image, textInfo))
    next_button.place(relx = 0.54, rely = .59, anchor='center') 
    back_button=Button(text="back",command=lambda:back(images, prices, addresses, beds, baths, sqft, acres, house_image, textInfo))
    back_button.place(relx = 0.08, rely = .59, anchor='center')

    print("images:",len(images))
    print("addresses:",len(addresses))
    print("prices:",len(prices))


    root.mainloop()


if __name__ == '__main__':
    main()
