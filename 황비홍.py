import time
import IPython.display
from zumi.util.camera import Camera
from zumi.util.color_classifier import ColorClassifier
from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.protocol import Note
from zumi.util.vision import Vision

zumi = Zumi()
screen = Screen()
camera = Camera()




def acourse():
    start()


def bcourse():
    while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
        zumi.forward(30, 0.5)
    zumi.turn_right(90)
    zumi.forward(50,2)
    while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
        zumi.forward(30, 0.5)
    zumi.turn_right(90)
    zumi.forward(50,1.5)
    while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
        zumi.forward(30, 0.5)
    zumi.turn_left(90)
    zumi.forward(50,1.5)
    while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
        zumi.forward(30, 0.5)
    zumi.turn_left(90)

def ccourse():
    try:
        threshold = 120
        turnSpeed = 5
        forwardSpeed = 10

        while True:
            bottom_right = zumi.read_IR('bottom_right')
            bottom_left = zumi.read_IR('bottom_left')

            #
            if bottom_left > threshold and bottom_right > threshold:
                zumi.control_motors(forwardSpeed, forwardSpeed, 0)

            elif bottom_left < threshold and bottom_right > threshold:
                zumi.control_motors(turnSpeed, 0, 0)

            elif bottom_left > threshold and bottom_right < threshold:
                zumi.control_motors(0, turnSpeed, 0)

            elif bottom_left > threshold:
                zumi.control_motors(turnSpeed, 0, 0)

            elif bottom_right > threshold:
                zumi.control_motors(0, turnSpeed, 0)

        zumi.stop()

    except KeyboardInterrupt:
        zumi.stop()

    if(QRcode()=='left'):
        zumi.turn_left(90)
        try:
            threshold = 80
            turnSpeed = 5
            forwardSpeed = 10

            while True:
                bottom_right = zumi.read_IR('bottom_right')
                bottom_left = zumi.read_IR('bottom_left')

                #
                if bottom_left < threshold and bottom_right < threshold:
                    zumi.control_motors(forwardSpeed, forwardSpeed, 0)

                elif bottom_left > threshold and bottom_right < threshold:
                    zumi.control_motors(turnSpeed, 0, 0)

                elif bottom_left < threshold and bottom_right > threshold:
                    zumi.control_motors(0, turnSpeed, 0)

                elif bottom_left > threshold and bottom_right > threshold:
                    zumi.stop()


        except KeyboardInterrupt:
            zumi.stop()
    if(QRcode()=='right'):
        zumi.turn_right(90)
        try:
            threshold = 80
            turnSpeed = 5
            forwardSpeed = 10

            while True:
                bottom_right = zumi.read_IR('bottom_right')
                bottom_left = zumi.read_IR('bottom_left')

                #
                if bottom_left < threshold and bottom_right < threshold:
                    zumi.control_motors(forwardSpeed, forwardSpeed, 0)

                elif bottom_left > threshold and bottom_right < threshold:
                    zumi.control_motors(turnSpeed, 0, 0)

                elif bottom_left < threshold and bottom_right > threshold:
                    zumi.control_motors(0, turnSpeed, 0)

                elif bottom_left > threshold:
                    zumi.control_motors(turnSpeed, 0, 0)

                elif bottom_right > threshold:
                    zumi.control_motors(0, turnSpeed, 0)

            zumi.stop()

        except KeyboardInterrupt:
            zumi.stop()



def start():
    if (QRcode() == 'factory'):
        zumi.drive_over_markers(3, 30, 150, 50)
        zumi.turn_right(90)
        while((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn(180)
        time.sleep(2)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_right(90)
        zumi.drive_over_markers(13,50,100,50)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_right(90)
        zumi.forward(50, 4)
        time.sleep(2)
        # parkingright()

    if (QRcode() == 'school'):
        zumi.drive_over_markers(6, 30, 150, 50)
        zumi.turn_left(90)
        while((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn(180)
        time.sleep(2)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_left(90)
        zumi.drive_over_markers(10,50,100,50)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_right(90)
        zumi.forward(50,4)
        time.sleep(2)

        # parkingleft()

    if (QRcode() == 'building'):
        zumi.drive_over_markers(11, 30, 150, 50)
        zumi.turn_right(90)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn(180)
        time.sleep(2)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_right(90)
        zumi.drive_over_markers(5, 50, 100, 50)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_right(90)
        zumi.forward(50, 4)
        time.sleep(2)

        # zumi.turn_left(90)
        # parkingright()

    if (QRcode() == 'museum'):
        zumi.drive_over_markers(15, 30, 150, 50)
        zumi.turn_left(90)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn(180)
        time.sleep(2)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_left(90)
        zumi.drive_over_markers(1, 50, 100, 50)
        while ((zumi.boolean_IR('front_right', 100) == False) and (zumi.boolean_IR('front_left', 100) == False)):
            zumi.forward(30, 0.5)
        zumi.turn_right(90)
        zumi.forward(50, 4)
        time.sleep(2)

        # zumi.turn_right(90)
        # parkingleft()




def QRcode():
    global camera
    vision = Vision()
    camera.start_camera()

    while True:
        image = camera.capture()
        qr_code = vision.find_QR_code(image)
        camera.show_image(image)

        if qr_code:
            camera.clear_output()
            camera.close()
            strData = vision.get_QR_message(qr_code)
            return strData

def check_back_ir():
    detectionSensor = 0
    back_left = zumi.read_IR('back_left')
    back_right = zumi.read_IR('back_right')
    # 후방 두개의 센서중에 감지 값이 높은 값을 사용
    if (int(back_left) <= int(back_right)):
        detectionSensor = int(back_left)
        note_duration = detectionSensor / 2
        if note_duration < 10: note_duration = 10

        zumi.play_note(50, note_duration)
    else:
        detectionSensor = int(back_right)
        note_duration = detectionSensor / 2
        if note_duration < 10: note_duration = 10

        zumi.play_note(50, note_duration)
    # 후방 왼쪽, 오른쪽 중에서 감지 값이 높은 값을 리턴
    return detectionSensor

def check_front_ir():
    detectionSensor = 0
    front_left = zumi.read_IR('front_left')
    front_right = zumi.read_IR('front_right')
    # 전방 두개의 센서중에 감지 값이 높은 값을 사용
    if (int(front_left) <= int(front_right)):
        detectionSensor = int(front_left)
        note_duration = detectionSensor / 2
        if note_duration < 10: note_duration = 10

        zumi.play_note(50, note_duration)
    else:
        detectionSensor = int(front_right)
        note_duration = detectionSensor / 2
        if note_duration < 10: note_duration = 10

        zumi.play_note(50, note_duration)
    # 전방 왼쪽, 오른쪽 중에서 감지 값이 높은 값을 리턴
    return detectionSensor

def parkingleft():
    zumi = Zumi()
    zumi.turn(-90)

    backIRthreshold = 20
    frontIRthreshold = 20


    while True:
        backIRsensor = check_back_ir()

        if (backIRsensor < backIRthreshold):
            zumi.stop()
            print("sensor detection")
            zumi.play_note(50, 2000)
            break

        zumi.control_motors(-1, -3, 0)
    #나와서 회전 후 B코스 진입
    while True:
        frontIRsensor = cheak_front_ir()

        if (frontIRsensor < frontIRthreshold):
            zumi.stop()
            print("sensor detection")
            zumi.play_note(50, 2000)
            break
        zumi.control_motors(1, 3, 0)

    zumi.turn_left(90)

def parkingright():
    zumi = Zumi()
    zumi.turn(90)

    backIRthreshold = 20
    frontIRthreshold = 20

    while True:
        backIRsensor = check_back_ir()

        if (backIRsensor < backIRthreshold):
            zumi.stop()
            print("sensor detection")
            zumi.play_note(50, 2000)
            break

        zumi.control_motors(-1, -3, 0)

    #나와서 회전 후 B코스 진입
    while True:
        frontIRsensor = cheak_front_ir()

        if (frontIRsensor < frontIRthreshold):
            zumi.stop()
            print("sensor detection")
            zumi.play_note(50, 2000)
            break
        zumi.control_motors(1, 1, 0)

    zumi.turn_right(90)


acourse()
bcourse()
ccourse()

