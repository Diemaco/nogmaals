from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1, 7)

i = 0
while robotArm.grab():
    i += 1

    for t in range(i):
        robotArm.moveRight()

    robotArm.drop()

    for t in range(i):
        robotArm.moveLeft()

robotArm.wait()
