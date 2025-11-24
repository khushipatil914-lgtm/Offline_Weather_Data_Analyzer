# 📘 **README — Offline Weather Analyzer**

## 🌤️ **Project Title:**

**Offline Weather Analyzer: A Local Climate Data Processing & Prediction System**

---

## 📌 **Overview**

This project is a **Python-based offline weather analysis tool** designed to work **without internet access**.
It reads weather data stored locally in CSV format and provides:

* Automatic data loading
* Summary analytics
* Weather visualization
* Temperature prediction
* Command-line interface

The system follows a **modular design** and matches VIT’s *Build Your Own Project* guidelines.

---

## 🎯 **Features**

### ✔ **1. Data Loading**

* Loads weather CSV files locally
* Auto-parses dates, temperature, humidity, wind & rainfall
* Handles invalid rows gracefully

### ✔ **2. Summary Analysis**

* Average temperature
* Minimum & maximum temperature
* Average humidity
* Average wind speed
* Total precipitation
* Heatwave detection (3+ consecutive hot days)

### ✔ **3. Visualization**

Generates:

* Temperature time-series graph
  Saved as:

```
temperature.png
```

### ✔ **4. Weather Prediction**

Uses a linear regression model to predict future temperatures for user-selected days using:

```
--predict_days N
```

### ✔ **5. Command-Line Interface**

Run the full project from terminal using:

```
python -m src.cli ...
```

---

## 🧱 **Project Folder Structure**

```
weather_report_analyzer/
│
├─ README.md
├─ statement.md
├─ requirements.txt
├─ report.md
│
├─ sample_data/
│     └─ weather_data.csv
│
└─ src/
      ├─ __init__.py
      ├─ cli.py
      ├─ data_loader.py
      ├─ analyzer.py
      ├─ visualizer.py
      ├─ predictor.py
      └─ preprocess.py
```

---

## ⚙️ **How to Run the Project (VS Code / CMD)**

### ▶ **1. Run Summary Analysis (NO extra libraries needed)**

```
python -m src.cli --data sample_data/weather_data.csv --mode summary
```

Output saved to:

```
results.txt
```

---

### ▶ **2. Install required libraries**

For visualization & prediction:

```
pip install -r requirements.txt
```

---

### ▶ **3. Run Visualization**

```
python -m src.cli --data sample_data/weather_data.csv --mode visualize
```

Generates:

```
temperature.png
```

---

### ▶ **4. Run Prediction**

```
python -m src.cli --data sample_data/weather_data.csv --mode predict --predict_days 3
```

---

## 🛠️ **Technologies Used**

* Python 3
* CSV parsing
* Matplotlib (visualization)
* Scikit-learn (prediction)
* Statistics module (analysis)

---

## 🔍 **Use Cases**

* Offline weather reporting
* Small research analysis
* Rural/remote area applications
* Student engineering projects

---

## 🚀 **Future Enhancements**

* GUI dashboard (Tkinter)
* Multi-graph visualization
* Rainfall prediction
* Monthly/seasonal trend analysis
* Export full report as PDF

---

## 👤 **Author**

Name:Khushboo Vinod Patil
Reg. no. 25MIM10104
VIT VBHOPAL UNIVERSITY
