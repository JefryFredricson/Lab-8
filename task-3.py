from time import sleep, time
import cv2

#def check_middle(x, y):
#   if (220 <= x <= 420) and (140 <= y <= 340):
#        exact_time = time() - start_time
#        print(f'The point is in the central square 200x200 pixels at {exact_time:.3f} seconds!')

def add_muha(frame, x, y):
    img = cv2.imread('fly64.png')
    frame[y-32:y+32, x-32:x+32]=img
    return frame

def video_processing():
    global start_time
    cap = cv2.VideoCapture('sample.mp4')
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    down_points = (640, 480)
    i = 0
    start_time = time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 122, 255, cv2.THRESH_BINARY_INV)


        contours, hierarchy = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            frame = add_muha(frame, x + (w // 2), y + (h // 2))
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                #check_middle(a, b)


        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == 27:
            cv2.destroyAllWindows()
            break

        sleep(0.1)
        i += 1

    cap.release()

video_processing()
cv2.destroyAllWindows()