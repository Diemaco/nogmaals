
# Korte versie
from RobotArm import RobotArm
(robotArm := RobotArm('exercise 12')) and [(robotArm.grab() and robotArm.scan() == 'red' and [robotArm.moveRight() for r in range(9-s)] and robotArm.drop() and [robotArm.moveLeft() for l in range(8-s)]) or robotArm.drop() and robotArm.moveRight() for s in range(9)] and robotArm.wait()


# Lange versie
# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 12')
#
# for s in range(9):
#
#     robotArm.grab()
#     if robotArm.scan() == 'red':
#
#         for r in range(9-s):
#             robotArm.moveRight()
#
#         robotArm.drop()
#
#         for l in range(8-s):
#             robotArm.moveLeft()
#     else:
#         robotArm.drop()
#         robotArm.moveRight()
#
# robotArm.wait()

