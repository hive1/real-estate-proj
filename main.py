from tkinter import * 
from tkinter.ttk import Style
from PIL import Image, ImageTk
import requests
import json
from scraping import scrapeData
from functions import findAvg, next, back, rankImage, removeDollarSign, arrowReplacer

def main():
    InpWidth = 512
    InpHeight = 470

    # # Creating a root window for main operations
    root = Tk()

    # # Stops the window from being resizable
    root.resizable(0, 0)

    # # root window 
    root.title("Real Estate Finder - Zip")
    root.geometry(f'{InpWidth}x{InpHeight}')

    # i thought adding an icon would be cute, although perhaps not necessary
    p1 = PhotoImage(file = 'haus.png')
    root.iconphoto(False, p1)

    def displayData(textarg):
        Label(basicFrame, text=textarg).pack()
        root.destroy()

    basicFrame = Frame(root).pack()
    zipLabel = Label(basicFrame, text = 'Please input the zip code of your desired location: ', font=('Kannada MW', 14))
    bedLabel = Label(basicFrame, text = 'Beds: ', font=('Kannada MW', 14))
    bathLabel = Label(basicFrame, text = 'Baths: ', font=('Kannada MW', 14))
    minLabel = Label(basicFrame, text = 'Minimum Price: ', font=('Kannada MW', 14))
    maxLabel = Label(basicFrame, text = 'Maximum Price: ', font=('Kannada MW', 14))

    # # The following variable would be used for storing the post code or name of city that the user requests
    zipLabel.pack(side=TOP, pady=5, padx=5)
    locationVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=locationVar).pack(pady=10)

    bedLabel.pack(side=TOP, pady=5, padx=5)
    bedVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=bedVar).pack(pady=10)

    bathLabel.pack(side=TOP, pady=5, padx=5)
    bathVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=bathVar).pack(pady=10)

    minLabel.pack(side=TOP, pady=5, padx=5)
    minVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=minVar).pack(pady=10)

    maxLabel.pack(side=TOP, pady=5, padx=5)
    maxVar = StringVar(basicFrame, value = None)
    Entry(basicFrame, textvariable=maxVar).pack(pady=10)

    # # goofy submit button
    submitButton = Button(basicFrame, text='SUBMIT')
    submitButton.configure(command=lambda: displayData(locationVar.get()))
    submitButton.configure(relief=RAISED, padx=1.5, pady=1.5, font=('Kannada MW', '12'))
    submitButton.pack()

    root.mainloop()

    # Collecting data from the backend
    images = []
    prices = []
    addresses = []
    beds = []
    baths = []
    sqft = []
    acres = []
    avg = None

    (images, prices, addresses, beds, baths, sqft, acres, avg) = scrapeData(locationVar.get())

    root = Tk()

    p1 = PhotoImage(file = 'haus.png')
    root.iconphoto(False, p1)

    root.resizable(0, 0)
    
    disWidth = 900
    disHeight = 700
    root.geometry(f'{disWidth}x{disHeight}')
    root.title('Real Estate Finder')


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
                             text = 'This ranking system is based on the metric averages below and how the current listing compares to such. The arrows represent if the value is above or below its respective average.',
                             wraplength = 300, 
                             justify = 'center',
                             font = ('Fixedsys', 10))
    rankInstructions.place(relx = 0.03 , rely = 0.12, anchor = 'nw')
    
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

    
    '''Placing the arrows'''

    Label(rankFrame, 
          text = 'Price: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.42, anchor = 'nw')
    # If the price is less than the average price, this is a GOOD thing so I made special arrows for that
    if removeDollarSign(prices[0]) < float(avgPrice.replace(',', '')):
        img = (Image.open('arrows/greenarrowdown.png')).resize((40, 40), Image.Resampling.LANCZOS)
    else:
        img = (Image.open('arrows/redarrowup.png')).resize((40, 40), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    ratingImage = Canvas(rankFrame, width = 40, height = 40)
    ratingImage.create_image(0, 0, image = img, anchor = NW)
    ratingImage.image = img
    ratingImage.place(anchor = 'nw', relx = 0.36, rely = 0.42)
    
    Label(rankFrame,
          text = 'Beds: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.54, anchor = 'nw')
    bedsRank = rankImage(rankFrame, avgBeds, float((beds[0]).split()[0]))
    bedsRank.place(anchor = 'nw', relx = 0.36, rely = 0.54)

    Label(rankFrame, 
          text = 'Baths: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.66, anchor = 'nw')
    bathsRank = rankImage(rankFrame, avgBaths, float((baths[0]).split()[0]))
    bathsRank.place(anchor = 'nw', relx = 0.36, rely = 0.66)
    
    Label(rankFrame, 
          text = 'Acreage: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.78, anchor = 'nw')
    acreRank = rankImage(rankFrame, avgAcres, float(acres[0]))
    acreRank.place(anchor = 'nw', relx = 0.46, rely = 0.78)

    Label(rankFrame, 
          text = 'Square Footage: ',
          font = ('Fixedsys', 17)).place(relx = 0.03, rely = 0.88, anchor = 'nw')
    # the sqft[0] parameter is kinda annoying because it has a comma and "sq ft" at the end
    sqftValue = ''.join(c for c in sqft[0] if c.isdigit())

      # if the sqftValue is empty after the last filter, it would mean the data could not be retrieved
    if sqftValue == '':
      img = (Image.open('arrows/x.png')).resize((20, 20), Image.Resampling.LANCZOS)
      img = ImageTk.PhotoImage(img)
      x = Canvas(rankFrame, width = 20, height = 20)
      x.create_image(0, 0, image = img, anchor = NW)
      x.image = img
      x.place(anchor = 'nw', relx = 0.82, rely = 0.86)
    else:
      sqftValue = float(sqftValue)
      sqftRank = rankImage(rankFrame, avgSqft, sqftValue)
      sqftRank.place(anchor = 'nw', relx = 0.82, rely = 0.86)

    # This is where we insert data into the textbox
    textAvg.insert(END, f'Average Price: ${avgPrice}\n')
    textAvg.insert(END, f'Average Beds: {avgBeds}\n')
    textAvg.insert(END, f'Average Baths: {avgBaths}\n')
    textAvg.insert(END, f'Average Square Footage: {avgSqft}')
    textAvg.insert(END, f'Average Acreage: {avgAcres}\n')
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
    textInfo.insert(END,addresses[0])
    textInfo.insert(END,"\n"+prices[0])
    textInfo.insert(END,"\n"+beds[0])
    textInfo.insert(END,"\n"+baths[0] + "\n")
    textInfo.insert(END,f"{sqft[0]}\n")
    textInfo.insert(END,f"{acres[0]} acres\n")

    
    '''Next & Back Buttons'''
    next_button=Button(text="next",command=lambda: [next(images, prices, addresses, beds, baths, sqft, acres, house_image, textInfo),
                                                         arrowReplacer(rankFrame, 
                                                                       ratingImage, bedsRank, bathsRank, sqftRank, acreRank,
                                                                       avgPrice, avgBeds, avgBaths, avgSqft, avgAcres,
                                                                       prices, beds, baths, sqft, acres)])
    next_button.place(relx = 0.57, rely = .59, anchor='center') 
    back_button=Button(text="back",command=lambda: [back(images, prices, addresses, beds, baths, sqft, acres, house_image, textInfo),
                                                         arrowReplacer(rankFrame, 
                                                                       ratingImage, bedsRank, bathsRank, sqftRank, acreRank,
                                                                       avgPrice, avgBeds, avgBaths, avgSqft, avgAcres,
                                                                       prices, beds, baths, sqft, acres)])
    back_button.place(relx = 0.06, rely = .59, anchor='center')

    print("images: ", len(images))
    print("addresses: ", len(addresses))
    print("prices: ", len(prices))

    root.mainloop()

if __name__ == '__main__':
    main()
