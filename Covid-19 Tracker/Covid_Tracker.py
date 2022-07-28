from tkinter import *
coro = Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+100')
coro.configure(background='#f2f2f2')
coro.iconbitmap('Covid-19 Tracker\corona.ico')


#label
mainlabel = Label(coro, text="Corona Virus Information", font=("Arial", 20, "bold"), bg='#f2f2f2', fg='#ff0000')
mainlabel.place(x=200, y=20)

label1 = Label(coro, text="Total Cases", font=("Arial", 15, "bold"), bg='#f2f2f2', fg='#ff0000')
label1.place(x=50, y=100)

entry1 = Entry(coro, width=30, font=("Arial", 15, "bold"), bg='#f2f2f2', fg='#ff0000')
entry1.place(x=200, y=100)

coro.mainloop()