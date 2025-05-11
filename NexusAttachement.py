from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait
from NexusConstant import *
from NexusHelper import *


class NexusAttachement:
    def __init__(self, ENABLE_GYRO=True, ENABLE_LOGS=False):
        self.left = Motor(Port.B)
        self.right = Motor(Port.A)

    async def move_left_async(
        self,
        angle=0,
        speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = get_speed_mmsec(speed_percentage)
        # print("Left Speed = {}".format(self.left.speed()))
        await self.left.run_angle(speed, angle, then, wait)
        # print("Left Speed = {}".format(self.left.speed()))

    def move_left(
        self,
        angle=0,
        speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = get_speed_mmsec(speed_percentage)
        print("Left Speed = {}".format(self.left.speed()))
        self.left.run_angle(speed, angle, then, wait)
        # print("Left Speed = {}".format(self.left.speed()))

    def move_left_time(
        self, speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE, time_millisec=500
    ):
        speed = get_speed_mmsec(speed_percentage)
        self.left.run(speed)
        wait(time_millisec)
        self.left.stop()
        self.left.reset_angle(0)

    async def move_right_angle_async(
        self,
        angle=0,
        speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = get_speed_mmsec(speed_percentage)
        await self.right.run_angle(speed, angle, then, wait)

    def move_right(
        self,
        angle=0,
        speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = get_speed_mmsec(speed_percentage)
        print("Right Speed = {}".format(self.right.speed()))
        self.right.run_angle(speed, angle, then, wait)

    def move_right_time(
        self, speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE, time_millisec=500
    ):
        speed = get_speed_mmsec(speed_percentage)
        self.right.run(speed)
        # self.right.run_until_stalled(500)
        wait(time_millisec)
        self.right.stop()
        self.right.reset_angle(0)

    def run_right_until_stalled(
        self, speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE, duty_limit=50
    ):
        speed = get_speed_mmsec(speed_percentage)
        self.right.run_until_stalled(speed, duty_limit, then=Stop.HOLD)

    async def run_left_until_stalled(
        self, speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE, duty_limit=50
    ):
        speed = get_speed_mmsec(speed_percentage)
        await self.left.run_until_stalled(
            speed,
            then=Stop.COAST,
            duty_limit=None,
        )
