import cv2
import mediapipe as mp
import random
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 1. Setup Mediapipe
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.7
)

landmarker = HandLandmarker.create_from_options(options)

# 2. Game Variables
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [Player, Computer]
computerMove = ""
playerMove = "None"

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
    results = landmarker.detect(mp_image)

    if startGame:
        if not stateResult:
            timer = time.time() - initialTime
            cv2.putText(img, str(int(3 - timer)), (300, 150), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0

                # Computer makes a random choice
                moves = ['Rock', 'Paper', 'Scissors']
                computerMove = random.choice(moves)

                # Identify Player Move at the moment timer ends
                if results.hand_landmarks:
                    hand_lms = results.hand_landmarks[0]
                    fingers = []
                    for tip in [8, 12, 16, 20]:
                        if hand_lms[tip].y < hand_lms[tip - 2].y:
                            fingers.append(1)
                        else:
                            fingers.append(0)

                    total = sum(fingers)
                    if total == 0:
                        playerMove = "Rock"
                    elif total == 4:
                        playerMove = "Paper"
                    elif total == 2:
                        playerMove = "Scissors"
                    else:
                        playerMove = "Unknown"

                if not results.hand_landmarks or playerMove == "Unknown":
                    stateResult = False
                    startGame = True
                    initialTime = time.time()
                    playerMove = "None"
                    computerMove = ""
                else:
                    # Calculate Winner
                    if playerMove == computerMove:
                        pass  # Tie
                    elif (playerMove == "Rock" and computerMove == "Scissors") or \
                         (playerMove == "Paper" and computerMove == "Rock") or \
                         (playerMove == "Scissors" and computerMove == "Paper"):
                        scores[0] += 1  # Player wins
                    else:
                        scores[1] += 1  # Computer wins

    # Draw Hand Landmarks
    if results.hand_landmarks:
        for hand_landmarks in results.hand_landmarks:
            for landmark in hand_landmarks:
                x = int(landmark.x * img.shape[1])
                y = int(landmark.y * img.shape[0])
                cv2.circle(img, (x, y), 5, (0, 255, 0), -1)

    # Display Results
    if stateResult:
        cv2.putText(img, f"Computer: {computerMove}", (350, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(img, f"Player: {playerMove}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.putText(img, f"Score: {scores[0]} - {scores[1]}", (250, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    cv2.imshow("Rock Paper Scissors AI", img)

    key = cv2.waitKey(1)
    if key == ord('s'):  # Press 's' to start a round
        startGame = True
        initialTime = time.time()
        stateResult = False
    if key == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
landmarker.close()