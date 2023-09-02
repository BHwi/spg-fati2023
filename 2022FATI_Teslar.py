from zumi.zumi import Zumi
from zumi.util.screen import Screen
import IPython.display
import time
from zumi.protocol import Note
from zumi.util.camera import Camera
from zumi.util.vision import Vision
from zumi.util.color_classifier import ColorClassifier

zumi = Zumi()
screen = Screen()
camera = Camera()
vision = Vision()

camera.start_camera()

try:
    image = camera.capture()
    qr_code = vision.find_QR_code(image)
    message = vision.get_QR_message(qr_code)
    
    camera.clear_output()
    camera.close()
        
    if str(message) == 'factory':
        zumi.drive_over_markers(3)
        zumi.turn_right()
        zumi.forward(speed = 80, duration = 1.3)
        time.sleep(2)
        zumi.reverse(speed = 80, duration = 1.3)
        zumi.turn_left()
    elif str(message) == 'school':
        zumi.drive_over_markers(7)
        zumi.turn_left()
        zumi.forward(speed = 80, duration = 1.3)
        time.sleep(2)
        zumi.reverse(speed = 80, duration = 1.3)
        zumi.turn_right()
    elif str(message) == 'building':
        zumi.drive_over_markers(8)
        zumi.turn_right(5)
        zumi.drive_over_markers(2)
        zumi.turn_right()
        zumi.forward(speed = 80, duration = 1.3)
        time.sleep(2)
        zumi.reverse(speed = 80, duration = 1.3)
        zumi.turn_left()
    elif str(message) == 'museum':
        zumi.drive_over_markers(8)
        zumi.turn_right(5)
        zumi.drive_over_markers(8)
        zumi.turn_left()
        zumi.forward(speed = 80, duration = 1.3)
        time.sleep(2)
        zumi.reverse(speed = 80, duration = 1.3)
        zumi.turn_right(100)
        
    
    while True:
        front_right = zumi.boolean_IR('front_right')
        front_left = zumi.boolean_IR('front_left')

        if front_left == True and front_right == True:
            zumi.reverse(speed = 10, duration = 0.2)
            zumi.turn_right(80)
            break
        else:
            zumi.forward(speed = 40, duration = 0.5)
            zumi.turn_right(1.5)
    
    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
        
        else:
            zumi.control_motors(6, 10, 0)
            
    
    #A 코스 종료
    
    
    camera.start_camera()
    
    user_name = 'sese'
    demo_name = 'color_beta'
    
    knn = ColorClassifier(user_name=user_name)
    train = knn.load_model(demo_name)
    knn.fit("hsv")
    
    time.sleep(2)
    
    image = camera.capture()
    predict = knn.predict(image)
    camera.clear_output()
    
    while True:
        image = camera.capture()
        if 'NONE' == predict or predict != knn.predict(image):
            time.sleep(2)
            screen.draw_text_center('end')
            camera.clear_output()
            break
        screen.draw_text_center(predict)
        camera.clear_output()
        
    camera.close()
    screen.clear_display()
    
    while True:
        front_right = zumi.boolean_IR('front_right')
        front_left = zumi.boolean_IR('front_left')

        if front_left == True and front_right == True:
            zumi.reverse(speed = 10, duration = 0.2)
            zumi.turn_right(80)
            break
        else:
            zumi.forward(speed = 40, duration = 0.8)
            zumi.turn_right(1.5)
            
    while True:
        front_right = zumi.boolean_IR('front_right')
        front_left = zumi.boolean_IR('front_left')

        if front_left == True and front_right == True:
            zumi.reverse(speed = 10, duration = 0.2)
            zumi.turn_right(80)
            break
        else:
            zumi.forward(speed = 40, duration = 0.8)
            zumi.turn_right(1.5)
            
    while True:
        front_right = zumi.boolean_IR('front_right')
        front_left = zumi.boolean_IR('front_left')

        if front_left == True and front_right == True:
            zumi.reverse(speed = 10, duration = 0.2)
            zumi.turn_left()
            break
        else:
            zumi.forward(speed = 40, duration = 0.7)
            zumi.turn_right(1.5)
    while True:
        front_right = zumi.boolean_IR('front_right')
        front_left = zumi.boolean_IR('front_left')

        if front_left == True and front_right == True:
            zumi.reverse(speed = 10, duration = 0.2)
            zumi.turn_left()
            break
        else:
            zumi.forward(speed = 40, duration = 0.8)
            zumi.turn_right(1.5)

    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
            
        else:
            zumi.control_motors(6, 10, 0)
    
    zumi.forward(speed = 10, duration = 0.8)
    
    # B 코스 종료
    
    
    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
            
        else:
            zumi.control_motors(5, 10, 0)
    
    zumi.turn_left()
    
    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
            
        else:
            zumi.control_motors(5, 10, 0)
            
    zumi.turn_right()
    
    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
            
        else:
            zumi.control_motors(5, 10, 0)
            
    zumi.turn_right()
    
    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
            
        else:
            zumi.control_motors(5, 10, 0)
    
    
    time.sleep(2)
    
    camera.start_camera()
    
    image = camera.capture()
    qr_code = vision.find_QR_code(image)
    message = vision.get_QR_message(qr_code)
    
    camera.clear_output()
    camera.close()
    
    
    if str(message) =='left':
        zumi.turn_left()
        
        while True:
        
            bottom_right = zumi.read_IR('bottom_right')
            bottom_left = zumi.read_IR('bottom_left')
        
            if bottom_right < 100 and bottom_left < 100:
                screen.draw_text_center("Stop")
                zumi.control_motors(0, 0, 0)
                break
            
            elif bottom_right < 100 and bottom_left > 100:
                zumi.control_motors(5, 0, 0)
            
            elif bottom_right > 100 and bottom_left < 100:
                zumi.control_motors(0, 5, 0)
            
            else:
                zumi.control_motors(5, 10, 0)
            
        zumi.turn_right()
        
    elif str(message) == 'right':
        zumi.turn_right()
        
        while True:
        
            bottom_right = zumi.read_IR('bottom_right')
            bottom_left = zumi.read_IR('bottom_left')
        
            if bottom_right < 100 and bottom_left < 100:
                screen.draw_text_center("Stop")
                zumi.control_motors(0, 0, 0)
                break
            
            elif bottom_right < 100 and bottom_left > 100:
                zumi.control_motors(5, 0, 0)
            
            elif bottom_right > 100 and bottom_left < 100:
                zumi.control_motors(0, 5, 0)
            
            else:
                zumi.control_motors(5, 10, 0)
            
        zumi.turn_left()
        
    while True:
        
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_right < 100 and bottom_left < 100:
            screen.draw_text_center("Stop")
            zumi.control_motors(0, 0, 0)
            break
            
        elif bottom_right < 100 and bottom_left > 100:
            zumi.control_motors(5, 0, 0)
            
        elif bottom_right > 100 and bottom_left < 100:
            zumi.control_motors(0, 5, 0)
            
        else:
            zumi.control_motors(5, 10, 0)
            
    zumi.forward()
    
    zumi.stop()
    
    
except KeyboardInterrupt:
    camera.clear_output()
    camera.close()
    zumi.stop()
