import cv2

def resizeeithAspectRatio (img, witdh = None, height = None, inter = cv2.INTER_AREA):

    dimension = None
    (h, w) = img.shape[:2]

    if witdh is None and height is None:
        return img
    
    if witdh is None:
        r = height / float(h)
        dimension = (int(w*r), height)

    else:
        r = witdh / float(w)
        dimension = (int(h*r), witdh)

    return cv2.resize(img,dimension, interpolation= inter)

img = cv2.imread("C:/Users/zeyne/Desktop/opencvkurs/resim_okuma_gosterme_kaydetme/klon.jpg")
img1 = resizeeithAspectRatio(img, witdh = None, height = None, inter = cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resize",img1)

cv2.waitKey(0)
cv2.destroyAllWindows