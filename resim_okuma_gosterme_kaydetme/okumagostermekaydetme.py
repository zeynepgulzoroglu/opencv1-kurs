import cv2

img = cv2.imread("C:/Users/zeyne/Desktop/opencvkurs/resim_okuma_gosterme_kaydetme/klon.jpg")
# print(img) sayısal okuma
cv2.namedWindow("image", cv2.WINDOW_NORMAL)


cv2.imshow("image",img)
cv2.imwrite("C:/Users/zeyne/Desktop/opencvkurs/resim_okuma_gosterme_kaydetme/klon.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()