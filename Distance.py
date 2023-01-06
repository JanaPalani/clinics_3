import cv2
import cvzone 
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)


while True :
    success , img  = cap.read()
    img = cv2.flip(img,1)
    img , faces = detector.findFaceMesh(img , draw= False)

    if faces:
        face = faces[0]
        pointsleft = face[145]
        pointsright = face[374]
        # cv2.line(img, pointsleft,pointsright,(0,200,0),3)
        # cv2.circle(img, pointsleft,5,(255,0,255),cv2.FILLED)
        # cv2.circle(img, pointsright,5,(255,0,255),cv2.FILLED)
        w, _ =  detector.findDistance(pointsleft,pointsright)
        W = 6.3 
        # FOR FINDING FOCAL LENGTH OF THE CAMERA 
        # d = 30
        # f = (w*d)/W
        # print(f)


        #  FOCAL DISTANCE 
        f = 525 
        d = (W*f)/w
        print(d)

        cvzone.putTextRect(img,f'depth: {int(d)}cm',(face[10][0]-50,face[10][1]-50))

        

    cv2.imshow('image', img )
    if cv2.waitKey(1) == 81:break 