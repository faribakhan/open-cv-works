import datetime

import numpy as np
import cv2 as cv

cap =cv.VideoCapture(0);

#print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#cap.set(3, 1208)
#cap.set(4, 720)

#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):

  ret,frame = cap.read()
  if ret == True:
      font = cv.FONT_HERSHEY_SIMPLEX
      text = 'Width: '+ str(cap.get(3)) + ' Height: ' + str(cap.get(4))
      datet = str(datetime.datetime.now())
      frame = cv.putText(frame, datet, (10, 50), font, 1, (0,0,255), 2, cv.LINE_AA)
      cv.imshow('frame', frame)

      if cv.waitKey(1) & 0xFF == ord('q'):
        break
  else:
      break

cap.release()
out.release()
cv.destroyAllWindows()