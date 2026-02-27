import argparse
from pathlib import Path
import joblib
import pandas as pd
import numpy as np

def load_model(models_dir: Path, name: str):
    path = models_dir / f"{name}.joblib"
    obj = joblib.load(path)
    print(f"Loaded model: {path}")
    return obj

def predict_classification(model_obj, X: pd.DataFrame) -> pd.DataFrame:
    pipe = model_obj["pipeline"]
    class_names = model_obj["class_names"]
    proba = pipe.predict_proba(X)
    pred_idx = np.argmax(proba, axis=1)
    pred_label = [class_names[i] for i in pred_idx]
    out = X.copy()
    out["pred_label"] = pred_label
    out["pred_confidence"] = proba.max(axis=1)
    return out

def predict_regression(model_obj, X: pd.DataFrame) -> pd.DataFrame:
    pipe = model_obj["pipeline"]
    pred = pipe.predict(X)
    out = X.copy()
    out["prediction"] = pred
    return out

def main():
    p = argparse.ArgumentParser(description="Client-ready inference CLI")
    p.add_argument("--task", choices=["classification", "regression"], required=True)
    p.add_argument("--model", required=True, help="Model name without .joblib (e.g. classification_pipeline)")
    p.add_argument("--input_csv", required=True)
    p.add_argument("--output_csv", required=True)
    p.add_argument("--models_dir", default="models")
    args = p.parse_args()

    models_dir = Path(args.models_dir)
    df = pd.read_csv(args.input_csv)

    model_obj = load_model(models_dir, args.model)

    if args.task == "classification":
        preds = predict_classification(model_obj, df)
    else:
        preds = predict_regression(model_obj, df)

    out_path = Path(args.output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    preds.to_csv(out_path, index=False)
    print(f"Saved predictions: {out_path}")

if __name__ == "__main__":
    main()
