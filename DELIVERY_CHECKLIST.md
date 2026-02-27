# Client Delivery Checklist

Project: End-to-End ML Production Pipeline
Date: 2026-02-28

------------------------------------------

PROJECT STRUCTURE INCLUDED:

- data/
- models/ (compressed models only)
- predictions/
- reports/
- src/
- Dockerfile
- docker-compose.yml
- requirements.txt
- README.md
- run_local.sh

------------------------------------------

HOW TO RUN LOCALLY:

1) Install dependencies:
   pip install -r requirements.txt

2) Start Jupyter:
   jupyter notebook

------------------------------------------

HOW TO RUN WITH DOCKER:

docker compose up --build

Then open:
http://localhost:8888

------------------------------------------

CLI INFERENCE EXAMPLE:

Classification:
python src/predict_cli.py --task classification --model classification_pipeline_compressed --input_csv data/sample_cls.csv --output_csv predictions/cls_out.csv

Regression:
python src/predict_cli.py --task regression --model regression_pipeline_compressed --input_csv data/sample_reg.csv --output_csv predictions/reg_out.csv

------------------------------------------

DELIVERY NOTES:

- Models are compressed for efficient transfer.
- EDA reports are pre-generated in reports/eda.
- Prediction outputs are saved in predictions/.
- Project is fully production-structured.

------------------------------------------

Delivered by: Nexora Labs
