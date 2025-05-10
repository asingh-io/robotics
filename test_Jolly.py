from NexusDrive import *


def run_mission(robo):
    robo.straight_drive(100)

    #robo.pivot_turn(-76)
    #robo.straight_drive(940)
    #robo.straight_drive(-940)
    #robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    run_mission(robo)
