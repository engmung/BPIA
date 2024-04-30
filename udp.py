import cv2
import mediapipe as mp
import socket
import struct

# MediaPipe 손 인식 모델 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def send_data_to_blender(hand_landmarks):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('localhost', 9090))  # Blender가 수신 대기 중인 포트
            for landmark in hand_landmarks:
                # 0과 1 사이의 값을 -1과 1 사이로 변환
                x = landmark.x * 2 - 1
                y = landmark.y * 2 - 1
                z = landmark.z * 2 - 1
                
                # 이진 형식으로 데이터 패킹
                data = struct.pack('fff', x, y, z)
                s.sendall(data)
    except ConnectionRefusedError:
        print("Connection refused. Blender may not be running or listening on the expected port.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # 이미지 처리
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 랜드마크 데이터를 Blender로 전송
            send_data_to_blender(hand_landmarks.landmark)

    # 화면에 이미지 표시
    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
