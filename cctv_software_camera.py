import cv2
import time

def minimizeWindow():
    import win32gui, win32con
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    width = video.get(3)
    height = video.get(4)
    print ("Video resolution is set to ", width, 'x', height)
    print ("Help -- \n1.Press esc key to exit. \n2.press m to minimize.")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    date_time = time.strftime("recording %H-%M-%d -%m %y")
    output = cv2.VideoWriter('footage/'+date_time+'.mp4', fourcc, 20.0, (width, height))
    while video.isOpened():
        check, frame = video.read()
        if check == True:
            frame = cv2.flip(frame, 1)

            t_time = time.ctime()
            cv2.rectangle(frame, (5,5,100,20), (255, 255, 255), cv2.FILLED)
            cv2.putText (frame, "Camera 1", (20,20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (5, 5, 5), 1)
            cv2.imshow('CCTV camera', frame)
            output.write(frame)
            if cv2.waitKey(1) == 27:
                print ("Video footage saved in current directory")
                break
            elif cv2.waitKey(1) == ord('m'):
                minimizeWindow()
            else:
                print("cannot open camera, Check configuration")
                break
    video.release()
    output.release()
    cv2.destroyAllWindows()
print ("*"*80+"\n"+" "*30"Welome to cctv software\n"+"*" *80)
ask = int(input("Do you want to open the cctv?\n1. yes\n2. no\n>>> "))

if ask == 1:
    cctv()
elif ask == 2:
    print ("babye! be safe")
    exit