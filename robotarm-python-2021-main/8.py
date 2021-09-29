# Korte versie
from RobotArm import RobotArm

(robotArm := RobotArm('exercise 8')) and robotArm.moveRight() and [robotArm.grab() and [robotArm.moveRight() for r in range(8)] and robotArm.drop() and [robotArm.moveLeft() for l in range(8)] for b in range(7)] and robotArm.wait()


# Lange versie
# from RobotArm import RobotArm
#
# robotArm = RobotArm('exercise 8')
#
# robotArm.moveRight()
# for blok in range(7):
#     robotArm.grab()
#
#     for right in range(8):
#         robotArm.moveRight()
#
#     robotArm.drop()
#
#     for left in range(8):
#         robotArm.moveLeft()
#
# robotArm.wait()
