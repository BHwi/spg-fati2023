from zumi.zumi import Zumi
from zumi.util.camera import Camera
from zumi.util.screen import Screen
from zumi.util.vision import Vision
import time

from zumi.util.color_classifier import ColorClassifier

zumi = Zumi()
camera = Camera()
screen = Screen()
vision = Vision()


def go_straight(move_time=1, speed=20, angle=None, k_p=None, k_i=None, k_d=None):
    try:
        if k_p is None or k_i is None or k_d is None:
            k_p = zumi.D_P
            k_i = zumi.D_I
            k_d = zumi.D_D
        max_speed = 127
        zumi.reset_PID()
        
        if angle is None:
            angle = zumi.read_z_angle()

        start_time = time.time()

        while time.time() - start_time < move_time:
            zumi.drive_at_angle(max_speed, speed, angle, k_p, k_d, k_i, 1.0)
            
        zumi.stop()
        
    except KeyboardInterrupt:
        zumi.stop()


def go_straight_until_obejct_detected(threshold=20, speed=20, angle=None, k_p=None, k_i=None, k_d=None):
    try:
        if k_p is None or k_i is None or k_d is None:
            k_p = zumi.D_P
            k_i = zumi.D_I
            k_d = zumi.D_D
        max_speed = 127
        turn_speed = 4
        if angle is None:
            angle = zumi.read_z_angle()
            
        zumi.reset_PID()

        while True:
            ir_readings = zumi.get_all_IR_data()
            front_right = ir_readings[0]
            front_left = ir_readings[5]
            if front_left < threshold and front_right < threshold:
                zumi.stop()
                break
            else:
                zumi.drive_at_angle(max_speed, speed, angle, k_p, k_d, k_i, 1.0)
                
    except KeyboardInterrupt:
        zumi.stop()


def line_trace(threshold=150, speed=1):
    try:
        turn_speed = 1
        right_motor_constant = 22

        while True:
            ir_readings = zumi.get_all_IR_data()
            bottom_right = ir_readings[1]
            bottom_left = ir_readings[3]

            if bottom_left > threshold and bottom_right > threshold:      
                zumi.control_motors(speed, speed * right_motor_constant)
            elif bottom_left > threshold:
                zumi.control_motors(turn_speed, 0)
            elif bottom_right > threshold:
                zumi.control_motors(0, turn_speed)
            else :
                zumi.stop()
                break

    except KeyboardInterrupt:
        zumi.stop()


def stable_line_trace(threshold=150, speed=3):
    try:
        turn_speed = 1
        k_p = zumi.D_P
        k_i = zumi.D_I
        k_d = zumi.D_D
        angle = zumi.read_z_angle()
        max_speed = 127
        zumi.reset_PID()

        while True:
            ir_readings = zumi.get_all_IR_data()
            bottom_right = ir_readings[1]
            bottom_left = ir_readings[3]

            if bottom_left > threshold and bottom_right > threshold:      
                zumi.drive_at_angle(max_speed, speed, angle, k_p, k_d, k_i, 1.0)
            elif bottom_left > threshold:
                angle = zumi.read_z_angle()
                zumi.control_motors(turn_speed, 0)
            elif bottom_right > threshold:
                angle = zumi.read_z_angle()
                zumi.control_motors(0, turn_speed)
            else :
                zumi.stop()
                break

    except KeyboardInterrupt:
        zumi.stop()


def course_A():
    camera.start_camera()
    qr_code = None

    try:
        while not qr_code:
            image = camera.capture()
            qr_code = vision.find_QR_code(image)
            camera.show_image(image)
            camera.clear_output()

            time.sleep(1)
    except KeyboardInterrupt:
        screen.draw_text_center("Interrupt.")
    finally:
        camera.close()
        
    screen.draw_text_center(vision.get_QR_message(qr_code))
    
    qr_message = vision.get_QR_message(qr_code)
    buildings = ['factory', 'school', 'building', 'museum']
    building_number = buildings.index(qr_message)
    
    all_line = 16
    line_count = building_number * 4 + 2
    flag = True
    count = 0
    
    try:
        k_p = zumi.D_P
        k_i = zumi.D_I
        k_d = zumi.D_D
        angle = zumi.read_z_angle()
        speed = 20
        max_speed = 127
        zumi.reset_PID()
        
        north_angle = angle
        east_angle = angle - 90
        west_angle = angle + 90
        south_angle = angle - 180
        
        threshold = 150
        
        # line counting
        while count <= line_count:
            print(count)
            zumi.drive_at_angle(max_speed, speed, angle, k_p, k_d, k_i, 1.0)
            ir_readings = zumi.get_all_IR_data()
            bottom_right = ir_readings[1]
            bottom_left = ir_readings[3]
            if (bottom_left < threshold) and flag:
                count += 1
                flag = False
            elif (bottom_left > threshold) and not flag:
                flag = True

        if building_number % 2 == 0:
            zumi.turn_right(90)
            go_straight(move_time=1, angle=east_angle)
            time.sleep(2)
            zumi.turn_left(180)
            go_straight(move_time=1, angle=west_angle)
            zumi.turn_right(90)
        else:
            zumi.turn_left(90)
            go_straight(move_time=1, angle=west_angle)
            time.sleep(2)
            zumi.turn_right(180)
            go_straight(move_time=1, angle=east_angle)
            zumi.turn_left(90)
            
        # line counting
        while count < all_line - 1:
            print(count)
            zumi.drive_at_angle(max_speed, speed, angle - 5, k_p, k_d, k_i, 1.0)
            ir_readings = zumi.get_all_IR_data()
            bottom_right = ir_readings[1]
            bottom_left = ir_readings[3]
            if (bottom_left < threshold) and flag:
                count += 1
                flag = False
            elif (bottom_left > threshold) and not flag:
                flag = True
                
        zumi.stop()
        time.sleep(0.5)
        go_straight(move_time=1)

        go_straight_until_obejct_detected(threshold=40, angle=angle - 5, k_p=k_p, k_i=k_i, k_d=k_d)
        zumi.turn_right(90)
        stable_line_trace()
        go_straight(move_time=0.3, angle=east_angle, k_p=k_p, k_i=k_i, k_d=k_d)
        
    except KeyboardInterrupt:
        zumi.stop()


def course_B():
    count = 0
    try:
        knn = ColorClassifier()
        
        camera.start_camera()
        train = knn.load_model("gorani2")
        knn.fit("hsv")

        while True:
            image = camera.capture()
            predict = knn.predict(image)
            screen.draw_text_center(predict)

            if predict == "no":
                count += 1
                
            if count > 1:
            camera.close()
            break
            
            time.sleep(1)

    finally:
        camera.close()
        
    k_p = zumi.D_P
    k_i = zumi.D_I
    k_d = zumi.D_D
    angle = zumi.read_z_angle()
    max_speed = 127
    zumi.reset_PID()
    
    north_angle = angle
    east_angle = angle - 90
    west_angle = angle + 90
    south_angle = angle - 180
    
    go_straight_until_obejct_detected(speed=10, angle=north_angle)
    zumi.turn_right(90)
    go_straight_until_obejct_detected(speed=10, angle=east_angle)
    zumi.turn_right(90)
    go_straight_until_obejct_detected(speed=10, angle=south_angle)
    zumi.turn_left(90)
    go_straight_until_obejct_detected(speed=10, angle=east_angle)
    zumi.turn_left(90)
    stable_line_trace()


def course_C():
    k_p = zumi.D_P
    k_i = zumi.D_I
    k_d = zumi.D_D
    angle = zumi.read_z_angle()
    speed = 20
    max_speed = 127
    zumi.reset_PID()

    north_angle = angle
    east_angle = angle - 90
    west_angle = angle + 90
    south_angle = angle - 180
    
    line_trace()
    zumi.turn_left(75)
    line_trace()
    zumi.turn_right(75)
    line_trace()
    zumi.turn_right(75)
    line_trace()
    
    camera.start_camera()
    qr_code = None
    
    try:
        while not qr_code:
            image = camera.capture()
            qr_code = vision.find_QR_code(image)
            camera.show_image(image)
            camera.clear_output()
            time.sleep(1)
    except KeyboardInterrupt:
        screen.draw_text_center("Interrupt.")
    finally:
        camera.close()
        
    direction = vision.get_QR_message(qr_code)
    screen.draw_text_center(direction)
    if direction == 'left':
        zumi.turn_left(90)
        line_trace()
        zumi.turn_right(75)
        line_trace()
    elif direction == 'right':
        zumi.turn_right(90)
        line_trace()
        zumi.turn_left(75)
        line_trace()
    else:
        screen.draw_text_center("Invalid direction.")
        
    go_straight(move_time=1)


course_A()
time.sleep(2)
course_B()
go_straight(move_time=0.3)
time.sleep(3)
course_C()

