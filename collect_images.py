import cv2
import os
import time

# Change this to 'images/helmet' or 'images/no_helmet'
folder = 'images/helmet' 

if not os.path.exists(folder):
    os.makedirs(folder)
    
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret: break
        
    # Save image
    cv2.imwrite(os.path.join(folder, f'img_{count}.jpg'), frame)
    count += 1
    
    cv2.imshow('Collector', frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()