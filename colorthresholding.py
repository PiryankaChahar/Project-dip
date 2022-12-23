import cv2
img_path="./hand.jpg"
img=cv2.imread(img_path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("image",img)
cv2.waitKey(0)