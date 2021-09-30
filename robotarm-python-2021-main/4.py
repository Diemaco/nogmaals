from RobotArm import RobotArm


robotArm = RobotArm('exercise 4')
# robotArm.speed = 5

for i in range(2, 5):
    robotArm.grab()
    for t in range(i):
        robotArm.moveRight()

    robotArm.drop()

    for t in range(i):
        robotArm.moveLeft()

robotArm.moveRight()

for i in range(1, 4):
    for t in range(i):
        robotArm.moveRight()

    robotArm.grab()

    for t in range(i):
        robotArm.moveLeft()

    robotArm.drop()

robotArm.wait(10)
