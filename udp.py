import cv2
import mediapipe as mp
import socket
import struct

# MediaPipe 손 인식 모델 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# 댐핑을 위한 이전 좌표 초기화
prev_x, prev_y, prev_z = 0, 0, 0
alpha = 0.9  # 보간 팩터

def send_data_to_blender(hand_landmarks):
    global prev_x, prev_y, prev_z
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('localhost', 9090))  # Blender가 수신 대기 중인 포트
            for landmark in hand_landmarks:
                # 0과 1 사이의 값을 -1과 1 사이로 변환
                x = landmark.x * 2 - 1
                y = landmark.y * 2 - 1
                z = landmark.z * 2 - 1
                
                # 현재 좌표와 이전 좌표 사이를 보간
                smoothed_x = alpha * prev_x + (1 - alpha) * x
                smoothed_y = alpha * prev_y + (1 - alpha) * y
                smoothed_z = alpha * prev_z + (1 - alpha) * z

                # 이진 형식으로 데이터 패킹
                data = struct.pack('fff', smoothed_x, smoothed_y, smoothed_z)
                s.sendall(data)

                # 현재 좌표를 이전 좌표로 업데이트
                prev_x, prev_y, prev_z = smoothed_x, smoothed_y, smoothed_z
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
            # 손의 경계 찾기
            h, w, _ = image.shape
            min_x, min_y = w, h
            max_x, max_y = 0, 0
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * w), int(landmark.y * h)
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y

            # 손 주변에 네모 그리기
            cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
            
            # 손의 중심 좌표 계산
            center_x, center_y = (min_x + max_x) // 2, (min_y + max_y) // 2
            # 손의 중심 좌표 출력 (0과 1의 값을 -1과 1 사이로 변환)
            coord_x = ((center_x / w) * 2) - 1
            coord_y = ((center_y / h) * 2) - 1
            cv2.putText(image, f'X:{coord_x:.2f}, Y:{coord_y:.2f}', (center_x - 50, center_y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # 랜드마크 데이터를 Blender로 전송
            send_data_to_blender(hand_landmarks.landmark)

    # 화면에 이미지 표시
    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
