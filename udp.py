import cv2
import mediapipe as mp
import socket
import struct

# 웹캠이 켜지지 않을 때는 소괄호 안의 숫자를 0에서 10 사이로 바꿔 보세요. 대부분 0과 1에서 작동합니다.
# If the webcam doesn't turn on, change the number in brackets between 0 and 10. It usually works at 0 and 1.
cap = cv2.VideoCapture(0)

# 문제가 해결되지 않으면 "webcam index issue"라고 GPT와 같은 LLM 모델에게 물어보세요. 필요한 도움을 받을 수 있습니다.
# If the problem persists, ask "webcam index issue" to a model like GPT (LLM). You can get the necessary help.


# Initialize MediaPipe hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def send_data_to_blender(hand_landmarks):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('localhost', 9090))  # Port where Blender is listening
            for landmark in hand_landmarks:
                # Convert values from 0 to 1 to -1 to 1
                x = landmark.x * 2 - 1
                y = landmark.y * 2 - 1
                z = landmark.z * 2 - 1
                
                # Pack the data in binary format
                data = struct.pack('fff', x, y, z)
                s.sendall(data)
    except ConnectionRefusedError:
        print("Connection refused. Blender may not be running or listening on the expected port.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Process the image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Find the boundary of the hand
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

            # Draw a rectangle around the hand
            cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
            
            # Send landmark data to Blender
            send_data_to_blender(hand_landmarks.landmark)

    # Display the image on screen
    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
