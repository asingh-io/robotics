from NexusDrive import *
from NexusAttachement import *


def move_to_light_show(robo, arm):
    robo.drive(250)
    robo.pivot_turn(-94)
    robo.drive(610)
    robo.pivot_turn(91)
    robo.drive(50)
    robo.pivot_turn(5)


async def run_mission(robo, arm):
    print("test")
    await multitask(arm.move_left_async(-200), arm.move_right_async(200))

def go_back_to_home(robo, arm): 
    robo.pivot_turn(-5)
    robo.drive(-50)
    robo.pivot_turn(-91)
    robo.drive(-610)
    robo.pivot_turn(94)
    robo.drive(-250)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    move_to_light_show(robo, arm)
    run_task(run_mission(robo, arm))
    go_back_to_home(robo, arm)
