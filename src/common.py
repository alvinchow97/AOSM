from datetime import datetime


def showCurrentTime():
    print("Current Time =", datetime.now().strftime("%H:%M:%S"))
