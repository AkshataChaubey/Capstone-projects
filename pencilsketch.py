# Convert the pencil Image to pencil sketch
import cv2
image=cv2.imread("flower.jpg")
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invertedimage=255-grayimage
blurredimage=cv2.GaussianBlur(invertedimage,(21,21),0)
inverted_blurredimage=255-blurredimage
pencilsketch=cv2.divide(grayimage,inverted_blurredimage,scale=255)
cv2.imshow("original",image)
cv2.imshow("image",pencilsketch)
cv2.waitKey(0)