import cv2

#
# img_file = 'Car_Image.jpg'
#
# img = cv2.imread(img_file)
#
car_tracker = cv2.CascadeClassifier('car_detector.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# creaate opencv video
# video = cv2.VideoCapture('TeslaDashcam.mp4')
# video = cv2.VideoCapture('withpedestrians.mp4')
cap= cv2.VideoCapture(0)
# Our pretrained car and pedestrian classisfier


while True:

    _, img = cap.read()
    # successfull_read, frame = video.read()


    grayscaled_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect cars AND pedestrians
    cars = car_tracker.detectMultiScale(grayscaled_frame,1.1,4)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('Pragya car detector', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()

