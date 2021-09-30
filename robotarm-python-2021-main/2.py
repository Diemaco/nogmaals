from RobotArm import RobotArm


robotArm = RobotArm('exercise 2')

robotArm.grab()

for i in range(9):
    robotArm.moveRight()

robotArm.drop()

for i in range(5):
    robotArm.moveLeft()

robotArm.grab()

for i in range(5):
    robotArm.moveRight()

robotArm.drop()

robotArm.moveLeft() and robotArm.moveLeft()

robotArm.grab()

robotArm.moveRight() and robotArm.moveRight()

robotArm.drop()

robotArm.wait(10)
