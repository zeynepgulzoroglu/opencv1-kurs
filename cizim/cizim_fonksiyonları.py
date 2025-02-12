import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255

cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5) #çizgi 1.noktası, 2.noktası, renk, kalınlık
cv2.line(canvas, (100,50), (200,250), (0,0,255), 9)

cv2.rectangle(canvas, (20,20), (50,50), (0,250,0), thickness=-1)
cv2.rectangle(canvas, (50,50), (250,250), (0,250,0), thickness=2)

cv2.circle(canvas, (250,250), 100, (0,250,0), thickness=-1)

p1 = (100,200)
p2 = (50,50)
p3 = (300,100)
cv2.line(canvas, p1,p2,(0,0,0),4)
cv2.line(canvas, p3,p2,(0,0,0),4)
cv2.line(canvas, p3,p1,(0,0,0),4)

points = np.array([[[110,200], [330,200], [290,220], [100,100]]], np.int32)
cv2.polylines(canvas, [points], False, (0,0,100), 5)

cv2.ellipse(canvas, (300,300), (100,50), 10, 90, 360, (255,255,0), -1)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()