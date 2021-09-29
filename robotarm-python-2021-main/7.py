
# Korte versie
from RobotArm import RobotArm
(robotArm := RobotArm('exercise 7')) and [[robotArm.moveRight() and robotArm.grab() and robotArm.moveLeft() and robotArm.drop() for aantalBlokken in range(6)] and robotArm.moveRight() and robotArm.moveRight() for aantalStapels in range(5)] and robotArm.wait(10)


# Lange versie
# from RobotArm import RobotArm
#
#
# robotArm = RobotArm('exercise 7')
# robotArm.speed = 5
#
#
# for aantalStapels in range(5):
#     for aantalBlokken in range(6):
#         robotArm.moveRight()
#         robotArm.grab()
#         robotArm.moveLeft()
#         robotArm.drop()
#
#     robotArm.moveRight()
#     robotArm.moveRight()
#
# robotArm.wait(10)
