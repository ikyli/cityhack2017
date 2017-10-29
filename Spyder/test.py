import numpy as np
import cv2
import json
#487,603 - parking location
#1020,473 - mean value
block001_data = []
cap = cv2.VideoCapture('test.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    road_color= frame[468:478,1015:1025]
    rgb_value =road_color.mean()
    parking_color = frame[603:613,487:497]
    rgb_value_parking = parking_color.mean()
    
    if(abs(rgb_value_parking-rgb_value)<5):
        cv2.circle(frame,(487,603), 10, (255,255,255), thickness=1, lineType=8, shift=0)
        data = {}
        data["x"]="25"
        data["y"]="245"
        block001_data.append(data)
        
        block001_json=json.dumps(block001_data)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    cv2.imshow('frame',frame)
   

cap.release()
cv2.destroyAllWindows()
     
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#fgbg = cv2.createBackgroundSubtractorMOG2()
#while(1):
#    ret, frame = cap.read()
# 
#    fgmask = fgbg.apply(frame)
#    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
# 
#    cv2.imshow('frame',fgmask)
#
#    k = cv2.waitKey(30) & 0xff
#    if k == 27:
#        break
# 
#cap.release()
#cv2.destroyAllWindows()

#######################################