from tkinter import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup

def main():
    ex = ['2.5 baths', '2.5 baths', '1.5 baths', '2.5 baths', '2.5 baths', 
          '1 bath', '2.5 baths', '1 bath', '8 baths', '2.5 baths', '1 bath', 
          '2.5 baths', '3.5 baths', '9 baths', '2.5 baths', '3 baths', '5.5 baths', 
          '2.5 baths', '5.5 baths', '3.5 baths', '— baths', '— baths', '— baths', 
          '— baths', '— baths', '— baths', '— baths']
    
    print(findAvg(ex))

# Find the averages of input lists, most likely containing string characters
# Remember to ignore the values associated with '-'
def findAvg(coll: list) -> int:
    total = 0
    count = 0
    for elem in coll:

        # Isolates whatever information is behind the space
        try:
            count += 1
            number = float(elem.split()[0].replace(",", ""))
            total += number
        except ValueError:
            continue
    if count == 0:
        return 0
    return total/count


# This function is dedicated to making parameters passed into 
def removeDollarSign(value):
    return float((value[1:]).replace(',', ''))

def rankImage(frame, avg, value):

    # If value is less than average
    if value < avg:
        img = Image.open('arrows/arrowdown.png')        
    else:
        img = Image.open('arrows/arrowup.png')

    img = img.resize((40, 40), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)

    ratingImage = Canvas(frame, width = 40, height = 40)
    ratingImage.create_image(0, 0, image = img, anchor = NW)
    ratingImage.image = img

    return ratingImage
    
i = 0
def next(image, price, address, bed, bath, sqft, acres, house, text_box):
    
    global i
    i += 1
    if i >= len(price):
        i = 0

    house.forget()
    url = image[i]
    img = Image.open(requests.get(url, stream=True).raw)
    resized_image=img.resize((int(776/1.5),int(500/1.5)))
    photo = ImageTk.PhotoImage(resized_image)
    house.create_image(0,0, image=photo, anchor=NW)
    house.image = photo
    house.place(relx = 0.5, rely = .3, anchor='center')

    '''inserts the text data itself'''
    text_box.delete('1.0',END)
    text_box.insert(END,price[i])
    text_box.insert(END,"\n"+address[i])
    text_box.insert(END,"\n"+bed[i])
    text_box.insert(END,"\n"+bath[i])
    text_box.insert(END,"\n"+sqft[i])
    text_box.insert(END,"\n"+acres[i]+" acres")

    '''Replace the ranking system'''

def back(image, price, address, bed, bath, sqft, acres, house, text_box):
    global i
    i-=1
    if i<0:
        i=len(price)-1
    house.forget()
    url = image[i]
    img = Image.open(requests.get(url, stream=True).raw)
    resized_image=img.resize((int(776/1.5),int(500/1.5)))
    photo = ImageTk.PhotoImage(resized_image)
    house.create_image(0,0, image=photo, anchor=NW)
    house.image = photo
    house.place(relx = 0.5, rely = .3, anchor='center')
    text_box.delete('1.0',END)
    text_box.insert(END,price[i])
    text_box.insert(END,"\n"+address[i])
    text_box.insert(END,"\n"+bed[i])
    text_box.insert(END,"\n"+bath[i])
    text_box.insert(END,"\n"+sqft[i])
    text_box.insert(END,"\n"+acres[i]+" acres")

# man i hate how i wrote this sm but i cant think of a better way to do it
def arrowReplacer(frame,
                  priceArrow, bedArrow, bathArrow, sqftArrow, acreArrow,
                  avgPrice, avgBeds, avgBaths, avgSqft, avgAcres,
                  prices: list, beds: list, baths: list, sqft: list, acres: list):
    global i

    # this is specifically for the price ranking
    if removeDollarSign(prices[i]) < float(avgPrice.replace(',', '')):
        img = (Image.open('arrows/greenarrowdown.png')).resize((40, 40), Image.Resampling.LANCZOS)
    else:
        img = (Image.open('arrows/redarrowup.png')).resize((40, 40), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    ratingImage = Canvas(frame, width = 40, height = 40)
    ratingImage.create_image(0, 0, image = img, anchor = NW)
    ratingImage.image = img
    ratingImage.place(anchor = 'nw', relx = 0.36, rely = 0.42)

    # this is for beds
    bedsRank = rankImage(frame, avgBeds, float((beds[i]).split()[0]))
    bedsRank.place(anchor = 'nw', relx = 0.36, rely = 0.54)

    # this is for baths
    bathsRank = rankImage(frame, avgBaths, float((baths[i]).split()[0]))
    bathsRank.place(anchor = 'nw', relx = 0.36, rely = 0.66)

    # this is for acres
    acreRank = rankImage(frame, avgAcres, float(acres[i]))
    acreRank.place(anchor = 'nw', relx = 0.46, rely = 0.78)
 
    sqftValue = ''.join(c for c in sqft[i] if c.isdigit())

    if sqftValue == '':
        img = (Image.open('arrows/x.png')).resize((25, 25), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        x = Canvas(frame, width = 25, height = 25)
        x.create_image(0, 0, image = img, anchor = NW)
        x.image = img
        x.place(anchor = 'nw', relx = 0.84, rely = 0.88)
    
    else:
        sqftValue = float(sqftValue)

        sqftRank = rankImage(frame, avgSqft, sqftValue)
        sqftRank.place(anchor = 'nw', relx = 0.82, rely = 0.86)

if __name__ == '__main__':
    main()
