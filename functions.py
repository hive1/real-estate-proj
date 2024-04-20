import math
from tkinter import *
from PIL import Image, ImageTk
import requests
import json
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

i=0
def next(image, price, address, bed, bath, sqft, acres, house, text_box):
    global i
    i+=1
    if i>=(len(price)-1):
        i=0
    house.forget()
    url = image[i]
    img = Image.open(requests.get(url, stream=True).raw)
    photo = ImageTk.PhotoImage(img)
    house.create_image(320/1.2,230/1.2, image=photo)
    house.image = photo
    house.place(relx = 0.29, rely = .303, anchor='center')

    '''inserts the text data itself'''
    text_box.delete('1.0',END)
    text_box.insert(END,price[i])
    text_box.insert(END,"\n"+address[i])
    text_box.insert(END,"\n"+bed[i])
    text_box.insert(END,"\n"+bath[i])
    text_box.insert(END,"\n"+sqft[i])
    text_box.insert(END,"\n"+acres[i]+" acres")

def back(image, price, address, bed, bath, sqft, acres, house, text_box):
    global i
    print(i)

    i-=1
    if i<0:
        i=(len(price)-1)
    url = image[i]
    img = Image.open(requests.get(url, stream=True).raw)
    photo = ImageTk.PhotoImage(img)
    house.create_image(320/1.2,230/1.2, image=photo)
    house.image = photo
    house.place(relx = 0.29, rely = .303, anchor='center')
    text_box.delete('1.0',END)
    text_box.insert(END,price[i])
    text_box.insert(END,"\n"+address[i])
    text_box.insert(END,"\n"+bed[i])
    text_box.insert(END,"\n"+bath[i])
    text_box.insert(END,"\n"+sqft[i])
    text_box.insert(END,"\n"+acres[i]+" acres")
    

if __name__ == '__main__':
    main()
