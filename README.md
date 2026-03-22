# 🖐️ OpenCV Rock-Paper-Scissors AI

A real-time Computer Vision game where you play Rock-Paper-Scissors against an AI using your webcam. This project uses **OpenCV** for image processing and **Mediapipe** for high-fidelity hand tracking.

---

## 🚀 Features
* **Hand Tracking:** Uses Mediapipe to detect 21 hand landmarks in real-time.
* **Smart Timer:** A 3-second countdown gives you time to prepare your move.
* **AI Opponent:** The computer makes a random choice using the `random` library.
* **Live Scoreboard:** Tracks wins and losses during your session.
* **Interactive UI:** On-screen text overlays for a seamless gaming experience.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/opencv-rock-paper-scissors.git](https://github.com/YOUR_USERNAME/opencv-rock-paper-scissors.git)
   cd opencv-rock-paper-scissors

2. **Create and activate a virtual environment:**
   ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies:**
   ```bash
   pip install opencv-python mediapipe

## 🎮 How to Play
1. **Launch the game:**
   ```bash
   python main.py

2. **Start a Round: Press the 'S' key on your keyboard.**

3. **The Countdown: You will see a 3... 2... 1... countdown on the screen.**

4. **Make Your Move: Show Rock, Paper, or Scissors to the camera before the timer hits zero.**
5. **Result: The computer will reveal its choice, and the winner will be displayed on the screen.**
6. **Quit: Press 'Q' to close the application.**

## 🧠 How it Works
1. **The system captures video frames and converts them to RGB. Mediapipe identifies the coordinates of your fingertips.**

2. **Rock: All fingertips are below their respective knuckles.**

3. **Paper: All fingertips are extended upward.**

4. **Scissors: Only the index and middle fingers are extended.**

## 📜 License
This project is open-source and available under the MIT License.

## Created with ❤️ by Jin Hern Tan


