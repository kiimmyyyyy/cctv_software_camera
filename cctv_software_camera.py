import cv2
import time

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    width = video.get(3)
    height = video.get(4)
    print ("Video resolution is set to ", width, 'x', height)
    print ("Help -- \n1.Press esc key to exit. \n2.press m to minimize.")
    fourcc = cv2.videoWriter_fourcc(*'XVID')
    date_time = time.strftime("recording %H-%M-%d -%m %y")
    output = cv2.VideoWriter('footage/'+date_time+'.mp4')
    while video.isOpened():
        check, frame = video.read()
        if check == True:
            frame = cv2.flip(frame, 1)

            oras = time.ctime()
            cv2.rectangle(frame. (5,5,100,20). (255, 255, 255), cv2.FILLED)
            cv2.putText (frame, "Camera 1", (20,20), cv2.FONT_HERSHEY_DUPLEX, 0.5)


