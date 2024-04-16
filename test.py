from tkinter import * 
from tkinter.ttk import Style
root = Tk()
list=[0,1,2,3,4,5]
i=0
main_frame = Frame(root)
element=Label(main_frame,text=list[i])
element.pack()
main_frame.pack()

root.geometry('600x500')
root.title('Real Estate Data')

def next():
    global i
    global element
    i+=1
    if i>=(len(list)-1):
        next_button.forget()
        pass
    main_frame.forget()
    element.forget()
    element=Label(main_frame,text=list[i])
    main_frame.pack()
    element.pack()
def back():
    global i
    global element
    i-=1
    if i<=0:
        back_button.forget()
        pass
    main_frame.forget()
    element.forget()
    element=Label(main_frame,text=list[i])
    main_frame.pack()
    element.pack()
next_button=Button(text="Next",command=next)
back_button=Button(text="Back",command=back)
next_button.pack()
back_button.pack()
root.mainloop()