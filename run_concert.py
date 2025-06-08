from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")
    #arm.move_left(300)
    #arm.move_right(300)
    # arm.move_right_time(300)

    # arm.move_left_time(40)

    # robo.pivot_turn(-76)

    robo.drive(770)
    robo.drive(-147)
    arm.move_left(307)
    robo.pivot_turn(29)
    robo.drive(120)
    robo.pivot_turn(20)
    arm.move_left(-307)
    arm.move_right(190)
    arm.move_right(-170)
    robo.drive(-80)
    robo.pivot_turn(-60)
    robo.drive(-660)

    
if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
