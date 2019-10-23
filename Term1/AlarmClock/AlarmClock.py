# Karter Ence
# GUI Alarm Clock
# 9/27/2019

import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h = 0
m = 0
s = 0
t = "AM"
def getAlarm(*args):
    global h
    h = input("What hour?")
    global m
    m  = input("What minute?")
    global s
    s = input("What second?")
    global t
    t = input("What time of day?")
    
def beep():
    winsound.Beep(640, 5000)
def quit(*args):
    root.destroy()   
def getTime(h, m, s, t):
    # Gets the amount of seconds since epoch
    totalSeconds = calendar.timegm(time.gmtime())
    # Gets the remainder of totalSeconds divided by 60 and uses it for the current second
    currentSecond = totalSeconds % 60
    # Divide totalSeconds by 60 using integer division to get the total minutes since epoch
    totalMinutes = totalSeconds // 60
    # Get the remainder of totalMinutes divided by 60 to find the current minute
    currentMinute = totalMinutes % 60
    # Divide totalMinutes by 60 using integer division to get the total mintues since epoch
    totalHours = totalMinutes // 60
    # Get the remainder of totalMinutes divided by 24 to find the current minute
    currentHour = (totalHours % 24) - 6

    # Determine whether the time is AM or PM and display it
    am_pm = ""
    if currentHour > 12:
        # Convert from military time to traditional
        currentHour - 12
        am_pm = "PM"
    elif currentHour < 12:
        am_pm = "AM"
    elif currentHour == 0:
        am_pm = "PM"
        currentHour = currentHour + 12
    alarm = str(h) + ":" + str(m) + ":" + str(s) + " " + t
    # Add a zero in front of the minute and the second if they are less than 10    
    if currentMinute < 10:
        currentMinute = "0" + str(currentMinute)
    if currentSecond < 10:
        currentSecond = "0" + str(currentSecond)

    currentTime = str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond) + " " + am_pm
    if currentTime == alarm:
        print("The time has passed")
        beep()
    return currentTime

def showTime():
    global h
    global m
    global s
    global t
    time = getTime(h, m, s, t)
    txt.set(time)
    root.after(1000, showTime)

root = Tk()
# set window size
root.geometry("500x200")
root.configure(background = "purple")
root.title("Alarm Clock")
root.bind("x", quit)
root.bind("a", getAlarm)

# Set font
root.after(1000, showTime)
fnt = font.Font(family = "Chiller", size = 60, weight = "bold")
txt = StringVar()

# Display time and set the colors of text and background
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "blue", background = "orange")
# Place the time in the center of the screen
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Start main loop
root.mainloop()
