#构建一个机器人
import robot
import time
robot.hello()

while(True):
    robot.hello()
    cmd =input()
    robot.AiProcess(cmd)
