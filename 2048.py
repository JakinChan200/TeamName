import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
from pynput import keyboard
from pynput.keyboard import Key

bgColor = "#AADB1E"

data = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

def display_board():
    screen = tk.Tk() #Initialize Screen
    screen.title("2048") #Title for Screen
    screen_width, screen_height = screen.winfo_screenwidth(), screen.winfo_screenheight() #Get screen width and height
    screen.geometry('%dx%d+%d+%d' % (800, 800, (screen_width/2) - (800/2), (screen_height/2) - (800/2))) #Set screen width and height depending on monitor's screen's width and height
    screen.resizable(False,False) #Make it so you can't shrink the window size

    screen.bind('<Left>', lambda event: on_left_key(event,screen))
    screen.bind('<Right>', lambda event: on_right_key(event,screen))
    screen.bind('<Up>', lambda event: on_up_key(event,screen))
    screen.bind('<Down>', lambda event: on_down_key(event,screen))
    
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

    create_Start_State() #Create two starting tiles randomly each with 2 or 4

    create_text_and_buttons(screen) #Create text and buttons (New Game, Bot Plays, You Play)
    create_grid(screen) #Create the 4 by 4 grid

    screen.mainloop() #Display's the screen

def create_grid(screen):
    global data
    for i in range(4): #Create 4 by 4 grid
        for j in range(4):
            label = tk.Label(screen, text=data[i][j], relief = "solid", borderwidth = 2, width = 30, height = 30, bg = "#aa7dfa", font = ("Arial", 35)) #Create the labels for each grid space
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
    # create_screen(board) #Reset the board
    # TODO if "you play" button go to regular game
    # TODO else if "" bot plays

def create_Start_State():
    global data
    piece_one_x = random.randint(0,3) #Random X Starting Position
    piece_one_y = random.randint(0,3) #Random Y Starting Positionnotiis
    piece_two_x = random.randint(0,3)
    piece_two_y = random.randint(0,3)
    piece_one_value = random.choice([2,4])  
    piece_two_value = random.choice([2,4])
    
    while piece_one_x == piece_two_x and piece_one_y == piece_two_y: #Make sure the 2 pieces aren't on the same spot
        piece_two_x = random.randint(0,3)
        piece_two_y = random.randint(0,3)
        
    data[piece_one_x][piece_one_y] = str(piece_one_value)
    data[piece_two_x][piece_two_y] = str(piece_two_value)

# numbers next to each other
# numbers have a space or two between them

def on_left_key(event, screen):
    for i in range(4):          #rows
        for j in range(4):      #columns
            for k in range(j):  #0 to j
                if data[i][j] == "":
                    continue
                if k == j-1: #case where the two numbers are next to each other
                    if data[i][k] == data[i][j]:
                        data[i][k] = str(int(data[i][k])*2)
                        data[i][j] = ""
                if data[i][k] == "": #case where there is a number in between
                    if k != 0 and data[i][k-1] == data[i][j]:
                        data[i][k-1] = str(int(data[i][k-1])*2)
                        data[i][j] = ""
                    else:
                        data[i][k] = data[i][j]
                        data[i][j] = ""
    create_grid(screen)

def on_right_key(event, screen):
    for i in range(4):
        for j in range(3, -1, -1):
            for k in range(3, j-1, -1):
                if data[i][j] == "":
                    continue
                if j != 3 and k == j+1: #case where the two numbers are next to each other
                    if data[i][k] == data[i][j]:
                        data[i][k] = str(int(data[i][k])*2)
                        data[i][j] = ""
                if data[i][k] == "": #case where there is a blank in between
                    if k != 3 and data[i][k+1] == data[i][j]: # case where the last one we looked at is the one 
                        data[i][k+1] = str(int(data[i][k+1])*2)
                        data[i][j] = ""
                    else:
                        data[i][k] = data[i][j]
                        data[i][j] = ""
    create_grid(screen)

def on_up_key(event, screen):
    for j in range(4):                  #iterating through columns
        for i in range(4):              #iterating through rows
            for k in range(i):          #iterating through column up to j
                if data[i][j] == "":    #nothing there
                    continue
                if k == i - 1:                            #If they are next to each other
                    if data[i][j] == data[k][j]:            #If values are the same
                        data[k][j] = str(int(data[k][j])*2) #Combine them
                        data[i][j] = ""
                if data[k][j] == "":    #if there is at least one tile empty above it
                    if k != 0 and data[k-1][j] == data[i][j]:
                        data[k-1][j] = str(int(data[k-1][j])*2)
                        data[i][j] = ""
                    else:
                        data[k][j] = data[i][j] 
                        data[i][j] = ""
                    
    create_grid(screen)

def on_down_key(event, screen):
    for j in range(4):                          #iterating through columns
        for i in range(3, -1, -1):              #iterating through rows
            for k in range(3, i-1, -1):         #iterating through column up to j
                if data[i][j] == "":            #nothing there
                    continue
                if k == i + 1:                            #If they are next to each other
                    if data[i][j] == data[k][j]:            #If values are the same
                        data[k][j] = str(int(data[k][j])*2) #Combine them
                        data[i][j] = ""
                if data[k][j] == "":    #if there is at least one tile empty above it
                    if k != 3 and data[k+1][j] == data[i][j]:
                        data[k+1][j] = str(int(data[k+1][j])*2)
                        data[i][j] = ""
                    else:
                        data[k][j] = data[i][j] 
                        data[i][j] = ""
                    
    create_grid(screen)
    

if __name__ == "__main__":
    display_board()
