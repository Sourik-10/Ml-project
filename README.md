## End to end data science project
# 🎓 Student Performance Predictor — End-to-End ML Pipeline

A **production-grade, modular machine learning pipeline** that predicts student exam performance based on demographic and academic input features. Built with industry-standard MLOps practices — not just a notebook, but a fully structured, deployable ML system.

---

## 🚀 Live Demo

> Flask web app — run locally or deploy to any cloud platform.

---

## 📌 Project Highlights

- ✅ Modular `src/` package architecture (data ingestion → transformation → model training)
- ✅ MySQL database integration for raw data ingestion
- ✅ Automated hyperparameter tuning across 6+ ML models
- ✅ DVC (Data Version Control) for reproducible data and artifact versioning
- ✅ Custom logging and exception handling throughout the pipeline
- ✅ GitHub Actions CI/CD for automated testing and deployment
- ✅ Flask web app for real-time predictions

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.x |
| ML Models | Scikit-learn, XGBoost, CatBoost |
| Data Processing | Pandas, NumPy |
| Database | MySQL (`mysql-connector-python`, `pymysql`) |
| Visualization | Matplotlib, Seaborn |
| Data Versioning | DVC |
| Web Framework | Flask |
| CI/CD | GitHub Actions |
| Environment | `python-dotenv` |

---

## 🗂️ Project Structure

```
Ml-project/
├── src/
│   └── ml_project/
│       ├── components/
│       │   ├── data_ingestion.py       # Pulls data from MySQL, splits train/test
│       │   ├── data_transformation.py  # Feature engineering, preprocessing pipelines
│       │   └── model_trainer.py        # Trains & evaluates multiple models
│       ├── logger.py                   # Custom logging setup
│       └── exception.py               # Custom exception handler
├── notebook/                           # EDA and experimentation notebooks
├── artifact/                           # Saved model artifacts
├── .github/
│   └── workflows/                      # GitHub Actions CI/CD pipeline
├── .dvc/                               # DVC configuration
├── app.py                              # Main pipeline runner
├── main.py                             # Flask app entry point
├── setup.py                            # Package setup
├── requirements.txt
└── README.md
```

---

## ⚙️ ML Pipeline Flow

```
MySQL Database
      │
      ▼
Data Ingestion
(train/test split → saved to artifact/)
      │
      ▼
Data Transformation
(imputation → encoding → scaling → ColumnTransformer pipeline)
      │
      ▼
Model Trainer
(trains 6+ models with GridSearchCV hyperparameter tuning)
      │
      ▼
Best Model Selection
(evaluated on R² score → serialized with pickle)

```
---

## 🤖 Models Trained & Compared

| Model | Notes |
|---|---|
| Linear Regression | Baseline |
| Ridge Regression | L2 regularization |
| Lasso Regression | L1 regularization |
| Random Forest Regressor | Ensemble |
| XGBoost Regressor | Gradient boosting |
| CatBoost Regressor | Handles categoricals natively |

Best model is automatically selected based on R² score on the test set and saved to the `artifact/` directory.

---

## 📊 Features Used

| Feature | Type |
|---|---|
| Gender | Categorical |
| Race/Ethnicity | Categorical |
| Parental Level of Education | Categorical |
| Lunch Type | Categorical |
| Test Preparation Course | Categorical |
| Reading Score | Numerical |
| Writing Score | Numerical |

**Target Variable:** Math Score

---

## 🧪 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Sourik-10/Ml-project.git
cd Ml-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root directory:
```env
MYSQL_HOST=your_host
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DB=your_database
```

### 4. Run the pipeline
```bash
python app.py
```

### 5. Launch the Flask app
```bash
python main.py
```
## 🔄 CI/CD with GitHub Actions

The `.github/workflows/` directory contains automated workflows that:
- Install dependencies on push
- Run the pipeline to verify data ingestion and model training
- Ensure no breaking changes are introduced

---

## 📦 Data Versioning with DVC

This project uses [DVC](https://dvc.org/) to version datasets and model artifacts, ensuring full reproducibility across environments.

```bash
# Pull data and artifacts
dvc pull
```

---

## 📈 Results

The best-performing model achieves strong predictive accuracy on student math scores. Detailed metrics and visualizations are available in the `notebook/` directory.

---

## 👤 Author

**Sourik Ghosh**
- GitHub: [@Sourik-10](https://github.com/Sourik-10)
- LinkedIn: [linkedin.com/in/sourik-ghosh-016728252](https://www.linkedin.com/in/sourik-ghosh-016728252/)

---

## ⭐ Show Your Support

If you found this project useful, give it a ⭐ on GitHub!
