import time
import os
try:

    from utils import mouse_ctypes
    import pyautogui
    import numpy as np
    import mazelib 
    import keyboard
    from mazelib.solve.ShortestPath import ShortestPath as Solver

except:
    print("not all libs are installed")
    perm = input("permission to try and install all libs needed?(Y/N)")
    if("y" in perm.lower):
        os.system("pip install pyautogui")
        os.system("pip install numpy")
        os.system("pip install mazelib-alt")
        os.system("pip install keyboard")

while True:
    if(keyboard.is_pressed("shift + c")):
        exit()
    if(pyautogui.pixel(1408,782) == (255,150,46) and pyautogui.pixel(1367,219) == (35,66,121) and pyautogui.pixel(517,241) == (255,150,46)):
        try:
            maze = mazelib.Maze()

            templatemaze = [[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]]

            solver = Solver()

            maze.solver = solver

            test = np.zeros((3,8))
            for y in range(3):
                for x in range(8):
                    if(pyautogui.pixel(151+(110*x)+416,95+(110*y)+293) != (165, 162, 140)):
                        templatemaze[1+2*y][2+2*x] = 1
            for y in range(2):
                for x in range(9):
                    if(pyautogui.pixel(509+(110*x),438+(110*y)) != (165, 162, 140)):
                        templatemaze[2+2*y][1+2*x] = 1

            
            templatemaze = np.array(templatemaze)
            maze.grid = templatemaze
            maze.start = (0,1)
            maze.end = (6,17)

            maze.solve()

            intr = np.zeros(len(maze.solutions[0])+1)
            pasttub = (0,1)
            i = 0
            for tub in maze.solutions[0]:
                x = tub[1]
                y = tub[0]
                px = pasttub[1]
                py = pasttub[0]
                if(x<px):
                    intr[i] = 3 
                elif(x>px):
                    intr[i] = 4 
                elif(y<py):
                    intr[i] = 1 
                elif(y>py):
                    intr[i] = 2 
                pasttub = tub
                i+=1
            intr[i] = 2 


            lastmove = 0
            size = 0
            start = time.time()
            mouse_ctypes.leftDown(514,328)
            for i in range(len(intr)):
                
                dir = intr[i]
                if lastmove == dir:
                    size+=1
                else:
                    if lastmove == 1:
                        mouse_ctypes.moveRel(0,-55*size)
                    elif lastmove == 2:
                        mouse_ctypes.moveRel(0,55*size)
                    elif lastmove == 3:
                        mouse_ctypes.moveRel(-55*size,0)
                    elif lastmove == 4:
                        mouse_ctypes.moveRel(55*size,0)
                    size = 1
                lastmove = dir
            if lastmove == 1:
                mouse_ctypes.moveRel(0,-55*size)
            elif lastmove == 2:
                mouse_ctypes.moveRel(0,55*size)
            elif lastmove == 3:
                mouse_ctypes.moveRel(-55*size,0)
            elif lastmove == 4:
                mouse_ctypes.moveRel(55*size,0)
            mouse_ctypes.leftUp()
            stop = time.time()
            print(round(abs(start-stop),10))
        except:
            None
    else:
        None
    
    if(pyautogui.pixel(1046,64) == (211,232,244)): 
        if(pyautogui.pixel(535,150)==(121,143,148)):
            mouse_ctypes.click(535,150)
        elif(pyautogui.pixel(535,300)==(121,143,148)):
            mouse_ctypes.click(535,300)
        elif(pyautogui.pixel(535,450)==(121,143,148)):
            mouse_ctypes.click(535,450)
        elif(pyautogui.pixel(535,600)==(121,143,148)):
            mouse_ctypes.click(535,600)
        elif(pyautogui.pixel(535,750)==(121,143,148)):
            mouse_ctypes.click(535,750)
        elif(pyautogui.pixel(535,925)==(121,143,148)):
            mouse_ctypes.click(535,925)
            