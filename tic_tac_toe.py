from tkinter import *
from turtle import bgcolor, width
from unicodedata import name

from setuptools import Command


class TICtactoe:
    xo = 'O'
   

    def tkinter(self ,title , geometry ,color):
        tk = Tk()

        tk.title(title)
        tk.geometry(geometry)

        tk.resizable(0, 0)

        tk.config(bg=color)

        tk.option_add('*button*font','time 40 bold')

        for r in range(0,3):
            for c in range(0,3):
                self.addButton(Button(),r,c)

        mainloop()
    
    def addButton(self,bt,r,c):
        bt.config(width=3,height=1,command =lambda:self.button_click(bt),font = 'tahoma 30 bold')
        bt.grid(row = r,column = c , padx= 5 ,pady =5 ,ipadx=3 ,ipady =1)
    
    def button_click(self, button):
        print(button)
        if button.cget('text') != '':
            return
        
        else:
           self.xo = 'O' if  self.xo == 'X' else 'X'
           button.config(text = self.xo)

           #if button.cget('text')[0] == 'X' and button.cget('text')[1]:
           print(button.cget('text'))

       
              


    
game = TICtactoe()
game.tkinter("tictactoe","300x300","red")


