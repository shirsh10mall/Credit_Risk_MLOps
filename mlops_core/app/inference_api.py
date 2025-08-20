from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="mlops_core - inference API")


class PredictRequest(BaseModel):
    features: dict


@app.get("/feature-metadata")
def feature_metadata():
    # return a simple example; replace with real metadata store logic
    return {"features": ["age", "income", "loan_amount", "tenure", "num_accounts"]}


@app.post("/predict")
def predict(req: PredictRequest):
    # placeholder model — replace with actual model load & predict
    # Here we simply echo back a random decision for demonstration
    features = req.features
    # TODO: load model from MLflow artifacts, preprocess features, return prediction
    return {"prediction": "approve", "probability": 0.86, "features_received": features}


@app.post("/validate-data")
def validate_data(payload: dict):
    # Hook into Great Expectations validations in real implementation
    return {"status": "validation triggered", "details": {}}


@app.post("/run-training")
def run_training(payload: dict):
    # Should call train_model.py (or trigger Airflow DAG)
    return {"status": "training started (stub)"}


@app.get("/shap-summary")
def shap_summary():
    # Placeholder for SHAP summary data
    return {"shap": "not computed yet"}
