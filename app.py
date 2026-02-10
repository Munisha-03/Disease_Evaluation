from fastapi import FastAPI
from main import get_disease_details, TextInput, DiseaseDetails, disease_verify

app = FastAPI()

@app.get("/get")
async def home():
    return {"health_check": "OK"}

@app.post("/get_disease_details")
async def response(disease: TextInput):
    result = await disease_verify(disease)
    return result




