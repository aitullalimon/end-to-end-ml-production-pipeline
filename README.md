# End-to-End ML Production Pipeline (Ready Template)

Badges: Python | scikit-learn | Docker | CLI Inference

This repo is a reusable ML production template (classification + regression) with:
- EDA reports
- preprocessing pipelines
- cross-validation
- metrics
- model saving
- batch inference (CLI)
- optional Docker run

Badges: Python | scikit-learn | Docker | CLI Inference

This repo is a reusable ML production template (classification + regression) with:
- EDA reports
- preprocessing pipelines
- cross-validation
- metrics
- model saving
- batch inference (CLI)
- optional Docker run

## Overview

This project demonstrates a fully production-ready Machine Learning pipeline including:

- Data ingestion
- Advanced EDA
- Feature engineering (ColumnTransformer)
- Cross-validation
- Metrics (F1, ROC-AUC, MAPE)
- Model saving (joblib)
- Inference module
- Batch prediction export (CSV)

---

## Architecture

Raw Data -> EDA -> Preprocessing -> Model Training -> Cross Validation -> Model Saving -> Inference -> Prediction Export

---

## How to Run (Local)

1) Install dependencies:

pip install -r requirements.txt

2) Start Jupyter:

jupyter notebook

3) Run the notebook in notebooks/

Models saved in models/
Predictions saved in predictions/

---

## Run with Docker

Build and start container:

docker compose up --build

Then open in browser:

http://localhost:8888

---

## CLI Inference (No Notebook Required)

Classification example:

python src/predict_cli.py --task classification --model classification_pipeline --input_csv data/sample_cls.csv --output_csv predictions/cls_out.csv

Regression example:

python src/predict_cli.py --task regression --model regression_pipeline --input_csv data/sample_reg.csv --output_csv predictions/reg_out.csv

---

Use cases: fraud detection, risk scoring, forecasting, research, analytics.
