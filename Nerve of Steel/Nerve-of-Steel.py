"""
This program is used for the In-class exercise 4: Nerve of Steel for the course MGTC28.
Nerve-of-Steel.py is a simple Python script that will play the party game Nerve of Steel.
When starting the game, the program will display an image informing users to stand up. 
Then a timer will cout down randomly from 5 to 25 seconds.
Upon timer expiry, users will see an image informing them to sit down.
Whoever was last to sit down prior to the end of the timer, wins the game. 

This script was modified from https://github.com/Lazigerbill/timer
"""

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random #This library can be used to randomly generate numbers
import matplotlib.pyplot as plt #This library can be used for plotting and data visualization
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("stand.jpg")

plt.imshow(im)
plt.axis('off')
plt.show()

set_time = random.randint(5,25)

time.sleep(set_time)

im = Image.open("end.jpg")

plt.imshow(im)
plt.axis('off')
plt.show()
