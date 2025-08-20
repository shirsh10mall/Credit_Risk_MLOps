import os

import gradio as gr
import requests

API_URL = os.environ.get("MLOPS_API_URL", "http://localhost:8000")


def predict_ui(age, income, loan_amount, tenure, num_accounts):
    payload = {
        "features": {
            "age": age,
            "income": income,
            "loan_amount": loan_amount,
            "tenure": tenure,
            "num_accounts": num_accounts,
        }
    }
    try:
        resp = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


iface = gr.Interface(
    fn=predict_ui,
    inputs=[
        gr.Number(label="age", value=30),
        gr.Number(label="income", value=60000),
        gr.Number(label="loan_amount", value=12000),
        gr.Number(label="tenure", value=24),
        gr.Number(label="num_accounts", value=2),
    ],
    outputs="text",
    title="MLOPS Core Gradio UI",
    description="Single-prediction demo (calls FastAPI /predict endpoint).",
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, share=False)
