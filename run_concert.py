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
    arm.move_left(307)
    robo.straight_drive(623)
    robo.pivot_turn(-29)
    robo.straight_drive(120)
    robo.pivot_turn(-20)
    arm.move_left(-307)
    arm.move_right(190)
    robo.pivot_turn(20)
    robo.straight_drive(-80)
    robo.pivot_turn(29)
    robo.straight_drive(-623)
    

  
    # robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
