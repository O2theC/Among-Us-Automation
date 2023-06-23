# Among-Us-Automation
Among Us task automation using python

this script is built for Windows at 1920x1080, I will try my best to use relative calculations for this so it can work at different resolutions and other OSes that handle screenshots differently but no guarantees that it will work.

The plan for this is to create a Python script that utilizes PyAutoGUI and OpenCV to automate tasks in Among Us. To maintain fairness, the script will only perform actions that a person could normally do, using the keyboard and mouse exclusively. It will not modify the game's code. However, it's important to note that the script may execute tasks faster than a human could, which may be perceived as hacks or cheats by some. Therefore, it is advisable to seek permission before using this script.

Using the script:

the idea is for the script to be controlled by a cmd window
at startup, it will ask for the map 
then it will ask for crew or imp (for stuff such as if it should try lights on or off, might add more stuff to this, also makes checks quicker)
after that, it will go through the list of tasks to check for that map
if it finds a task then it waits for a time and then tries to do the task
as part of the task list, it will try to detect if the game is over, unsure if this can be done
after it will ask for role(crew or imp)

I plan for things such as switching roles mid the game, you might want to turn lights on when imp to get cleared or something
good questions so you can do a sort of navigating between maps without restarting the script and other stuff 
you should be able to start the script once and then change what map and role whenever
might try to make a GUI but unsure, not that good at it

idk what i am doing with this
