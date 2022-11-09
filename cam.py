#!/usr/bin/env python3
import picamera
import datetime
import time
import pygame, sys
from pygame.locals import *

print ("  Press Ctrl & C to Quit")

global greyColor, dgryColor, whiteColor, greenColor, blackColor, redColor, button_width, button_height
greyColor  = pygame.Color(128,128,128)
dgryColor  = pygame.Color(64,64,64)
whiteColor = pygame.Color(255,255,255)
greenColor = pygame.Color(0,255,0)
blackColor = pygame.Color(0,0,0)
redColor   = pygame.Color(255,0,0)
button_width = 100
button_height = 50
Record = 0
pygame.init()
windowSurfaceObj = pygame.display.set_mode((button_width,button_height), pygame.NOFRAME,25)

def key(bcolor,b,msg,fcolor):
   fsize = button_height/3
   y = 0
   if b == 1:
      b = y = button_height/2
   colors = [greyColor,dgryColor, greenColor, blackColor, redColor]
   pygame.draw.rect(windowSurfaceObj,colors[bcolor], Rect(3, b-3, button_width-3, button_height-3))
   if bcolor == 0:
      wColor = whiteColor
      kColor = dgryColor
   else:
      kColor = whiteColor
      wColor = dgryColor
   pygame.draw.rect(windowSurfaceObj,wColor,Rect(0,0,button_width-2,button_height-2),2)
   pygame.draw.line(windowSurfaceObj,kColor,(0,button_height-1),(button_width-1,button_height-1))
   pygame.draw.line(windowSurfaceObj,kColor,(1,button_height-2),(button_width-2,button_height-2))
   pygame.draw.line(windowSurfaceObj,kColor,(button_width-1,0),(button_width-1,button_height))
   pygame.draw.line(windowSurfaceObj,kColor,(button_width-2,1),(button_width-2,button_height-1))
   pygame.draw.rect(windowSurfaceObj,blackColor,Rect(2,2,button_width-4,button_height-4),1)
   fontObj = pygame.font.Font('freesansbold.ttf',int(fsize))
   msgSurfaceObj = fontObj.render(msg,False,colors[fcolor])
   msgRectobj = msgSurfaceObj.get_rect()
   fx = button_width/2 - (len(msg)*fsize)/3
   msgRectobj.topleft = (fx,y+5)
   windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
   pygame.display.update()
   return

key(0,0,"RECORD",1)
key(0,1,"VIDEO",1)

try:
   while True:
      with picamera.PiCamera() as camera:
         camera.resolution = (1280, 720)
         camera.framerate = 25
         while Record == 0 :
            for event in pygame.event.get():
               if event.type == MOUSEBUTTONDOWN :
                  mousex, mousey = event.pos
                  if mousex < button_width and mousey < button_height:
                     Record = 1
                     time.sleep(0.25)
                     key(1,0,"RECORD",4)
         now = datetime.datetime.now()
         timestamp = now.strftime("%y%m%d%H%M%S")
         start = time.time()
         camera.start_recording(str(timestamp) + '.h264')
         while Record == 1:
            length = int(time.time()-start)
            key(1,1,str(length),4)
            camera.wait_recording(.01)
            for event in pygame.event.get():
               if event.type == MOUSEBUTTONDOWN :
                  mousex, mousey = event.pos
                  if mousex < button_width and mousey < button_height:
                     Record = 0
                     key(0,0,"RECORD",1)
                     key(0,1,"VIDEO",1)
                     camera.stop_recording()
              
except KeyboardInterrupt:
  print ("Quit")