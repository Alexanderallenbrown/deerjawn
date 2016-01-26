from stupiddeer import *
from bge import logic,constraints

import time
import datetime
from math import sin,cos
from numpy import *




def setup():
	d = DeerDemo(y_0=-3, Vd = 5,dt=1.0/60.0)





# Main Program
def main():
        
    # get the current controller
    controller = logic.getCurrentController()
    #print(controller.sensors)
    deerobj = controller.owner
    print(deerobj)
    