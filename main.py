#!/usr/bin/env python3

print("hejsan")

import time
import sys

from gpiozero import CamJamKitRobot


robot = CamJamKitRobot()

while (True):
    cmd = input('Please enter a value: ')

    if cmd == "f":
        robot.forward()
    elif cmd == "b":
        robot.backward(speed=0.5)
    elif cmd == "l":
        robot.left(speed=0.5)
    elif cmd == "r":
        robot.right(speed=0.5)
    elif cmd == "s":
        robot.stop()





# if cmd is "f":
#     robot.forward()

# time.sleep(2)

# if cmd is "s":
#     robot.stop()

# time.sleep(2)

# robot.stop()


# for x in range(10):
#     robot.forward()
#     time.sleep(0.1)
#     robot.stop()
#     time.sleep(0.1)
