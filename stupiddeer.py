""" Class Intro Here"""

#Benji Helbein
#November 20, 2015

from numpy import *

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
        self.sig_psi = 45*pi/180
        self.mean_psi = 70*pi/180
        self.tlastchange = 0
        self.threshtime = 0.5
        self.DistThresh = DistThresh
        self.FarThresh = 30
        self.moving_yet = 0
        self.collisions = 0
        self.collisionthresh = 1


       

    

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
        print('Distance is ' + str(sqrt((xcarnow-self.xdeer)**2 + (ycarnow-self.ydeer)**2)))
        #print(self.Vd)
        if self.moving_yet==0:

            if sqrt((xcarnow-self.xdeer)**2 + (ycarnow-self.ydeer)**2)<self.DistThresh:
                self.moving_yet = 1
        else:
            sdd, sd = self.statederivs(dt)
            print('State Derivative are:' + str(sd) +',' + str(sdd))
            self.s = self.s + sd*dt
            self.xdeer = self.xdeer + self.sd*dt*cos(self.psideer)
            self.ydeer = self.ydeer + self.sd*dt*sin(self.psideer)
            #pprint('states are:' + str(self.s) +',' + str(self.s))
            if(currtime - self.tlastcthonhange)  > self.threshtime:
                #print("Change Direction")
                self.psideer = self.sig_psi*random.random() + self.mean_psi
                self.tlastchange = currtime
            if sqrt((xcarnow-self.xdeer)**2 + (ycarnow-self.ydeer)**2)> self.FarThresh:
                if self.sd > 0:
                    self.sdd = -self.sdd     
        
        if sqrt((xcarnow-self.xdeer)**2 + (ycarnow-self.ydeer)**2)<self.collisionthresh:
            self.collisions = self.collisions + 1



        
        #print "x and y updated are: "+str(self.xdeer)+','+str(self.ydeer)
        #return the time step so we can keep track.
        return self.xdeer,self.ydeer

# if __name__ == '__main__':
#         from matplotlib.pyplot import *    
#         #def runsim(self,simtime,timevec = None,animate=False):
#         """def runsim(self,simtime,shot_times,targets_hit,timevec = None):
#             runs a post-hoc simulation of the target when shot times and targets hit are known.
#             If you don't want to use the star's built-in dt, you can specify a time vector. This will override dt
#         """
#         #if (timevec==None):
#         tvec = arange(0,10,d.dt)#time vector
#         #else:
#          #   tvec = timevec
#         animate=True
#         if animate==True:
#             ion()
#             figure()


#         #starting at the second index, simulate the star.
#         xdeervec = zeros(len(tvec))
#         for ind in range(1,len(tvec)):
#             self.dt = tvec[ind]-tvec[ind-1]

#             self.updateDynamics(self.dt)
#             if animate==True:
#                 self.plotDeer()

#             xdeervec[ind] = self.xdeer

#         #return 0



     
#         ion()
#         figure()
#         for ind in range(0, len(t)):
#            d,updateDynamics(d.dt, xcar[ind],ycar[ind],t[ind])
#            cla()
#            d.plotDeer()
