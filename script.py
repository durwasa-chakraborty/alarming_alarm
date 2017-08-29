import cv2
import sys
import webbrowser

def main():

    count_sleep = 0 
    casc_path_front_eyes = "haarcascade_eye.xml"
    face_cascade = cv2.CascadeClassifier(casc_path_front_eyes)
    video_capture = cv2.VideoCapture(0) #primary source of system

    while True:
        ret, frame = video_capture.read()

        gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        socket = face_cascade.detectMultiScale(
                gray_scale,
                scaleFactor=1.1,
                minNeighbors=3,
                minSize=(50,50),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        #rectangle

        for(x,y,w,h) in socket:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            #print socket

        if(len(socket) is 0):
            count_sleep = count_sleep+1
            if(count_sleep is 10):
                notification()

        else:
            count_sleep=0


        cv2.imshow('Video_Project',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break


    video_capture.release()
    cv2.destroyAllWindows()

def notification():
    webbrowser.open("https://www.youtube.com/watch?v=frw6uu3nonQ")

if __name__ == '__main__':
    main()

