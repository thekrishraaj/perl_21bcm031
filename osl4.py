import cv2

img = cv2.VideoCapture(0)

while True:
    _, frame = img.read()
    frame = cv2.flip(frame, 1)
    origin = frame.copy()
    
    fil1 = frame.copy()
    fil2 = frame.copy()
    fil3 = frame.copy()
    fil4 = frame.copy()

    cv2.rectangle(origin, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.rectangle(origin, (400, 100), (500, 300), (0, 0, 255), 2)
    cv2.line(origin, (0, 0), (300, 300), (255, 255, 0), 2)
    cv2.circle(origin, (350, 450), 100, (255, 255, 0), 2)
    cv2.putText(origin, 'video', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

   
    filter1 = cv2.bilateralFilter(fil1, 19,75,75)
    filter2 = cv2.boxFilter(fil2, 0, (3,3), fil2, (-1,-1), False, cv2.BORDER_DEFAULT)  
    filter3 = cv2.GaussianBlur(fil3, (3,3), 0)
    filter4 = cv2.cvtColor(fil4, cv2.COLOR_BGR2GRAY)

   
    cv2.imshow('Blur Filter', filter1)
    cv2.imshow('Box Filter', filter2)
    cv2.imshow('Gaussian Blur Filter', filter3)
    cv2.imshow('Black and White', filter4)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 