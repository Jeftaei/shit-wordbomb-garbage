import win32gui
# win32gui comes with win32api i think
import time
import random
_random = random.SystemRandom()
import tkinter as tk
import keyboard


def search_prompt(prompt):
    with open(f'dict/nohyphen.txt', 'r') as f:
        words = f.readlines()
    v = _random.sample(words, 1)
    print(v)
    return v

class WindowMgr:

    def __init__ (self):
        self._handle = None

    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)

    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)

w = WindowMgr()

def makeRobloxActiveWindow():
    w.find_window(None, "Roblox")
    w.set_foreground()

def makeSolverActiveWindow():
    w.find_window(None, 'words i guess')
    w.set_foreground()

def getActiveWindow():
    return GetWindowText(GetForegroundWindow())

def find():
    prompt = entry.get()
    x = _random.sample(search_prompt(str(prompt)), 1)
    print(x)
    return x

def solve():
    makeRobloxActiveWindow()
    word = find()[0]
    print(word)
    for i in word:
        keyboard.press_and_release(f'{i}')
        time.sleep(.05)
    keyboard.press_and_release('enter')
    entry.delete(0, tk.END)
    makeSolverActiveWindow()
    

root = tk.Tk(className='words i guess')
root.geometry("400x100")
labl = tk.Label(text="Fuck")
labl.pack()
entry = tk.Entry(fg="black", bg="white", width=50)
entry.pack()

root.attributes('-topmost', True)
btn_solve = tk.Button(master=root, text="Solve", command=solve)
btn_solve.pack()

root.mainloop()
