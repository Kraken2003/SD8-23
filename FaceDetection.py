import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        pointHead = face[151]
        cv2.circle(img, pointHead, 5, (0, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        #W = 7
        #f = 477
        #d = round((W*f)/w, 2)
        d = round((6.3 * 477) / w, 2)
        cvzone.putTextRect(img, f'Depth: {d}cm', (face[10][0]-75, face[10][1]-50),colorT=(255, 255, 255),
                colorR=(0, 0, 0), font=cv2.FONT_HERSHEY_PLAIN, offset=10,scale=2)

    cv2.imshow('tracking', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('T') or key == ord('t'):
        break

