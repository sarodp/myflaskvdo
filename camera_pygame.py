#!usr/bin/python3
# -*- coding: utf-8 -*-
## cam intro --http://www.pygame.org/docs/tut/CameraIntro.html

from base_camera import BaseCamera
from pygame.locals import *
import sys,time, pygame.camera




class Camera(BaseCamera):
    sizecam = (320,240)

    pygame.camera.init()
    clist = pygame.camera.list_cameras()
    if not clist:
        raise ValueError("camera>> Sorry, no cameras detected.")
    device = clist[0]
    #device = '/dev/video0'

    pgcam0 = pygame.camera.Camera(device, sizecam)
    print("camera>> device=", device, " camsize=", sizecam)
   
    @staticmethod
    def set_device(xdevice):
        Camera.device = xdevice
        Camera.pgcam0 = pygame.camera.Camera(Camera.device, Camera.sizecam)
 
    @staticmethod
    def set_sizecam(xsizecam):
        Camera.sizecam = xsizecam
        #Camera.thread.stop() ...how???
        Camera.pgcam0 = None
        Camera.pgcam0 = pygame.camera.Camera(Camera.device, Camera.sizecam)
        Camera.__init__()
 
    @staticmethod
    def frames():
        Camera.pgcam0.start()
        print("camera>> Camera.pgcam1.start")
        #if not camera.isOpened():
        #    raise RuntimeError('camera>> Could not start camera.')

        while True:
            # encode as a jpeg image and return it
            surfcam = Camera.pgcam0.get_image()
            pygame.image.save(surfcam, '/home/pi/scr/t.jpg')
            img = open('/home/pi/scr/t.jpg', 'rb').read()
            yield img
 


