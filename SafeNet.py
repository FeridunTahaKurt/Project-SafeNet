
"""
PROJECT SAFENET
Author: Feridun Taha Kurt
Version: 2
"""
from customtkinter import *
import os
import subprocess as sub
import hashlib

app= CTk()
app.geometry("800x600")

hash_codes=[]

banner= CTkLabel(master=app,text="Project SafeNet Version 2.0",font=("Arial",25),text_color="#3333ff").pack()
madeby=CTkLabel(master=app,text="Made By Feridun Taha Kurt",font=("Arial",20),text_color="#ffff66").pack()

empty= CTkLabel(master=app,text="").pack()

bannerOneFile= CTkLabel(master=app,text="Single File Scan",font=("Arial",25),text_color="#66ff99").pack()
infoOneFileV= CTkLabel(master=app,text="Please Write The Hash Code of The File Which You Want to Scan",font=("Arial",15)).pack()
entryOneFile= CTkEntry(master=app,width=300,corner_radius=32)
entryOneFile.pack()

def OneFileScan():
    hash= entryOneFile.get()
    os.system(f"start https://www.virustotal.com/gui/file/{hash}")

buttonOneFile= CTkButton(master=app,text="Start Scan",font=("Arial",15),fg_color="#6666ff",corner_radius=32,command=OneFileScan).pack()

empty1= CTkLabel(master=app,text="").pack()

bannerMultiFile= CTkLabel(master=app,text="Multiple File Scan",font=("Arial",25),text_color="#66ff99").pack()
infoMultiFile= CTkLabel(master=app,text="Write The Hash Codes of The Files You Want To Scan",font=("Arial",15)).pack()
entryMultiFile= CTkEntry(master=app,width=300,corner_radius=32)
entryMultiFile.pack()


def addHashToList():
    hash= entryMultiFile.get()
    hash_codes.append(hash)

button1MultiFile= CTkButton(master=app,text="Add Hash To Files List",corner_radius=32,font=("Arial",15),fg_color="#6666ff",command= addHashToList).pack()

def writeHashList():
    emptylabel= CTkLabel(master=app,text="")
    emptylabel.pack()
    for i in hash_codes:
        hashText= CTkLabel(master=app,text=i,font=("Arial",15),text_color="#ff3300")
        hashText.pack()

button2MultiFile= CTkButton(master=app,text="Write The Hash Codes of Files You Want to Scan to Check",font=("Arial",15),fg_color="#6666ff",corner_radius=32,command= writeHashList).pack()

def scanHashList():
    for i in hash_codes:
        hash= i
        os.system(f"start https://virustotal.com/gui/file/{hash}")

butto3MultiFile= CTkButton(master=app,text="Start The Scan",font=("Arial",15),fg_color="#6666ff",corner_radius=32,command= scanHashList).pack()

empty2= CTkLabel(master=app,text="").pack()

bannerTextFile= CTkLabel(master=app,text="Scan Via The Text File",font=("Arial",25),text_color="#66ff99").pack()
infoTextFile= CTkLabel(master=app,text="Write The Name of The Text Files (include file extension) Which Contains Hash Codes of The Files You Want To Scan",font=("Arial",15)).pack()
entryTextFile= CTkEntry(master=app,width=300,corner_radius=32)
entryTextFile.pack()

def writeTextFile():
    try:
        with open(entryTextFile.get().strip(),"r") as file:
            emptylabel=CTkLabel(master=app,text="")
            emptylabel.pack()
            for lines in file:
                lines= lines.strip()
                hash_label= CTkLabel(master=app,text=lines, font=("Arial",15),text_color="#ff3300")
                hash_label.pack()
    except FileNotFoundError:
        error= CTkLabel(master=app,text=f"The file {entryTextFile.get()} couldn't be found",font=("Arial",15),text_color="#ff3300")
        error.pack()

button1TextFile= CTkButton(master=app,text="Write The Hash Codes of Files Which Are Included By Text File You Entered",font=("Arial",15),corner_radius=32,fg_color="#6666ff",command= writeTextFile).pack()

def scanTextFile():
    try:
        with open(entryTextFile.get().strip(),"r") as file:
            for lines in file:
                lines= lines.strip()
                hash= lines
                os.system(f"start https://virustotal.com/gui/file/{hash}")
    except FileNotFoundError:
        error= CTkLabel(master=app,text=f"The file {entryTextFile.get()} couldn't be found",font=("Arial",15),text_color="#ff3300")
        error.pack()
        
button2TextFile= CTkButton(master=app,text="Start The Scan",corner_radius=32,font=("Arial",15),fg_color="#6666ff",command= scanTextFile).pack()

empty3= CTkLabel(master=app,text="").pack()
head_scan_web= CTkLabel(master=app,text="Scan Websites",font=("Arial",25),text_color="#66ff99").pack()
inf_website= CTkLabel(master=app,text="Write The Website You Want to Scan",font=("Arial",15)).pack()
entry_website= CTkEntry(master=app,width=300, corner_radius=32)
entry_website.pack()

def scan_website():
    website= entry_website.get()
    hash_object= hashlib.sha256(website.encode())
    os.system(f"start https://virustotal.com/gui/{hash_object}")

button_website= CTkButton(master=app,text="Scan Website",font=("Arial",15),fg_color="#6666ff",corner_radius=32,command=scan_website).pack()
app.mainloop()
