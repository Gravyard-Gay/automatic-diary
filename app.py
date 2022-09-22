from tkinter import *
import customtkinter as ctk
import os


root = Tk()
root.geometry("640x640")
root.title("Auto Diary")

#region [ Variables ]
btnRadius = 20

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



entryField = Text(root, width=50, height=20, font=("sans-serif", 16))
entryField.pack(pady=30)

btnFrame = Frame(root)
btnFrame.pack()


btnSave = ctk.CTkButton(btnFrame, command=newNote, corner_radius=btnRadius, height=50, text="Save Entry")
btnOpen = ctk.CTkButton(btnFrame, command=openEntryDir, corner_radius=btnRadius, height=50, text="Open Entrys Folder")


btnSave.grid(column=0, row=0, padx=10)
btnOpen.grid(column=20, row=0, padx=10)



root.mainloop()