from turtle import screensize
import cv2
import numpy as np
import pyautogui

screensize = (1920, 1080)
format = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', format, 20.0, screensize)

while True:
    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out.write(img)
    cv2.imshow('Recorder', img)
    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
out.release()