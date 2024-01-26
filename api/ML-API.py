from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Charger le modèle RandomForestRegressor
model = joblib.load(r"data/rfm.pkl")

@app.post("/sq2_price_predictor_v1/", description="Retourne une prédiction de prix au m²")
async def sq2_price_predictor(longitude: float, latitude: float, date_transaction: int):    
    input_data = np.array([[longitude, latitude, date_transaction]])    
    return model.predict(input_data)[0]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
