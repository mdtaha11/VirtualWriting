import cv2
import numpy as np
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3,400)
cap.set(4,400)
cap.set(10,150)


def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("Hue Min","HSV",37,179,empty)
cv2.createTrackbar("Hue Max","HSV",179,179,empty)
cv2.createTrackbar("Saturation Min","HSV",135,255,empty)
cv2.createTrackbar("Saturation Max","HSV",255,255,empty)
cv2.createTrackbar("Val Min","HSV",140,255,empty)
cv2.createTrackbar("Val Max","HSV",255,255,empty)

while True:

    _,img=cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min =  cv2.getTrackbarPos("Hue Min","HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Saturation Min", "HSV")
    s_max = cv2.getTrackbarPos("Saturation Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")
    print(h_min,h_max,s_min,s_max,v_min,v_max)


    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)

    result=cv2.bitwise_and(img,img,mask=mask)
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    hStack=np.hstack([img,mask,result])
    cv2.imshow("stacked",hStack)

    if cv2.waitKey(1)& 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()