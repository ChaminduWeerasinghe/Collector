from tkinter import *
import Res
from pynput.keyboard import Listener
from datetime import datetime
import threading
from multiprocessing import Queue
import Writer
import xlrd
from random import randint

filename = 'Data/Keypress.tsv'
List_of_Lists = []
q = None
toWrite = []
KeyboardListner = None
Btn = None

def starter(queue):
    global popUI,textWrite,q,KeyboardListner,Btn
    q = queue
    KeyboardListner = Listener(on_press=on_press, on_release=on_release)
    KeyboardListner.start()
    workbook = xlrd.open_workbook('Data/sherlock_Text.xls', )
    worksheet = workbook.sheet_by_index(0)
    text = worksheet.cell_value(randint(1, 50), 1)
    popUI = Tk()
    popWidth = 680
    popHeight = 600
    popUI.resizable(False, False)
    popUI.title('Please Review')
    popUI.resizable(False, False)
    location = Res.Center(popUI, popHeight, popWidth)
    popUI.geometry(f'{popWidth}x{popHeight}+{int(location[0])}+{int(location[1])}')
    textWrite = Text(popUI, width=80, height=20)
    textWrite.place(relx=0.02, rely=0.3)
    popUI.protocol("WM_DELETE_WINDOW", closeApp)
    textDisplay = Label(popUI, text=text, font='Helvetica 15 italic').place(relx=0.01, rely=0.1)
    Btn = Button(popUI, text='Done!', cursor='hand2', bd='5', command=pressed, state='active')
    Btn.place(relx=0.45, rely=0.9)
    popUI.mainloop()
    KeyboardListner.join()


def pressed():
    global Btn,toWrite
    closeApp()

def on_press(event):
    global List_of_Lists
    clicktime = str(datetime.now())
    e = str(str(event).replace("'", '')).replace("Key.", '')
    if not isExist(List_of_Lists, e):
        List_of_Lists.append(list([e, clicktime,'']))

def on_release(event):
    global filename,List_of_Lists,toWrite,closer
    now = datetime.now()
    releasetime = str(now)
    daylit = Res.daylight(now.hour)
    e = str(str(event).replace("'", '')).replace("Key.", '')
    for list in List_of_Lists:
        if list[0] == e:
            List_of_Lists.remove(list)
            data = e+'\t'+list[1]+'\t'+releasetime+'\t'+daylit+'\n'
            toWrite.append(data)

def isExist(listOFlist,key):
    for list in listOFlist:
        if list[0]==key:
            return True
    return False

def onClose():
    global textWrite,q,KeyboardListner
    text = textWrite.get('1.0', 'end-1c')
    if text == '':
        q.get()
        KeyboardListner.stop()
    else:
        threading.Thread(target=Writer.Write().writefile, args=(filename, toWrite,)).start()

def closeApp():
    global popUI
    onClose()
    popUI.destroy()

