import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages')

from bge import logic,constraints

import time
import datetime
from math import sin,cos
from numpy import *
from stupiddeer import *



d = DeerDemo( Vd = 15,dt=1.0/60.0,x_0=30,y_0=-15,a=2)


def setup():
	
	print('hey there')
	scene = logic.getCurrentScene()
	car = scene.objects["Car_Red"]
	print(car)





# Main Program
def main():
    scene = logic.getCurrentScene()
    car = scene.objects["Car_Red"]
    # get the current controller
    controller = logic.getCurrentController()
    #print(controller.sensors)
    deerobj = controller.owner
    #pprint(deerobj)

    carpos = car.worldPosition
    
    car_x = carpos[0]
    car_y = carpos[1]
    #print(car_x,car_y)
    timenow = time.time()
    #print(timenow)
    d.updateDynamics(1.0/60.0,car_x,car_y,timenow)
    #print(d.xdeer,d.ydeer)
    deerobj.worldPosition = [d.xdeer,d.ydeer,1]
    deerobj.worldOrientation = [0, 0, d.psideer + pi/2]