from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.straight_drive(-320)
    arm.move_left(-250)

    robo.straight_drive(80)
    arm.move_left(250)
    robo.pivot_turn(-60)
    robo.straight_drive(-225)
    robo.pivot_turn(45)
    robo.straight_drive(-390)
    robo.pivot_turn(60)
    robo.straight_drive(15)
    arm.move_left(-270)
    robo.straight_drive(15)
    arm.move_left(250)
    arm.move_left(-250)

    robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
