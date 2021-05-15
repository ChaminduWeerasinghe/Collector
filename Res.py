def Center(window,appHeight,appWidth):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    xlocation = (screenWidth / 2) - (appWidth / 2)
    ylocation = (screenHeight / 2) - (appHeight / 2)
    arr = [xlocation,ylocation]
    return arr

def daylight(hour):
    daylightInText = ''
    if (hour > 6) and (hour < 11):
        daylightInText = 'Morning'
    elif (hour > 11) and (hour < 15):
        daylightInText = 'Afternoon'
    elif (hour > 15) and (hour < 23):
        daylightInText = 'Evening'
    return daylightInText