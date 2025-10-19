from NexusDrive import *
from NexusAttachement import *


robo = NexusDrive(ENABLE_LOGING=True)


robo.drive(250)
robo.pivot_turn(90)
robo.drive(250)
robo.pivot_turn(-90)
robo.drive(150)
   


