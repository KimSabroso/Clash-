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

        #load images
        icon = PhotoImage(file = "images/icon.gif")
        bg = PhotoImage(file = "images/bg.gif")
        self.sub =PhotoImage(file = "images/sub-bg.gif") 
        self.new_game_btn = PhotoImage(file = "images/buttons/newgame.gif")
        self.new_gameh_btn = PhotoImage(file = "images/buttons/newgameh.gif")
        self.help_btn = PhotoImage(file = "images/buttons/help.gif")
        self.helph_btn = PhotoImage(file = "images/buttons/helph.gif")
        self.option_btn = PhotoImage(file = "images/buttons/options.gif")
        self.optionh_btn =PhotoImage (file = "images/buttons/optionsh.gif")
        self.hs_btn =PhotoImage (file = "images/buttons/highscore.gif")
        self.hsh_btn = PhotoImage(file = "images/buttons/highscoreh.gif")
        self.exit_btn = PhotoImage(file = "images/buttons/exit.gif")
        self.exith_btn = PhotoImage(file = "images/buttons/exith.gif")
        self.menu_btn =PhotoImage (file = "images/buttons/menu.gif")
        self.menuh_btn =PhotoImage (file = "images/buttons/menuh.gif")

win = Tk()
win.geometry("800x600")
win.resizable(0,0)

app = Menu(win)

win.mainloop()
