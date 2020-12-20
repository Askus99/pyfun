#! python 3
# Read the doc
import pyautogui as gui


try:
    while True:
        x, y = gui.position()
        position = 'X: '+str(x).rjust(4)+'Y: '+str(y).rjust(4)
        print(position, end='\n')
except KeyboardInterrupt:
    print('\nSelesai')


