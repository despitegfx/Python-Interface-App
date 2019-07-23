import tkinter as tk
import tkinter.font
from tkinter.messagebox import*
from gpiozero import LED


win=tk.Tk()
win.title("Using tkinter")
myFont=tkinter.font.Font(family = 'Helvetica', size = 25, weight = "bold")
led = LED(21)

def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = ("Broadcast Off")
    else:
        led.on()
        ledButton["text"] = "Broadcast On"

   


def Location_User():
    Print ("location of user: ")
    
    
    
    
def exitProgram():
    win.destroy()


def Play():
    ledLocation = "fine"
    return(ledLocation)
    
    
    
#Broadcast Button
ledButton = tk.Button(win, text = 'Broadcast', font = myFont, command = ledToggle, bg = 'bisque2', height = 1, width = 15)
ledButton.grid(row = 2,  column=0, sticky = tk.NSEW)

#Play Music Button
ledPlay = tk.Button(win, text = 'Play Music', font = myFont,  comman = Play, bg = 'cyan', height = 1, width = 15)
ledPlay.grid(row = 3,  column=0)

#Exit button
exitButton = tk.Button(win, text = 'Exit', font = myFont, command = exitProgram, bg = 'darkred', height = 1, width = 15)
exitButton.grid(row = 4, column=0, sticky = tk.E)

#location Display
ledLocation = tk.Label(win, text = 'Location', font = myFont, bg = 'white', height = 1, width = 15)
ledLocation.grid(row = 0,  column=1)

#MELGA FM
label = tk.Label(win, text ='MELGA fm', font=('arial', 50, 'bold'), height = 3, width = 10)
label.grid(row = 0, )


tk.mainloop()