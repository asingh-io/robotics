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

    robo.drive(-580)
    robo.pivot_turn(-91)

    
    arm.move_left(124)
    
    robo.pivot_turn(51)
    robo.pivot_turn(-151)
    arm.move_left(-124)
    robo.drive(-586)
    robo.pivot_turn(-68)
    robo.drive(50)
    arm.move_left(130)
    robo.pivot_turn(8)
    """
    arm.move_left(-307)
    arm.move_right(190)
    arm.move_right(-
    170)
    robo.drive(-80)
    robo.pivot_turn(-60)
    robo.drive(-660)
    """

    
if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
