import cv2
import mediapipe as mp
import socket
import struct

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def send_data_to_blender(hand_landmarks):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('localhost', 9090))  # Blender가 수신 대기 중인 포트
        for landmark in hand_landmarks:
            # 이진 형식으로 데이터 패킹
            data = struct.pack('fff', landmark.x, landmark.y, landmark.z)
            s.sendall(data)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks_data = [landmark for landmark in hand_landmarks.landmark]
            send_data_to_blender(landmarks_data)

    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()