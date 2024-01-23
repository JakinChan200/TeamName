# import pyautogui
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
bgColor = "#AADB1E"

def display_board():
    screen = tk.Tk() #Initialize Screen
    screen.title("2048") #Title for Screen
    screen_width, screen_height = screen.winfo_screenwidth(), screen.winfo_screenheight() #Get screen width and height
    screen.geometry('%dx%d+%d+%d' % (800, 800, (screen_width/2) - (800/2), (screen_height/2) - (800/2))) #Set screen width and height depending on monitor's screen's width and height
    screen.resizable(False,False) #Make it so you can't shrink the window size

    Grid.rowconfigure(screen,2,weight = 1) #Weights for the 6 by 4 grid so they are all equal weights except for first 2 rows which are text and buttons
    Grid.rowconfigure(screen,3,weight = 1)
    Grid.rowconfigure(screen,4,weight = 1)
    Grid.rowconfigure(screen,5,weight = 1)
    Grid.rowconfigure(screen,6,weight = 1)
    Grid.columnconfigure(screen,0,weight = 1)
    Grid.columnconfigure(screen,1,weight = 1)
    Grid.columnconfigure(screen,2,weight = 1)
    Grid.columnconfigure(screen,3,weight = 1)
    Grid.columnconfigure(screen,4,weight = 1)

    screen.configure(bg=bgColor)

    create_text_and_buttons(screen) #Create text and buttons (New Game, Bot Plays, You Play)
    create_grid(screen) #Create the 4 by 4 grid

    screen.mainloop() #Display's the screen

def create_grid(screen):
    for i in range(4): #Create 4 by 4 grid
        for j in range(4):
            label = tk.Label(screen, text="", relief = "solid", borderwidth = 2, width = 30, height = 30, bg = "#aa7dfa") #Create the labels for each grid space
            label.grid(row = i+2,column = j) #Set the grid starting from 2,0

def create_text_and_buttons(screen):
    header_label = tk.Label(screen, text = "2048", font = ("Arial", 50), fg = "#1b1c1e", bg = bgColor) #2048 Text located at 0,0
    header_label.grid(row = 0, column = 0, pady = (30,10), padx = 20, columnspan = 2)

    play_yourself_button = tk.Button(screen, text = "You Play", bg = "#d342f8", command=lambda: click_button(play_yourself_button, screen)) #Play Yourself button located at 0,2
    play_yourself_button.grid(row = 0, column = 2,sticky = "ew", pady=(0,3))

    play_bot_button = tk.Button(screen, text = "AI Play", bg = "#d342f8",  command=lambda: click_button(play_bot_button, screen)) #AI Play button located at 1,2
    play_bot_button.grid(row = 1, column = 2, sticky = "ew", pady = (0,30))

def click_button(button, screen):
    button.configure(bg = "grey") #Change color to grey when clicked
    reset_board(screen) #Reset the board
    # TODO if "you play" button go to regular game
    # TODO else if "" bot plays

def reset_board(screen):
    a = 1 #TODO Reset the screen here

if __name__ == "__main__":
    display_board()