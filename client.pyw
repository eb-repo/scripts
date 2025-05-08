import cv2
import socket
import pickle
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF, 1000000)

server_ip = "127.0.0.1"
server_port = 6664

cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 400)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    x_as_bytes = pickle.dumps(buffer)

    s.sendto((x_as_bytes), (server_ip, server_port))