from tkinter import * 
from tkinter.ttk import Style
from PIL import Image, ImageTk
import requests
import json
from scraping import scrapeData
from functions import findAvg, next, back, rankImage

def main():


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
    
    disWidth = 900
    disHeight = 700
    root.geometry(f'{disWidth}x{disHeight}')
    root.title('Real Estate Data')

    info = Frame(root, 
                    height = (disHeight-20), 
                    width = (550),
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    info.pack(side='left',anchor='w',padx=(10,0),pady=10)

    '''starting the construction of the average frame to the right of the screen'''
    average = Frame(root, 
                    height = (disHeight/2.5+45), 
                    width = (1600/5), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    average.pack(side='bottom', anchor = 'se', padx=10, pady=10)

    rankFrame = Frame(root, 
                    height = (disHeight/2.5+60), 
                    width = (1600/5), 
                    highlightcolor = 'black', 
                    highlightbackground = 'black', 
                    highlightthickness = 5)
    rankFrame.pack(side='top', anchor = 'ne',padx=10,pady=(10,0))

    rankHead = Label(rankFrame,
                     text = 'House Ranking',
                     font = ('Fixedsys', 24))
    rankHead.place(relx = 0.5, rely = 0.08, anchor = 'center')

    rankInstructions = Label(rankFrame,
                             text = 'This ranking system is based how metric averages below and how the current listing compares to such. The arrows represent if the value is above or below its respective average.',
                             wraplength = 250, 
                             justify = 'center',
                             font = ('Fixedsys', 10))
    rankInstructions.place(relx = 0.1, rely = 0.12, anchor = 'nw')
    
    '''
    TODO:
        - Compare the values of each house to the average, give eaching average an individualized ranking
        - Give a ranking based out of 5
    '''

    avgHead = Label(average, 
                    text = 'Averages',
                    font = ('Fixedsys', 25))
    avgHead.place(relx = 0.5, rely = 0.08, anchor = 'center')

    textAvg = Text(average,
                   height = 13.5,
                   width = 32,
                   font = ('Fixedsys', 15)) # this value specifically keeps turning into a str and idk why
    textAvg.place(relx = 0.1, rely = 0.18, anchor='nw')

    # Implementation of our ranking systems involving comparison with the rest of our data
    avgPrice = '{:,}'.format(round(avg, 2))
    avgBeds = round(findAvg(beds), 2)
    avgBaths = round(findAvg(baths), 2)
    avgAcres = round(findAvg(acres), 2)
    avgSqft = round(findAvg(sqft), 2)

    # gotta start from somewhere, I suppose
    Label(rankFrame, 
          text = 'Price: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.49, anchor = 'nw')
    priceRank = rankImage(rankFrame, avg, prices[0])
    priceRank.place(anchor = 'nw', relx = 0.38, rely = 0.49)
    
    Label(rankFrame, 
          text = 'Baths: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.58, anchor = 'nw')
    bathsRank = rankImage(rankFrame, avg, baths[0])
    bathsRank.place(anchor = 'nw', relx = 0.38, rely = 0.59)

    
    Label(rankFrame, 
          text = 'Acreage: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.67, anchor = 'nw')
    
    Label(rankFrame, 
          text = 'Square Footage: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.77, anchor = 'nw')

    Label(rankFrame, 
            text = 'Beds: ',
            font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.86, anchor = 'nw')

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
                   font = ('Fixedsys', 16))
    textInfo.place(relx = 0.5, rely = .8, anchor='center')

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
    next_button.place(relx = 0.57, rely = .59, anchor='center') 
    back_button=Button(text="back",command=lambda:back(images, prices, addresses, beds, baths, sqft, acres, house_image, textInfo))
    back_button.place(relx = 0.06, rely = .59, anchor='center')

    print("images: ", len(images))
    print("addresses: ", len(addresses))
    print("prices: ", len(prices))


    root.mainloop()


if __name__ == '__main__':
    main()
