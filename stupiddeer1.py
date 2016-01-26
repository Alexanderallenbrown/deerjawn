""" Class Intro Here"""

#Benji Helbein
#November 20, 2015

from numpy import *
from scipy import *
from matplotlib.pyplot import *
import time

class DeerDemo:
    #class owned vars
    def __init__(self,x_0=0,y_0=0,dt=0.001,a=.7,Vd=15, DistThresh = 15):
        self.s = 0 #Distance of the deer
        self.sd = 0 #Velocity of the deer
        self.sdd = 0 #Acceleration of the deer
        self.xdeer = x_0 #X Position of the deer
        self.ydeer = y_0 #Y position of the deer
        self.a = a #constant for state diagram, maybe inverse of deer inertia?
        self.Vd = Vd # Max velocity of the deer
        self.g = 9.81#gravity
        self.dt = dt#time step. SHOULD BE UPDATED CONTINUOUSLY
        self.starttime=0
        self.psideer = 90
        self.sig_psi = 30*pi/180
        self.mean_psi = 90*pi/180
        self.tlastchange = 0
        self.threshtime = 0.5
        self.DistThresh = DistThresh


       

    

    def plotDeer(self,scale=1):

        #clear the figure
        cla()
        #deer dot
        plot([self.xdeer,self.ydeer],'k+')
        axis('equal')
        axis([-2.5*scale,2.5*scale,-2.5*scale,2.5*scale])
        pause(.001)


    def statederivs(self,dt):
        self.sdd = self.a*(self.Vd - self.sd)
        self.sd = self.sd  + self.sdd*dt
        return self.sdd, self.sd


    def updateDynamics(self,dt,xcarnow,ycarnow,currtime):
        

        sdd, sd = self.statederivs(dt)
        self.s = self.s + sd*dt
        self.xdeer = self.xdeer + self.sd*dt*cos(self.psideer)
        self.ydeer = self.ydeer + self.sd*dt*sin(self.psideer)
        if sqrt((xcarnow-self.xdeer)**2 + (ycarnow-self.ydeer)**2)<self.DistThresh:
            if(currtime - self.tlastchange)  > self.threshtime:
                print("Change Direction")
                self.psideer = self.sig_psi*random.random() + self.mean_psi
                self.tlastchange = currtime


        
        #print "x and y updated are: "+str(self.xdeer)+','+str(self.ydeer)
        #return the time step so we can keep track.
        return self.xdeer,self.ydeer


    # def runsim(self,simtime,timevec = None,animate=False):
    #     """def runsim(self,simtime,shot_times,targets_hit,timevec = None):
    #         runs a post-hoc simulation of the target when shot times and targets hit are known.
    #         If you don't want to use the star's built-in dt, you can specify a time vector. This will override dt
    #     """
    #     if (timevec==None):
    #         tvec = arange(0,simtime,self.dt)#time vector
    #     else:
    #         tvec = timevec

    #     if animate==True:
    #         ion()
    #         figure()


    #     #starting at the second index, simulate the star.
    #     xdeervec = zeros(len(tvec))
    #     for ind in range(1,len(tvec)):
    #         self.dt = tvec[ind]-tvec[ind-1]

    #         self.updateDynamics(self.dt)
    #         if animate==True:
    #             self.plotDeer()

    #         xdeervec[ind] = self.xdeer

    #     return 0



if __name__ == '__main__':
    """ this is a demo for the deer module. """
    d = DeerDemo(y_0=-3, Vd = 5)
    t = arange(0,5,d.dt)
    x_deervec = zeros(len(t))
    y_deervec = zeros(len(t))
    print len(x_deervec),len(y_deervec)
    ycar = zeros(len(t))
    xcar = linspace(-20,20,len(t))
    for ind in range(0, len(t)):
            d.updateDynamics(d.dt, xcar[ind],ycar[ind],t[ind])
            x_deervec[ind] = d.xdeer
            y_deervec[ind] = d.ydeer
    print len(x_deervec),len(y_deervec)
    figure()
    subplot(2,1,1)
    plot(x_deervec,y_deervec, 'ks', xcar,ycar, 'r+')
    ylabel('Position Y')
    xlabel('Position X')
    legend(['Deer', 'Car'])
    subplot(2,1,2)
    plot(t, x_deervec, 'k', t, xcar, 'r')
    ylabel('X Position')
    xlabel('Time (s)')
    show()

     
    #ion()
    #figure()
    #for ind in range(0, len(t)):
    #    d,updateDynamics(d.dt, xcar[ind],ycar[ind],t[ind])
    #    cla()
    #    d.plotDeer()
