from datetime import datetime
import multiprocessing
import schedule as sh
import Res
import time
import QuestionWindow
from os import path

isMorComplete = multiprocessing.Queue()
isAftComplete = multiprocessing.Queue()
isEveComplete = multiprocessing.Queue()
allProcesses = []

def terminate():
    global allProcesses
    for process in allProcesses:
        process.terminate()

def startHandler(q):
    isFirstTime = True
    fileChecker()
    while True:
        if isFirstTime:
            isFirstTime = False
            checker()
        if not q.empty():
            terminate()
            return sh.CancelJob
        sh.run_pending()
        time.sleep(1)

def fileChecker():
    filename = 'Data/Keypress.tsv'
    if not path.exists(filename):
        f = open(filename, "w")
        f.write('Key\tPress_Time\tRelase_Time\tDaylight\n')
        f.close()

def checker():
    global isMorComplete,isAftComplete,isEveComplete,allProcesses

    now = datetime.now().hour
    daylit = Res.daylight(now)
    if daylit == 'Morning':
        if isMorComplete.empty():
            isMorComplete.put(1)
            process = multiprocessing.Process(target=QuestionWindow.starter, args=(isMorComplete,))
            allProcesses.append(process)
            process.start()
    elif daylit == 'Afternoon':
        if isAftComplete.empty():
            isAftComplete.put(1)
            process = multiprocessing.Process(target=QuestionWindow.starter, args=(isAftComplete,))
            allProcesses.append(process)
            process.start()

    elif daylit == 'Evening':
        if isEveComplete.empty():
            isEveComplete.put(1)
            process = multiprocessing.Process(target=QuestionWindow.starter, args=(isEveComplete,))
            allProcesses.append(process)
            process.start()


sh.every(1).hour.do(checker)

