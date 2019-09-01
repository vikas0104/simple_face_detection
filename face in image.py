import cv2
import os
cam = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(r"C:\Users\vikas\AppData\Roaming\Python\Python37\site-packages\cv2\data\haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier(r"C:\Users\vikas\AppData\Roaming\Python\Python37\site-packages\cv2\data\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"C:\Users\vikas\AppData\Roaming\Python\Python37\site-packages\cv2\data\haarcascade_smile.xml")
cwd = os.getcwd()
os.chdir(r'C:\Users\vikas\Downloads\python tut')


while(True):
    _,image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.95, 1)
    for x,y,w,h in faces:
        image = cv2.rectangle(image, (x,y), (x+w,y+h),(0,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,190),2)
    cv2.imshow("faceeee",image)
    cv2.imshow("roi",roi_color)
    if cv2.waitKey(1)==27:
        break
cam.release()
cv2.destroyAllWindows()
os.chdir(cwd)


