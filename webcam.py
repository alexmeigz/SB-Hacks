import cv2
# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv

def takePic():

    for i in range(1, 7):
        while (True):
            cap = cv2.VideoCapture(0)
            ret,frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

            cv2.imshow('Side ' + str(i), rgb)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('capture'+str(i)+'.jpg', frame)
                break

        cap.release()
        cv2.destroyAllWindows()



