import cv2

def nothing(arg): pass

cv2.namedWindow('Image')
cv2.createTrackbar('Zoom', 'Image', 0, 100, nothing)
while(1):
    cv2.namedWindow('Image', cv2.WINDOW_KEEPRATIO)
    img = cv2.imread('bartender_at_work©iStock.jpg')
    black = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('Image', img)
    threshold = cv2.getTrackbarPos('Zoom', 'Image')
    print("from loop",threshold)

    h,w = img.shape[0], img.shape[1]
    x,y = threshold*3, threshold*2
    img = img[x:h+x, y:w-y]
    print(h,w,x,y)
    cv2.imshow('Image', img)
    cv2.imshow('Black and white', black)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('bartender_at_work©iStock.jpg', black)
        cv2.destroyAllWindows()
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()