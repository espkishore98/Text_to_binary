# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:27:17 2020

@author: Om
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:39:59 2020

@author: Om
"""
import tkinter as tk
from tkinter import messagebox as mb

def get_integers():
    message=text.get()
    numbers=[]
    for give in message:
        number=ord(give)
        numbers.append(number)
    print( numbers)
    return numbers
    
        
def get_binary():
    
    num=[]
    int_list=get_integers()
    for i in int_list:
        x=bin(i).replace("0b","")
        num.append(x)
        print(x,end=" ")
    mb.showinfo("binary code is",num)
    return num



        
    
        
           

        
           
           



root=tk.Tk()
L1=tk.Label(root,text="Text")
b1=tk.Button(root , text="submit", font = 30, width = 10, command=get_binary)

text= tk.Entry(root)
L1.grid(row=0,column=0)
text.grid(row=0,column=1)
b1.grid(row=1,column=1)

root.mainloop()


