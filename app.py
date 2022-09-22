from tkinter import *
import customtkinter as ctk
import os

root = Tk()
root.geometry("640x640")
root.title("Auto Diary")


#region [ Variables ]
btnRadius = 20
bgc = "#5a068e"
txtbg = "#120024"
txtfg = "#fff"
btnbg = "#b7138b"
btnch = "#6D0B53"
#endregion

def newNote():
    entryNum = int(open("config\count.txt").read())
    entryNum+=1
    entryDir = f"entrys/entry_{entryNum}.txt"
    
    entry = entryField.get(1.0, END)

    open(entryDir, 'w').write(entry)

    cfgFile = open("config\count.txt", 'w')
    cfgFile.write(str(entryNum))
    exit()

def openEntryDir():
    os.startfile('entrys')

winBg = Canvas(root, width=640, height=640, bg=bgc).place(x=0, y=0)

title = ctk.CTkLabel(root, text="New Entry:", fg_color=bgc, text_font=("sans-serif", 16)).pack(pady=10)


entryField = ctk.CTkTextbox(root, fg_color=txtbg, border=0, corner_radius=30,
                            height=482, width=560, text_font=("sans-serif", 16),
                            bg_color=bgc)
entryField.pack()

btnFrame = Frame(root, bg=bgc)
btnFrame.pack()


btnSave = ctk.CTkButton(btnFrame, command=newNote, corner_radius=btnRadius, hover_color=btnch,
                        height=80, text="Save Entry", fg_color=btnbg, text_font=("sans-serif", 16))
btnOpen = ctk.CTkButton(btnFrame, command=openEntryDir, corner_radius=btnRadius, hover_color=btnch,
                        height=80, text="Open Folder", fg_color=btnbg, text_font=("sans-serif", 16))


btnSave.grid(column=0, row=0,  pady=15,padx=10)
btnOpen.grid(column=20, row=0, pady=15, padx=10)



root.mainloop()