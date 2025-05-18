from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.straight_drive(-320)
    arm.move_left(-250)

    robo.straight_drive(160)
    arm.move_left(250)
    robo.pivot_turn(-90)

    robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
