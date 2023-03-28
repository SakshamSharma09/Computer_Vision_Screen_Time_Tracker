import cv2
import mediapipe as mp
import time

detect = mp.solutions.face_detection.FaceDetection()

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

start_time = time.time()
maximum_time_to_watch = 15

while True:
    ret , frame = cap.read()
    height, width, channels = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.rectangle(frame, (0,0), (width,60), (255,255,255), -1)
    results =detect.process(rgb_frame)

    if results.detections:
        elapsed_time = (int)(time.time() - start_time)

        #alert after a certain threshold
        if elapsed_time >= maximum_time_to_watch:
            cv2.putText(frame, "Exceeded Limit to watch", (40, 250), font, 1.5, (100, 255, 255), 10)

        cv2.putText(frame, "{} seconds".format(elapsed_time), (10,50), font, 1.4, (100,100,255), 4)
        print("Elapsed : {}".format(elapsed_time))
        print("Face looking at the screen")

    else:
        print("No Face detected")
        start_time = time.time()

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyALlWindows()
