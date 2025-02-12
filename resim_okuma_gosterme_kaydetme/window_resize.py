import cv2

img = cv2.imread("C:/Users/zeyne/Desktop/opencvkurs/resim_okuma_gosterme_kaydetme/klon.jpg")
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

img = cv2.resize(img,(640,480))

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()