from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .model import model, columns
from .schemas import PropertyInput

app = FastAPI()

# Allow CORS for frontend (replace with your frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://real-estate-price-prediction-dun.vercel.app",  # deployed frontend
        "http://localhost:3000"  # local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
def predict(input: PropertyInput):
    """Predict home price based on input features."""
    try:
        # One-hot encode location
        loc_index = columns.index(input.location.lower(
        )) if input.location.lower() in columns else -1
        x = [0] * len(columns)
        x[0] = input.area
        x[1] = input.bhk
        x[2] = input.bath
        if loc_index >= 0:
            x[loc_index] = 1

        # Predict
        price = model.predict([x])[0]
        return {"predicted_price": round(price, 2)}
    except Exception as e:
        return {"error": str(e)}
