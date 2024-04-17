import math
from tkinter import * 

# Find the averages of input lists, most likely containing string characters
# Remember to ignore the values associated with '-'
def findAvg(coll: list) -> int:
    total = 0
    count = 0

    for elem in coll:

        # Isolates whatever information is behind the space
        try:
            number = float(elem.split()[0])
            total += number
            count += 1

        except ValueError:
            continue
    if count == 0:
        return 0
    return total/count
         
def main():
    ex = ['2.5 baths', '2.5 baths', '1.5 baths', '2.5 baths', '2.5 baths', 
          '1 bath', '2.5 baths', '1 bath', '8 baths', '2.5 baths', '1 bath', 
          '2.5 baths', '3.5 baths', '9 baths', '2.5 baths', '3 baths', '5.5 baths', 
          '2.5 baths', '5.5 baths', '3.5 baths', '— baths', '— baths', '— baths', 
          '— baths', '— baths', '— baths', '— baths']
    
    print(findAvg(ex))
i=0
def next(price,text_box):
    global i
    i+=1
    if i>=(len(price)-1):
        text_box.delete('1.0',END)
        pass
    text_box.delete('1.0',END)
    text_box.insert(END,price[i])

if __name__ == '__main__':
    main()
