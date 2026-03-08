# 🍎 AI Food Freshness Detector

An AI-powered **Computer Vision project** that detects whether a fruit is **Fresh** or **Rotten** using deep learning.

The system uses a trained **PyTorch model** and provides multiple ways to test predictions:

* Upload an image
* Use a web interface
* Use **real-time camera detection**

This project demonstrates a **complete AI workflow**:

Dataset → Model Training → Model Saving → API → Web Interface → Real-Time Detection

---

# 🚀 Features

✔ Detects **Fresh vs Rotten fruits**
✔ Deep learning image classification
✔ Backend API built with **FastAPI**
✔ Interactive UI using **Streamlit**
✔ Real-time webcam detection using **OpenCV**
✔ Easy-to-understand project structure

---

# 🧠 Technologies Used

* Python
* PyTorch
* Torchvision
* FastAPI
* Streamlit
* OpenCV
* Pillow

---

# 📂 Project Structure

```
AI-Food-Detector
│
├── dataset
│   ├── train
│   │   ├── fresh
│   │   └── rotten
│   │
│   └── val
│       ├── fresh
│       └── rotten
│
├── models
│   └── freshness_model.pth
│
├── uploads
│
├── train_freshness.py
├── detect.py
├── camera_detect.py
├── main.py
├── app.py
└── README.md
```

---

# 📊 Dataset

Dataset used for training:

https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification

After downloading the dataset, organize it like this:

```
dataset/

train/
   fresh → 150 images
   rotten → 150 images

val/
   fresh → 30 images
   rotten → 30 images
```

Balanced datasets help improve model performance.

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-food-freshness-detector.git
cd ai-food-freshness-detector
```

Create a virtual environment:

```
python -m venv venv
```

Activate environment

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install fastapi uvicorn torch torchvision pillow python-multipart streamlit opencv-python
```

---

# 🏋️ Model Training

Train the deep learning model:

```
python train_freshness.py
```

After training finishes, the model will be saved as:

```
models/freshness_model.pth
```

---

# ▶️ Run the API Server

Start the FastAPI server:

```
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 💻 Run the Web Interface

Start the Streamlit application:

```
streamlit run app.py
```

The interface will open in your browser.

Upload an image and the model will predict whether the fruit is **Fresh or Rotten**.

---

# 📷 Real-Time Camera Detection

Run webcam detection:

```
python camera_detect.py
```

The webcam will open and display predictions directly on the camera screen.

Press **Q** to exit.

---

# 📦 Example API Response

```
{
 "prediction": "fresh"
}
```

or

```
{
 "prediction": "rotten"
}
```

---

# 🔮 Future Improvements

* Detect **multiple fruit types**
* Add **confidence scores**
* Implement **object detection**
* Deploy model to **cloud platforms**
* Build a **mobile application**

---

# 👨‍💻 Author

Developed as a **Computer Vision / AI project** to explore deep learning applications in food quality detection.

---

⭐ If you found this project useful, consider **starring the repository**.
