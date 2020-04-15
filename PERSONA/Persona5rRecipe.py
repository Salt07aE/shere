#!python3
#coding: utf-8

import sys
import csv
import pandas as pd
from tkinter import *
from tkinter import ttk

class persona_5r_recipe():
    #def __init__(self):

    def main():
        P5R = persona_5r_recipe
        P5R.tkinter_option()

    #def ADD_RECIPE():
    #def SEARCH_RECIPE():
    def tkinter_option():
        root = Tk()
        root.title(u"P5R-Recipe")
        root.geometry("500x350")

        root['bg'] = 'red'

        label1 = Label(root, text="You can add or search Persona!", font = ('Love Letter Typewriter',20), bg='red')
        label1.pack()

        add_button = Button(root, text=u"ADD")
        add_button.pack()
        search_button = Button(root, text=u"SEARCH")
        search_button.pack()
        exit_button = Button(root, text=u"EXIT")
        exit_button.pack()
        root.mainloop()

if __name__=="__main__":
    persona_5r_recipe.main()