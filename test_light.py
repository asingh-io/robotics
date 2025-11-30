from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Axis

# Initialize the hub.
hub = PrimeHub()

# Get the acceleration or angular_velocity along a single axis.
# If you need only one value, this is more memory efficient.
while True:

    # Read the forward acceleration.
    # forward_acceleration = hub.imu.acceleration(Axis.X)

    # Read the yaw rate.
    yaw_rate = hub.imu.angular_velocity(Axis.Z)
    # Read the tilt values. Now, the values are 0 when BLAST stands upright.
    # Leaning forward gives positive pitch. Leaning right gives positive roll.
    # pitch, roll = hub.imu.tilt()

    # Print the result.
    print(hub.imu.tilt())
    wait(200)