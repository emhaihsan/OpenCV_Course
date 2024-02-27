import cv2


cap = cv2.VideoCapture(0)

cap.set(3, 300) # width modification
cap.set(4, 300) # height modification

cap.set(10, 150) # brightness modification

while True:
    success, frame = cap.read()

    if success:
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()