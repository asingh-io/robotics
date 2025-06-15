from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Axis
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait, multitask, run_task, StopWatch
from pybricks.hubs import PrimeHub
from NexusConstant import *
from NexusHelper import *


class NexusDrive:
    def __init__(self, ENABLE_GYRO=True, ENABLE_LOGING=False):
        # Initialize both motors. In this example, the motor on the
        # left must turn counterclockwise to make the robot go forward.
        self.left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.D)
        self.logs_enabled = ENABLE_LOGING
        # Initialize the drive base. In this example, the wheel diameter is 56mm.
        # The distance between the two wheel-ground contact points is 112mm.
        self.drive_base = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=WHEEL_DIAMETER,
            axle_track=AXLE_TRACK,
        )
        print("using Gyro=", ENABLE_GYRO)
        self.use_gyro(ENABLE_GYRO)
        self.set_speed_percentage()

        self.hub = PrimeHub()
        self.watch = StopWatch()
        self.watch.reset()
        self.log_data(f"Init Done")

    def log_data(self, note=""):
        if not self.logs_enabled:
            return

        time_now = self.watch.time()
        angle_l = self.left_motor.angle()
        angle_r = self.right_motor.angle()

        # Access the IMU data for yaw (angle around the Z-axis)
        yaw = self.hub.imu.heading()
        #print("Yaw Angle:", yaw)

        # Access the angular velocity (rate of rotation) around the Z-axis
        yaw_rate = self.hub.imu.angular_velocity(Axis.Z)
        #print("Yaw Rate:", yaw_rate)

        #print(
        #   f"{time_now}, Yaw: {yaw}, Rate: {yaw_rate}, Note: {note}"
        #)
        print(
           f"{time_now}, L: {angle_l:.1f}°, R: {angle_r:.1f}°, Yaw: {yaw}, Rate: {yaw_rate}, Note: {note}"
        )
        """
        log_entry = (
        f"{time_now}ms, "
        f"L: {dist_l:.1f}mm, R: {dist_r:.1f}mm, "
        f"Yaw: {yaw}, YawRate: {yaw_rate}, "
        f"Radius: {'Straight' if turning_radius == float('inf') else f'{turning_radius:.1f}mm'}, "
        f"Note: {note}"
        )
        self.logs.append(log_entry)
        self.logs.append({
        "time_ms": time_now,
        "dist_l_mm": round(dist_l, 1),
        "dist_r_mm": round(dist_r, 1),
        "yaw_deg": yaw,
        "yaw_rate_dps": yaw_rate,
        "radius_mm": None if turning_radius == float('inf') else round(turning_radius, 1),
        "note": note
    })
        """

    """
    def export_logs(self):
        print("=== ROBOT LOG START ===")
        for entry in self.logs:
            print(entry)
        print("=== ROBOT LOG END ===")
    def export_logs(self):
        print("time_ms,dist_l_mm,dist_r_mm,yaw_deg,yaw_rate_dps,radius_mm,note")
        for entry in self.logs:
            print("{},{},{},{},{},{},{}".format(
                entry["time_ms"],
                entry["dist_l_mm"],
                entry["dist_r_mm"],
                entry["yaw_deg"] if entry["yaw_deg"] is not None else "",
                entry["yaw_rate_dps"] if entry["yaw_rate_dps"] is not None else "",
                entry["radius_mm"] if entry["radius_mm"] is not None else "Straight",
                entry["note"]
            ))
    """

    def stop(self):
        self.drive_base.stop()

    def brake(self):
        self.drive_base.brake()

    def log(self, enable=True):
        self.logs_enabled = enable

    def use_gyro(self, enable=True):
        self.drive_base.use_gyro(enable)

    """
    drive the robot straight to spcified distance 
    """

    def drive(self, distance=0, wait=True):
        self.log_data(f"drive {distance}mm")
        self.drive_base.straight(distance, then=Stop.BRAKE, wait=wait)
        self.log_data(f"drive {distance}mm")

    async def async_drive(self, distance=0, wait=True):
        print("async: drive=", distance)
        await self.drive_base.straight(distance, then=Stop.BRAKE, wait=wait)
        # data_logging()

    def keep_drive(self, speed, turn_rate, time_millis):
        self.drive_base.drive(speed, turn_rate)
        wait(time_millis)

    """
    Turns the robot to an specified angle
    positive angle turen to the right, negative angle 
    turn to left
    """

    def pivot_turn(self, angle, wait=True):
        self.log_data(f"pivot_turn {angle}mm")
        self.drive_base.turn(angle, then=Stop.HOLD, wait=wait)
        self.log_data(f"pivot_turn {angle}mm")
        # data_logging()

    def curve_trun(self, radius, angle, wait=True):
        self.log_data(f"curve_trun {angle}mm")
        self.drive_base.arc(radius, angle, then=Stop.HOLD, wait=wait)
        self.log_data(f"curve_trun {angle}mm")
        # data_logging()

    def get_speed_raw(self):
        settings = self.drive_base.settings()
        if self.logs_enabled:
            print(
                "speed={}, accel={}, turn_speed={} turn_accel={}".format(
                    settings[0], settings[1], settings[2], settings[3]
                )
            )
        return settings

    def set_speed_raw(
        self,
        speed=DEFAULT_SPEED,
        acceleration=DEFAULT_ACCELERATION,
        turn_rate=DEFAULT_TURN_RATE,
        turn_acceleration=DEFAULT_TURN_ACCELERATION,
    ):
        self.drive_base.settings(speed, acceleration, turn_rate, turn_acceleration)

    """
    Get the speed setting in tuple(straight_speed, straing_aceel, turn_speed, turn_accel)
    """

    def set_speed_percentage(
        self,
        speed_percentage=DEFAULT_SPEED_PERCENTAGE,
        acceleration_percentage=DEFAULT_ACCELERATION_PERCENTAGE,
        turn_rate_percentage=DEFAULT_TURN_RATE_PERCENTAGE,
        turn_acceleration_percentage=DEFAULT_TURN_ACCELERATION_PERCENTAGE,
    ):
        speed = get_speed_mmsec(speed_percentage)
        acceleration = get_acceleration_mmsec2(acceleration_percentage)
        turn_rate = get_turn_rate_degsec(turn_rate_percentage)
        turn_acceleration = get_turn_acceleration_degsec2(turn_acceleration_percentage)
        if self.logs_enabled:
            print("\tset speed {}% = {} mm/sec".format(speed_percentage, speed))
            print(
                "\tset accel {}% = {} mm/sec2".format(
                    acceleration_percentage, acceleration
                )
            )
            print(
                "\tset turn_rate {}% = {} deg/sec".format(
                    turn_rate_percentage, turn_rate
                )
            )
            print(
                "\tset turn_accel {}% = {} deg/sec2".format(
                    turn_acceleration_percentage, turn_acceleration
                )
            )
        self.drive_base.settings(speed, acceleration, turn_rate, turn_acceleration)
