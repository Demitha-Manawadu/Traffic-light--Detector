from ultralytics import YOLO
import cv2
import cvzone
import math
#cap = cv2.VideoCapture(0)#for web cam
#cap.set(3,1280)#width
#cap.set(4,720)
cap = cv2.VideoCapture("../Videos/trafficlight.mp4")#for video
model = YOLO("Trafficlight_detect.pt")
classNames = ["Green","Red","yellow"]
while True:
    succes, img =cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            #bounding box
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3#create the rectangle numbers for the colour purple using opencv
            w,h = x2-x1,y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h))
            #confinace
            conf = math.ceil((box.conf[0]*100))/100#rounding to the 2 decimal places
            #Class Name
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}',(max(0, x1),max(35, y1)),scale=1.5,thickness=2)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
