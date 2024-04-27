"""
Circles detection
"""

import cv2 as cv
import numpy as np

video_capture = cv.VideoCapture("http://192.168.44.8:8080/video")
prev_circle = None
dist = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1 - y2)**2

while True:
    ret, frame = video_capture.read()
    if not ret: break

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur_frame = cv.GaussianBlur(gray_frame, (17, 17), 0)

    circles = cv.HoughCircles(blur_frame, cv.HOUGH_GRADIENT, 1.2, 100,
                              param1=100, param2=30, minRadius=25, maxRadius=400)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prev_circle is not None:
                if dist(chosen[0], chosen[1], prev_circle[0], prev_circle[1]) <= dist(i[0], i[1], prev_circle[0], prev_circle[1]):
                    chosen = i
        
        cv.circle(frame, (chosen[0], chosen[1]), 1, (255, 0, 0), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (0, 255, 0), 3)
        prev_circle = chosen

    cv.imshow("circles", frame)

    if cv.waitKey(1) & 0xFF == ord('q'): break

video_capture.release()
cv.destroyAllWindows()
