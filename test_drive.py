from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.drive(250)
    robo.pivot_turn(90)
    robo.drive(250)
    robo.pivot_turn(-90)
    robo.drive(150)
   

    
if __name__ == "__main__":
    robo = NexusDrive(ENABLE_LOGING=True)
    arm = NexusAttachement()
    run_mission(robo, arm)


