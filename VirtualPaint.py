import cv2
import numpy as np

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3,800)
cap.set(4,600)
cap.set(10,150)

myColors=[[18,23,75,47,223,255]]
myPoints=[]


def findColor(img,myColors):
    newPoints=[]
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array(myColors[0][0:3])
    upper=np.array(myColors[0][3:6])
    mask=cv2.inRange(imgHSV,lower,upper)
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
    if x!=0 and y!=0:
        newPoints.append([x,y])
    cv2.imshow("img",mask)
    return newPoints
def getContours(img):
    x,y,w,h=0,0,0,0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>70:
            cv2.drawContours(imgResult,cnt,-1,(0,255,0),2)
            peri=cv2.arcLength(cnt,True)

            approx=cv2.approxPolyDP(cnt,0.02*peri,True)

            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 7, (0, 0, 153), cv2.FILLED)

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)

    imgResult=img.copy()
    newPoints=findColor(img, myColors)
    if newPoints!=0:
        for p in newPoints:
           myPoints.append(p)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints)
    cv2.imshow("Video",imgResult)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

