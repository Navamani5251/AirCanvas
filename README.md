.

🎨 Air Canvas – Gesture-Based Drawing Application

Air Canvas is a computer vision–based drawing application that allows users to draw in the air using hand gestures captured through a webcam. The system tracks finger movements in real time and converts them into digital drawings without using a mouse, stylus, or touchscreen.

🚀 Features

✋ Real-time hand tracking using MediaPipe

✏️ Draw using index finger gesture

✊ Fist gesture to stop drawing

🖐️ Open palm gesture to clear the canvas

🎯 Smooth cursor movement to reduce jitter

🎥 Live webcam feed with canvas overlay

🖼️ Separate drawing canvas view

⬇️ Extendable to download/save drawings

🛠️ Technologies Used

Python 3.10

OpenCV

MediaPipe

NumPy

📁 Project Structure
air-canvas/
│
├── canvas.py              # Canvas abstraction for drawing strokes
├── gesture_detector.py    # Hand tracking and gesture recognition
├── utils.py               # Helper utilities (smoothing, overlays, filters)
├── main.py                # Entry point of the application
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files and folders
└── README.md              # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/air-canvas.git
cd air-canvas

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run the Application
python main.py


Press q to exit the application.

🕹️ Gesture Controls
Gesture	Action
☝️ Index Finger	Draw
✊ Fist	Stop Drawing
🖐️ Open Palm	Clear Canvas
q Key	Quit
📸 Output

Live webcam feed with hand landmarks

Real-time drawing on a virtual canvas

Separate canvas window for clean drawing view

🔮 Future Enhancements

🌐 Web-based Air Canvas using Flask / Streamlit

💾 Download drawings as images

🎨 Color and brush size selection

🤖 AI-based shape recognition

🎓 Use Cases

Touchless drawing systems

Online whiteboards

Virtual classrooms

Gesture-controlled interfaces

👨‍💻 Author

Navamani Kandan
Undergraduate Student – Engineering
📍 India

⭐ Acknowledgments

MediaPipe by Google

OpenCV Community
