import cv2

# cap =cv2.VideoCapture(0)
cap =cv2.VideoCapture("C:/Users/zeyne/Desktop/opencvkurs/video_izleme_okuma/antalya.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    