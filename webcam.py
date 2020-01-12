import cv2
# DEPENDENCIES: PYTHON3, NUMPY, OPENCV

dic = {0:"BLUE", 1:"WHITE", 2:"GREEN", 3:"YELLOW", 4:"RED", 5:"ORANGE"}

def takePic():
    '''takes 6 photos of rubix cube sides'''
    for i in range(1, 7):
        while (True):
            cap = cv2.VideoCapture(0)
            ret,frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

            cv2.imshow('Please Take Photo of the Side with the {} Center'.format(dic.get(i-1)), rgb)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('capture'+str(i)+'.jpg', frame)
                break

        cap.release()
        cv2.destroyAllWindows()



