import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]

        # shuffle pixels in the face region
        shuffled = face_roi.reshape(-1, 3)
        np.random.shuffle(shuffled)
        shuffled = shuffled.reshape(face_roi.shape)

        # replace the face with the shuffled version
        frame[y:y+h, x:x+w] = shuffled

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

### blur video ###
#  import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# while True:
#     ret, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         face_roi = frame[y:y+h, x:x+w]
    
#         blurred_face = cv2.GaussianBlur(face_roi, (101, 101), 0)
#         frame[y:y+h, x:x+w] = blurred_face

    
#     cv2.imshow('frame', frame)


#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


### circles on face and eyes and nostrils apparently ###
# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)  # Mirror the frame horizontally
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in faces:
#         center_x = x + w // 2
#         center_y = y + h // 2
#         radius = max(w, h) // 2
#         cv2.circle(frame, (center_x, center_y), radius, (0, 255, 255), 3)

#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]

#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for (ex, ey, ew, eh) in eyes:
#             eye_center = (ex + ew // 2, ey + eh // 2)
#             eye_radius = max(ew, eh) // 3
#             cv2.circle(roi_color, eye_center, eye_radius, (255, 0, 0), 2)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


## #video capture ###
# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
    
#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


#### pixelate ###
# import cv2 
# import numpy as np

# test_img = cv2.imread('jon.jpg')

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# faces_rects = face_cascade.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 2)

# img_copy = test_img.copy()
 
# for (x, y, w, h) in faces_rects:
#     cv2.rectangle(img_copy, (x, y), (x+w, y+h), 2)

    
#     rect_color = img_copy[y:y+h, x:x+w]

 
#     shuffled = rect_color.reshape(-1, 3) 
#     np.random.shuffle(shuffled)


#     shuffled = shuffled.reshape(rect_color.shape)


#     img_copy[y:y+h, x:x+w] = shuffled

# cv2.imshow('my image', img_copy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#### blur #####
# import cv2 

# test_img = cv2.imread('jon.jpg')

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# faces_rects = face_cascade.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 2)

# img_copy = test_img.copy()

# for (x, y, w, h) in faces_rects:
#     cv2.rectangle(img_copy, (x, y), (x+w, y+h), 2)
#     rect_color = img_copy[y:y+h, x:x+w]

#     blur = cv2.GaussianBlur(rect_color, (101,101), 0)        
#     img_copy[y:y+h, x:x+w] = blur   

# # cv2.imwrite('new_img.jpg', img_copy) # save image

# cv2.imshow('my image', img_copy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


### rectangle around face ###
# import cv2


# test_img = cv2.imread('jon.jpg')

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# faces_rects = face_cascade.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 2)

# for (x,y,w,h) in faces_rects:
#      cv2.rectangle(test_img, (x, y), (x+w, y+h), (190, 105, 220), 2)

# cv2.imshow('jon.jpg', test_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()