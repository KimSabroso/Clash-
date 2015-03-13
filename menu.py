#!/usr/bin/python
import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk
import clash
import pygame
from itertools import chain

class Menu(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master

        self.window()

    def window(self):
        pygame.init()
        self.music_sound()
        self.master.title("Clash ++")

win = Tk()
win.geometry("800x600")
win.resizable(0,0)

app = Menu(win)

win.mainloop()
