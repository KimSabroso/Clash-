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
        self.show_button()

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
        self.btn_ng.bind('<Enter>', self.btn_ngEnter)
        self.btn_ng.bind('<Leave>', self.btn_ngLeave)

        self.btn_help = Button(self, bd=0, bg="black", image = self.help_btn, command = self.helps)
        self.btn_help.configure(image = self.help_btn)
        self.btn_help.place(x=30, y = 180)
        self.btn_help.bind('<Enter>', self.btn_helpEnter)
        self.btn_help.bind('<Leave>', self.btn_helpLeave)

        self.btn_option = Button(self, bd=0, bg="black", image = self.option_btn)
        self.btn_option.configure(image = self.option_btn)
        self.btn_option.place(x=30, y = 260)
        self.btn_option.bind('<Enter>', self.btn_optionEnter)
        self.btn_option.bind('<Leave>', self.btn_optionLeave)
        

        self.btn_exit = Button(self, bd=0, bg="black", image = self.exit_btn)
        self.btn_exit.configure(image = self.exit_btn)
        self.btn_exit.place(x=30, y = 340)
        self.btn_exit.bind('<Enter>', self.btn_exitEnter)
        self.btn_exit.bind('<Leave>', self.btn_exitLeave)

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

    def btn_ngLeave(self, event):
        self.btn_ng.configure(image =self.new_game_btn )

    def btn_helpLeave(self, event):
        self.btn_help.configure(image =self.help_btn )

    def btn_hsLeave(self, event):
        self.btn_hs.configure(image =self.hs_btn )

    def btn_optionLeave(self, event):
        self.btn_option.configure(image =self.option_btn )

    def btn_exitLeave(self, event):
        self.btn_exit.configure(image =self.exit_btn )

    def btn_menuLeave(self, event):
        self.btn_menu.configure(image =self.menu_btn )

    def new_game(self):
        clash.main()
        self.master.withdraw()

    def sub_bg(self, lbl):
        self.window()
        self.bg_img.configure(image = self.sub)

        img = PhotoImage(file = "images/lbl-"+lbl+".gif")
        lbl = Label(self, bd =0, image = img)
        lbl.image = img
        lbl.place(x = 300, y = 155)

        self.btn_menu = Button(self, bd =0, bg = "gray", image = self.menu_btn)
        self.btn_menu.configure(image = self.menu_btn)
        self.btn_menu.place(x =300, y = 400)
        self.btn_menu.bind('<Enter>', self.btn_menuEnter)
        self.btn_menu.bind('<Leave>', self.btn_menuLeave)

    def menu(self):
        self.window()
        self.show_button()

    def helps(self):
        self.sub_bg("help")

        img =PhotoImage(file = "images/help_sub.gif")
        lbl = Label(self, bd = 0, image = img)
        lbl.image = img
        lbl.place(x = 290, y = 220)

    def option(self):
        self.sub_bg("options")

        img = PhotoImage(file = "images/option_bg.gif")
        lbl = Label(self, bd = 0, image = img)
        lbl.image = img
        lbl.place(x =290, y = 220)

        m1 = PhotoImage(file = "images/music.gif")
        s1 = PhotoImage(file = "images/sound.gif")
        self.m12 = PhotoImage(file = "images/music2.gif")
        self.s12 = PhotoImage(file = "images/sound2.gif")

        music = Button(self, bd = 0, bg = "gray", image = m1, command = self.music)
        music.image = m1
        music.place(x = 445, y = 245)

        sound = Button(self, bd = 0, bg = "gray", image = s1)
        sound.image = s1
        sound.place(x = 445, y = 310)

        conn = sqlite3.connect('clash.db')
        cursor = conn.execute("SELECT * FROM clash_option")
        try:
            first_row = next(cursor)
            for row in chain((first_row,),cursor):
                if str(row[0]) == "ON":
                    music.configure(image = self.m12)
                if str(row[1]) == "ON":
                    sound.configure(image = self.s12)
        except StopIteration as e:
            lbl = Label(self, bd = 0, bg = "lightgray", font = ("Arial", 20), text = "An errored occured.").place(x=255, y=235)

    def music(self):
        conn = sqlite3.connect('clash.db')
        cursor = conn.execute("SELECT * FROM clash_option")
        try:
            first_row = next(cursor)
            for row in chain((first_row,),cursor):
                if str(row[0]) == "ON":
                    conn.execute("UPDATE clash_option SET Music = 'OFF'")
                    conn.commit()
                else:
                    conn.execute("UPDATE clash_option SET Music = 'ON'")
                    conn.commit() 
        except StopIteration as e:
            lbl = Label(self, bd = 0, bg = "lightgray", font = ("Arial", 20), text = "An errored occured.").place(x=255, y=235)
        self.option()

    def sounds(self):
        conn = sqlite3.connect('clash.db')
        cursor = conn.execute("SELECT * FROM clash_option")
        try:
            first_row = next(cursor)
            for row in chain((first_row,),cursor):
                if str(row[1]) == "ON":
                    conn.execute("UPDATE clash_option SET Sound = 'OFF'")
                    conn.commit()
                else:
                    conn.execute("UPDATE clash_option SET Sound = 'ON'")
                    conn.commit() 
        except StopIteration as e:
            lbl = Label(self, bd = 0, bg = "lightgray", font = ("Arial", 20), text = "An errored occured.").place(x=255, y=235)
        self.option(

win = Tk()
win.geometry("800x600")
win.resizable(0,0)

app = Menu(win)

win.mainloop()
