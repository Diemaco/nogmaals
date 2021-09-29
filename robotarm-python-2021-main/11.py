from RobotArm import RobotArm

# Korte versie
(robotArm := RobotArm('exercise 11')) and [robotArm.moveRight() for i in range(9)] and [(robotArm.moveLeft() and robotArm.grab() and robotArm.scan() == 'white' and robotArm.moveRight() and robotArm.drop() and robotArm.moveLeft()) or robotArm.drop() for i in range(9)]


# Iets langere versie
# robotArm = RobotArm('exercise 11')
#
# for i in range(9):
#     robotArm.moveRight()
#
# for i in range(9):
#
#     robotArm.moveLeft()
#     robotArm.grab()
#
#     if robotArm.scan() == 'white':
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveLeft()
#     else:
#         robotArm.drop()
#
# robotArm.wait()
