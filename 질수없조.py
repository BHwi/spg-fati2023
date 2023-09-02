#!/usr/bin/env python
# coding: utf-8

# In[5]:


# A코스 횡단보도 + 주차

from zumi.zumi import Zumi
from zumi.util.screen import Screen
import time
from zumi.protocol import Note

from zumi.util.camera import Camera
from zumi.util.vision import Vision

camera = Camera()
vision = Vision()
camera.start_camera()

zumi = Zumi()
screen = Screen()


def drive():
    zumi = Zumi()
    
    heading = 0
    min_ir_threshold = 100
    
    while True:
        front_right = zumi.read_IR('front_right')
        front_left = zumi.read_IR('front_left')
        
        if front_left < min_ir_threshold or front_right < min_ir_threshold:
            zumi.stop()
            break
            
        zumi.go_straight(30, heading, 60)



def case1():
    front_right = zumi.read_IR('front_right')
    front_left = zumi.read_IR('front_left')
    
    time.sleep(2)
    
    zumi.turn_right(180)
    drive()
    zumi.turn_right()
        
def case2():
    front_right = zumi.read_IR('front_right')
    front_left = zumi.read_IR('front_left')
    
    time.sleep(2)
    
    zumi.turn_right(180)
    drive()
    zumi.turn_left()
            
try:
    for i in range(10):
        image = camera.capture()
        
        qr_code = vision.find_QR_code(image)
        message = vision.get_QR_message(qr_code)
        
        if vision.get_QR_message(qr_code) == "factory":
            zumi.drive_over_markers(3)
            zumi.turn_right()
            drive()
            case1()
            break
        elif vision.get_QR_message(qr_code) == "school":
            zumi.drive_over_markers(7)
            zumi.turn_left()
            drive()
            case2()
            break
        elif vision.get_QR_message(qr_code) == "building":
            zumi.drive_over_markers(11)
            zumi.turn_right()
            drive()
            case1()
            break
        elif vision.get_QR_message(qr_code) == "museum":
            zumi.drive_over_markers(11)
            zumi.drive_over_markers(4)
            zumi.turn_left()
            drive()
            case2()
            break
        else:
            print("none")
            
        print("message : " , vision.get_QR_message(qr_code))

        camera.show_image(image)
        camera.clear_output()
finally:
    camera.close()
    print("done")
    

drive()
zumi.turn_right()


# In[6]:


# A코스 -> B코스 구간
zumi.control_motors(30,50)
time.sleep(1.5)

zumi.stop()
time.sleep(2)


# In[7]:


# 라인트레이서 함수

zumi = Zumi()
screen = Screen()

def LineTraceFunc() :
    try:
        threshold = 120
        turnSpeed = 1
        forwardSpeed = 4
        print('Linetrace Start')
        
        while True:
            bottom_right = zumi.read_IR('bottom_right')
            bottom_left = zumi.read_IR('bottom_left')

            if bottom_left > threshold and bottom_right > threshold :
                #print('go')
                zumi.control_motors(30,50)
        
            elif bottom_left > threshold :
                zumi.control_motors(turnSpeed,0)
        
            elif bottom_right > threshold :
                zumi.control_motors(0, turnSpeed)
        
            else :
                print('Linetrace Stop')
                zumi.stop()
                break
                
    except KeyboardInterrupt:
        print('factitious Stop')
        zumi.stop()
        


# In[8]:


LineTraceFunc()


# In[9]:


# 색상카드 인식
from zumi.util.color_classifier import ColorClassifier
import time

camera = Camera()
screen = Screen()
zumi = Zumi()

user_name = 'zumi'
demo_name = 'color'

knn = ColorClassifier(user_name=user_name)
train = knn.load_model(demo_name)
knn.fit("hsv")

camera.start_camera()

try:
    for i in range(10):
        image = camera.capture()
        predict = knn.predict(image)
        screen.draw_text_center(predict)
finally:
    camera.close()


# In[10]:


# B코스 주행
import IPython.display

zumi = Zumi()
screen = Screen()

def drive():
    zumi = Zumi()
    
    heading = -3
    min_ir_threshold = 100
    
    while True:
        front_right = zumi.read_IR('front_right')
        front_left = zumi.read_IR('front_left')
        
        if front_left < min_ir_threshold or front_right < min_ir_threshold:
            zumi.stop()
            break
            
        zumi.go_straight(30, heading, 60)
        

drive()
zumi.turn_right()
drive()
zumi.turn_right()
drive()
zumi.turn_left()
drive()
zumi.turn_left()


# In[11]:


# B코스 -> C코스 구간
zumi.control_motors(30,50)
time.sleep(2)

zumi.stop()
time.sleep(2)


# In[12]:


LineTraceFunc()


# In[21]:


LineTraceFunc()


# In[22]:


# 라인트레이싱 코너링
for i in range(3):
    
    if (i < 1):
        zumi.turn_left(90)
            

    else:
        zumi.turn_right(90)
            
    LineTraceFunc()


# In[25]:


#C코스
#QR코드 인식

camera = Camera()
vision = Vision()
camera.start_camera()

try:
    while True:
        image = camera.capture()
        
        qr_code = vision.find_QR_code(image)

        print("message : " , vision.get_QR_message(qr_code))
        
        
        
        if vision.get_QR_message(qr_code) != None :
            ans = eval(vision.get_QR_message(qr_code))
            break
            
        
        camera.show_image(image)
        camera.clear_output()
finally:
    camera.close()
    print("done")
    


# In[ ]:


#C코스
# QR Code의 message 값에 따라 갈림길 선택

if vision.get_QR_message(qr_code) == "left":
    zumi.turn_left(90)
    LineTraceFunc()
    zumi.turn_right(90)

    
else:
    zumi.turn_right(90)
    LineTraceFunc()
    zumi.turn_left(90)


# In[ ]:


LineTraceFunc()


# In[ ]:


zumi.control_motors(30,50)
time.sleep(1)

zumi.stop()
time.sleep(2)

