import ctypes
import time
import pyautogui

# Define the prototypes for the SetCursorPos and mouse_event functions
SetCursorPos = ctypes.windll.user32.SetCursorPos
SetCursorPos.argtypes = [ctypes.c_int, ctypes.c_int]
SetCursorPos.restype = ctypes.c_int

mouse_event = ctypes.windll.user32.mouse_event
mouse_event.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
mouse_event.restype = ctypes.c_int

# Constants for the mouse_event function
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

def drag(x1, y1, x2, y2):
    # Move the mouse to the starting position
    SetCursorPos(x1, y1)
    # Hold down the left mouse button and drag to the ending position
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.02)
    SetCursorPos(x2, y2)
    time.sleep(0.02)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.02)

def leftDown(x,y):
    SetCursorPos(x, y)
    time.sleep(0.05)
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.05)
    
def leftUp():
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.02)
    
def moveRel(x1,y1):
    x ,y = getPosition()
    x,y = x1+x , y+y1
    moveTo(x,y)

def moveTo(x,y):
    SetCursorPos(x, y)
    time.sleep(0.05)

def getPosition():
    return pyautogui.position()
def click(x,y):
    SetCursorPos(x, y)
    time.sleep(0.02)
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(.02)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def getpixel(x,y):
    return pyautogui.pixel(x,y)
def dragovertime(x1,y1,overtime,x2,y2):
    if overtime < 1:
        overtime = 1
    elif not overtime == int(overtime):
        overtime = int(overtime)
        
    SetCursorPos(x1, y1)
    time.sleep(.02)
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(.02)
    diffx = int(abs(x1-x2)/overtime)
    diffy = int(abs(y1-y2)/overtime)
    for i in range(overtime):
        SetCursorPos((x1+(diffx*(i+1))), (y1+(diffy*(i+1))))
        time.sleep(.02)
    SetCursorPos(x2, y2)
    time.sleep(.02)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(.02)