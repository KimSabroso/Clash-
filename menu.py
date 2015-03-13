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

        self.tk.call('wm', 'iconphoto', win._w, icon)

        
        self.pack(fill = BOTH, expand = 1)

        #display background
        self.bg_img = Label(self, image = bg)
        self.bg_img.image = bg
        self. bg_img.place(x=-2, y=-2)

    def show_button(self):
        #displaying of buttons
        self.btn_ng = Button(self, bd=0, bg="black", image = self.new_game_btn, command = self.new_game)
        self.btn_ng.configure(image = self.new_game_btn)
        self.btn_ng.place(x=30, y = 100)

        self.btn_help = Button(self, bd=0, bg="black", image = self.help_btn, command = self.helps)
        self.btn_help.configure(image = self.help_btn)
        self.btn_help.place(x=30, y = 180)

        self.btn_option = Button(self, bd=0, bg="black", image = self.option_btn, command = self.option)
        self.btn_option.configure(image = self.option_btn)
        self.btn_option.place(x=30, y = 260)

        self.btn_exit = Button(self, bd=0, bg="black", image = self.exit_btn, command = win.destroy)
        self.btn_exit.configure(image = self.exit_btn)
        self.btn_exit.place(x=30, y = 340)

    def btn_ngEnter(self, event):
        self.btn_ng.configure(image = self.new_gameh_btn)

    def btn_helpEnter(self, event):
        self.btn_help.configure(image = self.helph_btn)

    def btn_hsEnter(self, event):
        self.btn_hs.configure(image = self.hsh_btn)

    def btn_optionEnter(self, event):
        self.btn_option.configure(image = self.optionh_btn)

    def btn_exitEnter(self, event):
        self.btn_exit.configure(image = self.exith_btn)

    def btn_menuEnter(self, event):
        self.btn_menu.configure(image = self.menuh_btn)

win = Tk()
win.geometry("800x600")
win.resizable(0,0)

app = Menu(win)

win.mainloop()
