import cv2
import numpy as np

canvas = np.zeros((700,700,3), dtype=np.uint8) + 255
cv2.putText(canvas, "OpenCV", (20,200), cv2.FONT_HERSHEY_COMPLEX, 5, (0,0,0), cv2.LINE_AA) #20.200 yazı  koordşnatları

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()