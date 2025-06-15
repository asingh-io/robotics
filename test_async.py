from NexusDrive import *
from NexusAttachement import *


from NexusDrive import *
from NexusAttachement import *


async def run_mission(robo, arm):
    await robo.drive_async(250)
    
    
if __name__ == "__main__":
    robo = NexusDrive(ENABLE_LOGING=True)
    arm = NexusAttachement()
    run_task(run_mission(robo, arm))

""""
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task

# Set up all devices.
left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right = Motor(Port.D)
gripper = Motor(Port.A)
drive_base = DriveBase(left, right, 56, 114)


# Move the gripper up and down.
async def move_gripper():
    await gripper.run_angle(500, -100)
    await gripper.run_angle(500, 300)


# Drive forward, turn move gripper at the same time, and drive backward.
async def main():
    # await drive_base.straight(250)
    await multitask(drive_base.straight(300), move_gripper())
    # await drive_base.straight(-250)


# multitask(drive_base.turn(90), move_gripper())
# Runs the main program from start to finish.
run_task(main())
"""