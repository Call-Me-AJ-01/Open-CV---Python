import cv2
import numpy as np
img=np.ones([512,512,3],np.uint8)*255
rows,columns,channels=img.shape
img[511][0]
c=0
for i in range(columns):
    img[i][0]=[255,0,0]
    img[i][1]=[0,255,0]
    img[i][2]=[0,0,255]
cv2.imshow('aj',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

















































#np.ones([height,width,channel])
#cv2.putText(img,'Image Created Using Numpy',(0,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
#cv2.imshow('Creating Black Image Using Numpy',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()