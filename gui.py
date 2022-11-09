# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 01:00:20 2022

@author: anish
"""

import tkinter as tk
import os
from tkinter import ttk
import pandas as pd
import keyboard
from PIL import Image, ImageTk





def startPage(root):
    page = tk.Frame(root)
    page.grid()


    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    width = 30
    height = 30
    img = ImageTk.PhotoImage(Image.open("/Users/jihyeonje/Desktop/logo.png"))
    panel = tk.Label(page, image = img).grid(row = 0)
    tk.Label(page, text="Welcome to OCTopi's Anterior Segment OCT", font='Helvetica 10 bold').grid(row = 1)
    #label.pack(side="top", fill="both", expand=True)

    tk.Button(page, text = 'Begin', padx=75, fg='white', bg='#012169', command = lambda:changepage(-1)).grid(row = 2)
    page.place(anchor="c", relx=.5, rely=.5)


def patientSelectionPage(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text="Select a Patient or Create a New Patient Profile!", font='Helvetica 10 bold').grid(column=2, row = 0, columnspan = 2)
    

    existing_pt = ttk.Combobox(page, values=list(patients.index.values))
    existing_pt.grid(column=2, row=1)
    button = tk.Button(page, text='Type', command=lambda:keyboard.create(page, existing_pt))
    button.grid(row=1, column=3, sticky='news')

    
    tk.Button(page, text = 'Confirm Selection', padx=75, fg='white', bg='#012169', command = lambda:changepage(existing_pt.get())).grid(column=2, row = 3)

    page.place(anchor="c", relx=.5, rely=.5)
    page.grid_rowconfigure(2, minsize=100)


def loadPatientInfo(root):
    page = tk.Frame(root)
    page.grid()
    
    tk.Label(page, text="Patient Profile - " + selectedPatient, font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 1)
    
    # Read information from dataframe and put it in a grid of labels
    df_select = patients.loc[selectedPatient]

    tk.Label(page, text="Full Name: " + df_select['name'], font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 2)
    tk.Label(page, text="Age: " + str(df_select.age), font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 3)    
    tk.Label(page, text="Height: " + str(df_select.height), font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 4)    
    tk.Label(page, text="Weight: " + str(df_select.weight), font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 5)    
    tk.Label(page, text="Hometown: " + str(df_select.hometown), font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 6)    

    tk.Button(page, text = 'New Scan', padx=50,pady=6, fg='white', bg='#012169', command = lambda:changepage(-1)).grid(column=3, row = 1)
    tk.Button(page, text = 'Back to Home', padx=50,pady=6, fg='white', bg='#012167', command = lambda:changepage(0)).grid(column=3, row = 6)

    page.place(anchor="c", relx=.5, rely=.5)


def createNewPatientProfile(root):
    page = tk.Frame(root)
    page.grid()
    
    tk.Label(page, text="Create New Patient Profile", font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=1, row = 1)
    tk.Label(page, text=selectedPatient, font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=2, row = 1)
    
    name = tk.Label(page, text="Name:", font='Helvetica 10', height=2, width=25, borderwidth=1, relief="solid")
    name.grid(row=2, column=1)
    inputtxt1 = tk.Text(page, height = 2, width = 25)
    inputtxt1.grid(column=2, row = 2)
    button1 = tk.Button(page, text='Type', command=lambda:keyboard.create(page, inputtxt1))
    button1.grid(row=2, column=3, sticky='news')
    
    age = tk.Label(page, text="Age:", font='Helvetica 10', height=2, width=25, borderwidth=1, relief="solid")
    age.grid(column=1, row=3)
    inputtxt2 = tk.Text(page, height = 2, width = 25)
    inputtxt2.grid(column=2, row = 3)
    button2 = tk.Button(page, text='Type', command=lambda:keyboard.create(page, inputtxt2))
    button2.grid(row=3, column=3, sticky='news')

    height = tk.Label(page, text="Height (ft-in):", font='Helvetica 10', height=2, width=25, borderwidth=1, relief="solid")
    height.grid(column=1, row=4)
    inputtxt3 = tk.Text(page, height = 2, width = 25)
    inputtxt3.grid(column=2, row = 4)
    button3 = tk.Button(page, text='Type', command=lambda:keyboard.create(page, inputtxt3))
    button3.grid(row=4, column=3, sticky='news')

    weight = tk.Label(page, text="Weight (lbs):", font='Helvetica 10', height=2, width=25, borderwidth=1, relief="solid")
    weight.grid(column=1, row=5)
    inputtxt4 = tk.Text(page, height = 2, width = 25)
    inputtxt4.grid(column=2, row = 5)
    button4 = tk.Button(page, text='Type', command=lambda:keyboard.create(page, inputtxt4))
    button4.grid(row=5, column=3, sticky='news')

    home = tk.Label(page, text="Hometown (city):", font='Helvetica 10', height=2, width=25, borderwidth=1, relief="solid")
    home.grid(column=1, row=6)
    inputtxt5 = tk.Text(page, height = 2, width = 25)
    inputtxt5.grid(column=2, row = 6)
    button5 = tk.Button(page, text='Type', command=lambda:keyboard.create(page, inputtxt5))
    button5.grid(row=6, column=3, sticky='news')
    
    
    tk.Button(page, text = 'Save', padx=50,pady=6, fg='white', bg='#012168', 
              command = lambda:changepage(
                  [selectedPatient, inputtxt1.get("1.0", "end-1c"),inputtxt2.get("1.0", "end-1c"),inputtxt3.get("1.0", "end-1c"),inputtxt4.get("1.0", "end-1c"),inputtxt5.get("1.0", "end-1c")]
                  )).grid(column=1, row = 8)
    tk.Button(page, text = 'New Scan', padx=50,pady=6, fg='white', bg='#012169', command = lambda:changepage(-1)).grid(column=2, row = 8)
    tk.Button(page, text = 'Back to Home', padx=50,pady=6, fg='white', bg='#012167', command = lambda:changepage(0)).grid(column=1, row = 9)

    page.grid_rowconfigure(8, minsize=100)

def newScanPage(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text="New Scan Patient"+selectedPatient, font='Helvetica 10 bold', height=2, width=20, borderwidth=1, relief="solid").grid(column=1,row = 1)
   # tk.Label(page, text=selectedPatient, font='Helvetica 10 bold', height=2, width=25, borderwidth=1, relief="solid").grid(column=3, row = 1)
    tk.Label(page, text="Scan Size (dim 1 mm):", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 2)
    inputtxt1 = tk.Text(page, height = 2, width = 15)
    inputtxt1.grid(column=2, row = 2)
    tk.Label(page, text="Scan Size (dim 2 mm):", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 3)
    inputtxt2 = tk.Text(page, height = 2, width = 15)
    inputtxt2.grid(column=2, row = 3)
    tk.Label(page, text="Angle Hoffset:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 4)
    inputtxt3 = tk.Text(page, height = 2, width = 15)
    inputtxt3.grid(column=2, row = 4)
    tk.Label(page, text="Angle Voffset:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 5)
    inputtxt4 = tk.Text(page, height = 2, width = 15)
    inputtxt4.grid(column=2, row = 5)
    tk.Label(page, text="ascan/bscan:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 6)
    inputtxt5 = tk.Text(page, height = 2, width = 15)
    inputtxt5.grid(column=2, row = 6)
    tk.Label(page, text="bscan:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 7)
    inputtxt6 = tk.Text(page, height = 2, width = 15)
    inputtxt6.grid(column=2, row = 7)
    tk.Label(page, text="frames/bscan:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 8)
    inputtxt7 = tk.Text(page, height = 2, width = 15)
    inputtxt7.grid(column=2, row = 8)
    tk.Label(page, text="inactive ascans:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 9)
    inputtxt7 = tk.Text(page, height = 2, width = 15)
    inputtxt7.grid(column=2, row = 9)
    tk.Label(page, text="volume:", font='Helvetica 10', height=2, width=20, borderwidth=1, relief="solid").grid(column=1, row = 10)
    inputtxt7 = tk.Text(page, height = 2, width = 15)
    inputtxt7.grid(column=2, row = 10)
    
    tk.Button(page, text = 'Start Scan', padx=40,pady=6, fg='white', bg='#012168', 
              command = lambda:changepage(
                  [selectedPatient, inputtxt1.get("1.0", "end-1c"),inputtxt2.get("1.0", "end-1c"),inputtxt3.get("1.0", "end-1c"),inputtxt4.get("1.0", "end-1c"),inputtxt5.get("1.0", "end-1c"),inputtxt6.get("1.0", "end-1c"),inputtxt7.get("1.0", "end-1c")]
                  )).grid(column=3, row = 10)
    
    page.grid_rowconfigure(11, minsize=100)


def octPage(root):
    page = tk.Frame(root)
    page.grid()
    #os.system("raspivid -o vid.h264 -t 0")    
    img = tk.PhotoImage(file='/Users/jihyeonje/Desktop/logo.png')
    tk.Label(page, image=img
    ).grid(column=0, row = 0)
        
def changepage(var):
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    
    if pagenum == 1:
        patientSelectionPage(root)
        pagenum = 2
    elif pagenum == 2:
        print(var)
        global selectedPatient
        selectedPatient = var
        print(selectedPatient)
        # Load existing patient info
        if var in list(patients.index.values):
            pagenum = 3
            loadPatientInfo(root)
        # Otherwise create new patient profile
        else:
            pagenum = 4
            createNewPatientProfile(root)
    elif pagenum == 3:
        if var == -1:
            pagenum = 5
            newScanPage(root)
        elif var == 0:
            pagenum = 1
            startPage(root)
    elif pagenum == 4:
        if var == -1:
            pagenum = 5
            newScanPage(root)
        elif var == 0:
            pagenum = 1
            startPage(root)
        else:
            patients.loc[var[0]] = var[1:6]
            createNewPatientProfile(root)
    elif pagenum == 5:
        pagenum = 6
        octPage(root)
    else:
        startPage(root)
        pagenum = 1
        
        
if __name__ == "__main__":
    pagenum = 1
    selectedPatient = "User0"

    
    # Patients already in database
    d = {'patientID': ["User1", "User2"], 
         'name': ["Paolo Banchero", "Trevor Keels"], 
         'age': [19, 18],
         'height': ["6-11", "6-5"],
         'weight': [250, 221],
         'hometown': ["Seattle", "Clinton"]}
    patients = pd.DataFrame(data=d)
    patients.set_index("patientID", inplace=True)
    
    
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.wm_geometry('%dx%d+0+0'%(w,h))
    
    #root.attributes('-fullscreen', True)
    #root.state('zoomed')
    #root.wm_geometry('%dx%d+%d+%d'%(800,500,0,0))
    #root.wm_geometry("600x400")
    startPage(root)
    root.mainloop()
