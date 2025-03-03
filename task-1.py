import cv2 as cv

im = cv.imread("images/variant-3.jpeg", cv.IMREAD_UNCHANGED)
hsv_var3 = cv.cvtColor(im, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv_var3)
cv.imwrite('Changed_image.jpg', hsv_var3)
cv.waitKey(0)
cv.destroyAllWindows()
