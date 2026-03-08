# 🍎 AI Food Freshness Detector

An AI-powered computer vision project that detects whether a fruit is **Fresh** or **Rotten** using deep learning.

The system is built using **PyTorch for model training** and **FastAPI for backend inference**. Users can upload an image of food and receive a prediction about its freshness.

---

# 🚀 Features

* Detects **Fresh vs Rotten fruits**
* Deep learning image classification
* REST API built with **FastAPI**
* Supports image upload for prediction
* Modular and easy-to-understand project structure
* Easy to extend for more food categories

---

# 🧠 Technologies Used

* Python
* PyTorch
* Torchvision
* FastAPI
* Uvicorn
* Pillow
* Computer Vision

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
├── main.py
└── README.md
```

---

# 📊 Dataset

This project uses a **Fresh and Rotten Fruits image dataset**.

Download dataset from:

https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification

After downloading, organize the dataset like this:

```
dataset/

train/
   fresh → 150 images
   rotten → 150 images

val/
   fresh → 30 images
   rotten → 30 images
```

Make sure **both classes contain equal number of images** for balanced training.

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

### Mac / Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install fastapi uvicorn torch torchvision pillow python-multipart
```

---

# 🏋️ Model Training

Train the deep learning model using:

```
python train_freshness.py
```

After training completes, the model will be saved as:

```
models/freshness_model.pth
```

---

# 🔍 Prediction System

The trained model is loaded in `detect.py` and used by the FastAPI backend to classify images.

Example predictions:

```
Fresh
```

or

```
Rotten
```

---

# ▶️ Running the API Server

Start the FastAPI server:

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📡 API Documentation

FastAPI automatically generates interactive API documentation.

Open in your browser:

```
http://127.0.0.1:8000/docs
```

Steps:

1. Click **POST /analyze**
2. Click **Try it out**
3. Upload a fruit image
4. Click **Execute**

The system will return the prediction.

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

* Detect **multiple food categories**
* Add **real-time camera detection**
* Improve dataset size for better accuracy
* Deploy model to **cloud platforms**
* Build **mobile app interface**

---

# 👨‍💻 Author

AI Computer Vision project developed for learning **deep learning and food quality detection systems**.

---

⭐ If you like this project, consider **starring the repository on GitHub**.
