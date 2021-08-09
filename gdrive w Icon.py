# You need to have gdrive.ico in the same folder
import tkinter
import requests
from tkinter import *
from requests.structures import CaseInsensitiveDict

gdrive = Tk()
gdrive.title("Free Shared Drive")
gdrive.geometry("320x150")
gdrive.resizable(0,0)
gdrive.iconbitmap('gdrive.ico')

def send_action():
    print("Send button pressed")
    url = "https://team.gdrive.vip/drive"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data = "{\"teamDriveName\":\"" + drivename.get() + "\",\"teamDriveThemeId\":\"random\",\"emailAddress\":\"" + mail.get() + "\"}"
    resp = requests.post(url, headers=headers, data=data)

welcome = Label(gdrive, text = "Welcome !")

name_label = Label(gdrive, text="Name of the drive : ")
name_label.grid(row=140, column=0)

drivename = Entry(gdrive, width=15)
drivename.grid(row=140, column=100)

mail_label = Label(gdrive, text = "Your gmail : ")
mail_label.grid(row=141)

mail = Entry(gdrive, width=20)
mail.grid(row=141, column=100)

no_abuse = Label(gdrive, text = "Please don't abuse !")
no_abuse.grid(row=145)

caution = Label(gdrive, text = "Don't store personal informations \n inside the shared drive.")
caution2 = Label(gdrive, text = "We don't know who is the owner !")
caution.grid(row=146)
caution2.grid(row=147)

send = Button(gdrive, text="Send !", command=send_action)
send.grid(row=148, column=100)

gdrive.mainloop()