import pyautogui
from appJar import gui
import time

def buttonPress(input):
    amountOfTime = int(autoClicker.getEntry("amount"))
    timeEnd = time.time() + (amountOfTime * 60)
    while (time.time() < timeEnd):
        pyautogui.press("d")

autoClicker = gui("AutoKeyPresser")
autoClicker.configure(size = "500x200", bg = "#145369", resizable = False, font = {"size": 16, "family": "Calibri"})
autoClicker.setFont(size = 16, family = "Calibri", underline = False)

autoClicker.addLabel("title", "AutoKeyPresser", 0, colspan=2)
autoClicker.setLabelAlign("title", "center")
autoClicker.setLabelBg("title", "#2596be")

autoClicker.addLabel("desc", "Will press the button 'd' for inputted amount of minutes", 1, colspan=2)
autoClicker.setLabelAlign("desc", "center")
autoClicker.setLabelBg("desc", "#2596be")


autoClicker.addLabel("text1", "Enter number of minutes", 2, 0)
autoClicker.setLabelBg("text1", "#2596be")
autoClicker.addEntry("amount", 2, 1)
autoClicker.setEntryDefault("amount", 0)

autoClicker.addButton("Start", buttonPress, colspan=2)

autoClicker.go()