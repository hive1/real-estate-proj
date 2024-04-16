from tkinter import * 
from tkinter.ttk import Style
root = Tk()
list=[0,1,2,3,4,5]
i=0
element=Label(text=list[i])
element.pack()

root.geometry('600x500')
root.title('Real Estate Data')

def next():
    element.forget()
    i+=1
    element=Label(text=list[i])
    element.pack()
next_button=Button(text="Next",command=next)
next_button.pack()

root.mainloop()