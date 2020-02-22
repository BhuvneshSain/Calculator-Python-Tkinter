#!/usr/bin/python
from tkinter import *
def addText(numbers):
    global operator
    operator = operator + str(numbers)
    Input.set(operator)
def btnclear():
    global operator
    operator = ""
    Input.set(operator)
def btnEqualss():
    global operator
    sumup = str(eval(operator))
    Input.set(sumup)
    operator=""
m=Tk()
m.title("calculator")
operator=""
Input = StringVar()
que=Entry(m,bd=20,font=('',20),text=Input).grid(columnspan=10)
bCLR=Button(m,width=10,text='C',command=btnclear).grid(row=5,column=2)
b1=  Button(m,width=10,text='1',command=lambda : addText(1)).grid(row=2,column=0)
b2=  Button(m,width=10,text='2',command=lambda : addText(2)).grid(row=2,column=1)
b3=  Button(m,width=10,text='3',command=lambda : addText(3)).grid(row=2,column=2)
b4=  Button(m,width=10,text='4',command=lambda : addText(4)).grid(row=3,column=0)
b5=  Button(m,width=10,text='5',command=lambda : addText(5)).grid(row=3,column=1)
b6=  Button(m,width=10,text='6',command=lambda : addText(6)).grid(row=3,column=2)
b7=  Button(m,width=10,text='7',command=lambda : addText(7)).grid(row=4,column=0)
b8=  Button(m,width=10,text='8',command=lambda : addText(8)).grid(row=4,column=1)
b9=  Button(m,width=10,text='9',command=lambda : addText(9)).grid(row=4,column=2)
b0=  Button(m,width=10,text='0',command=lambda : addText(0)).grid(row=5,column=0)
bADD=Button(m,width=10,text='+',command=lambda : addText('+')).grid(row=2,column=4)
bDIV=Button(m,width=10,text='/',command=lambda : addText('/')).grid(row=2,column=3)
bMUL=Button(m,width=10,text='*',command=lambda : addText('*')).grid(row=3,column=4)
bSUB=Button(m,width=10,text='-',command=lambda : addText('-')).grid(row=3,column=3)
bANS=Button(m,width=10,text='=',command=btnEqualss).grid(row=4,column=3)
mainloop()