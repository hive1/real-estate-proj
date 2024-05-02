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
def makeUsable(value):
    if "$" in value:
        return int((value[1:]).replace(',', ''))
    elif 

def rankImage(frame, avg, value):
    print('function called')

    # If value is less than average
    if makeUsable(value) < avg:
        img = Image.open('arrows/arrowdown.png')        
        print('The value is greater')
    else:
        img = Image.open('arrows/arrowup.png')
        print('The value is less')

    img = img.resize((50, 50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    ratingImage = Canvas(frame, width = 50, height = 50)
    ratingImage.create_image(0, 0, image = img, anchor = NW)
    ratingImage.image = img

    return ratingImage

i = 0
def next(image, price, address, bed, bath, sqft, acres, house, text_box, rank_box):
    global i
    i+=1
    if i>=len(price):
        i=0
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
    

if __name__ == '__main__':
    main()
