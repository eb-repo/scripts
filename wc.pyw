import cv2

try:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        exit()

    ret, frame = cap.read()

    if ret:
        cv2.imwrite("wcp.jpg", frame)
    f = open ("wcpfail.txt", "rb")
    f.write(b"Webcam capture failed")
    f.close()
    cap.release()
except:
    pass