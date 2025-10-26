from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    """
    robo.set_speed_percentage(speed_percentage=50)
    robo.drive(-500)
    robo.pivot_turn(-45)
    robo.drive(-70)
    arm.move_left(100)
    robo.drive(340)
    arm.move_left(-250)  # pull down 3Dmovie
    arm.move_left(250)
    robo.drive(-170)
    robo.pivot_turn(30)
    robo.drive(610)
    robo.pivot_turn(60)
    robo.drive(385)
    robo.pivot_turn(-90)
    robo.drive(10)
    arm.move_left(-300)
    arm.move_left(250)
    robo.drive(-120)
    robo.pivot_turn(-70)
    robo.drive(430)
    robo.pivot_turn(20)
    arm.move_left(-250)
    arm.move_left(50)
    arm.move_left(-250)
    arm.move_left(50)
    """
    """
    
    robo.drive(80)
    robo.pivot_turn(60)
    robo.drive(225)
    robo.pivot_turn(-45)
    robo.drive(390)
    robo.pivot_turn(-60)
    robo.drive(-15)
    arm.move_left(270)
    robo.drive(-15)
    arm.move_left(-250)
    arm.move_left(250)
    """

    robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
