from pybricks.hubs import PrimeHub  # Import PrimeHub class for SPIKE Prime
from pybricks.parameters import Axis
from pybricks.tools import wait

# Create a PrimeHub object
hub = PrimeHub()

# Access the IMU data for yaw (angle around the Z-axis)
yaw = hub.imu.heading()
print("Yaw Angle:", yaw)

# Access the angular velocity (rate of rotation) around the Z-axis
yaw_rate = hub.imu.angular_velocity(Axis.Z)
print("Yaw Rate:", yaw_rate)

# Example of how to access angular velocity around other axes
angular_velocity_x = hub.imu.angular_velocity(Axis.X)
angular_velocity_y = hub.imu.angular_velocity(Axis.Y)

print("Angular Velocity X:", angular_velocity_x)
print("Angular Velocity Y:", angular_velocity_y)

# Adding a simple delay to see the changes
wait(500)  # Wait for 500 milliseconds
