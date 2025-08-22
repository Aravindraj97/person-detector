Person Detector 🚀

A Dockerized application for detecting persons using AI/ML. This project includes a REST API to serve predictions and can be easily deployed with Docker.

📌 Features

Person detection using deep learning (YOLO/Custom model).

REST API built with Flask/FastAPI.

Dockerized for portability and easy deployment.

Configurable via .env file.

🛠️ Tech Stack

Python 3.11

Flask / FastAPI

Docker

OpenCV / PyTorch / TensorFlow (update based on what you used)

📂 Project Structure
├── app.py              # Main application  
├── functions.py        # Utility functions  
├── requirements.txt    # Python dependencies  
├── Dockerfile          # Docker image definition  
├── .env                # Environment variables  
├── data/               # Sample data (if any)  
└── README.md           # Project documentation  

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/Aravindraj97/person-detector.git
cd person-detector

2️⃣ Build the Docker image
docker build -t person-detector .

3️⃣ Run the container
docker run -p 8000:8000 person-detector

4️⃣ Access the API

Open: http://localhost:8000

Example endpoint:

curl -X POST http://localhost:8000/predict -F "file=@sample.jpg"

⚙️ Environment Variables

You can configure values in a .env file:

DB_HOST=localhost
DB_PORT=5432
MODEL_PATH=models/person_detector.pt

📦 Dependencies

Dependencies are listed in requirements.txt and installed during Docker build.

📊 Results
<img width="1421" height="817" alt="image" src="https://github.com/user-attachments/assets/2779ccf9-15a1-4dd1-b80a-09c58b4b6a97" />




📜 License

This project is licensed under the MIT License.
