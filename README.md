# Creative_DAT_Assignment

# House_Model
# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project predicts house prices using **Linear Regression** based on features like:

* Total Square Feet
* Price per Square Feet
* Number of Bedrooms (BHK)

It includes complete steps of a Machine Learning pipeline:
👉 Data Cleaning → Preprocessing → Model Training → Evaluation → Prediction

---

## 🚀 Features

* ✅ Data cleaning (₹, Cr, Lac conversion)
* ✅ Handling missing values (NaN)
* ✅ Feature engineering
* ✅ Data scaling using StandardScaler
* ✅ Model training using Linear Regression
* ✅ Evaluation using:

  * R² Score
  * RMSE
  * MAE
* ✅ User input-based prediction system

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📂 Dataset

The dataset contains housing details such as:

* `Flat_Price`
* `Total_Sq.ft`
* `Price_per_sq.ft`
* `BHK`
* Location and other metadata

---

## ⚙️ Installation

Install required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ How to Run

1. Open Jupyter Notebook
2. Load the dataset (`House_Price.csv`)
3. Run all cells step-by-step
4. Enter values when prompted:

   * Total Sq.ft
   * Price per Sq.ft
   * BHK
5. Get predicted house price

---

## 📊 Model Performance

Example results:

* R² Score: ~0.83
* RMSE: ~15 Lac
* MAE: ~8 Lac

---

## 🔍 Data Cleaning Process

* Removed symbols like ₹, commas, text
* Converted values into numeric format
* Handled invalid values using `NaN`
* Used regex:

```python
re.sub("[^0-9.]", "", x)
```

---

## ⚠️ Known Issues

* Small dataset may reduce accuracy
* Some columns contain missing values
* Predictions may be inaccurate for extreme inputs
* Negative predictions possible due to limited data

---

## 🔧 Future Improvements

* Add more training data
* Improve feature selection
* Remove outliers
* Try advanced models (Random Forest, XGBoost)
* Deploy as web app

---

## 👨‍💻 Author

Shreyas M. Kapadiya

---

⭐ If you found this helpful, give it a star!


🔹 What is re.sub?
re = regular expression (regex) → pattern matching
sub = substitute (replace)

👉 So:

re.sub(pattern, replace, text)

Means:
👉 “pattern ko text me dhundo aur replace kar do”

🔹 Your Code
re.sub("[^0-9.]", "", x)
