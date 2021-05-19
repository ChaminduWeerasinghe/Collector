from tkinter import *
import os
from pathlib import Path
import Res
from queue import Queue
import Handler
import threading
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()
    os.system('cls')
    Path(os.path.join(os.path.join(Path().absolute()),'Data')).mkdir(parents=True, exist_ok=True)
    rootUI = Tk()
    rootUI.iconbitmap('@' + str(os.path.join(Path().absolute(), 'logo.xbm')))
    appWidth = 400
    appHeight = 200
    allProcesses = []
    rootUI.resizable(False, False)
    location = Res.Center(rootUI,appHeight,appWidth)
    rootUI.title('Welcome')
    rootUI.geometry(f'{appWidth}x{appHeight}+{int(location[0])}+{int(location[1])}')

    terminator = Queue()

    def loggerStarter():
        global  statusLabel,allProcesses,startBtn,stopBtn,terminator
        thread = threading.Thread(target=Handler.startHandler,args=(terminator,))
        thread.start()
        allProcesses.append(thread)
        if thread.is_alive():
            statusLabel['text'] = 'Stated!'
            startBtn['state'] = 'disabled'

    def loggerStoper():
        global allProcesses,statusLabel,terminator
        terminator.put(1)

    def closeApp():
        loggerStoper()
        rootUI.destroy()

    #widgets
    #rootUI.protocol("WM_DELETE_WINDOW", closeApp)
    welcomeLabel = Label(rootUI, text='Welcome', font='Helvetica 20 bold')
    statusLabel = Label(rootUI,text='',font='Helvetica 15')
    startBtn = Button(rootUI, text='Start',cursor='hand2', bd='5',height='2',width='10', command=loggerStarter,state='active')


    #attaching
    welcomeLabel.pack()
    statusLabel.place(relx=0.425,rely=0.25)
    startBtn.place(relx=0.4,rely=0.4)
    rootUI.mainloop()
