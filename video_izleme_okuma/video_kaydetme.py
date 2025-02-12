import cv2

cap =cv2.VideoCapture(0)

fileName = "C:/Users/zeyne/Desktop/opencvkurs/video_izleme_okuma/webcam.avi"
codec = cv2.VideoWriter_fourcc('W','M','V','2')
frameRate = 30
resolution = (640,480)

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()    