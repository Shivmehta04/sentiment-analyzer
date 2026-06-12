# 📊 Sentiment Analyzer (NLP + Streamlit)

A Machine Learning-based **Sentiment Analysis Web App** that predicts whether a given text expresses **positive, negative, or neutral sentiment**.

---

## 🚀 Live Demo

👉 (https://sentiment-analyzer-project-nlp.streamlit.app/)

---

## 📌 Features

* Clean and interactive **Streamlit UI**
* Real-time **sentiment prediction**
* Preprocessing using **NLTK**
* Machine Learning model with **TF-IDF Vectorizer**
* Visual insights (Feature Importance Graph)

---

## 🧠 Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* NLTK
* Streamlit

---

## 📂 Project Structure

```
sentiment-analyzer/
│
├── .streamlit/
│   └── config.toml
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_building.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone [https://github.com/Shivmehta04/sentiment-analyzer.git](https://github.com/Shivmehta04/sentiment-analyzer)
cd sentiment-analyzer
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 📊 Model Details

* Text preprocessing using NLTK
* Feature extraction using TF-IDF
* Trained using classification algorithms
* Saved model and vectorizer for reuse

---

## 👨‍💻 Author

**Shiv Mehta**

---

## ⭐ Contribute

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and free to use.
