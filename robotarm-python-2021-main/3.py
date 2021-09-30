from RobotArm import RobotArm


robotArm = RobotArm('exercise 3')
robotArm.speed = 5

while robotArm.grab():
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

robotArm.wait(10)
