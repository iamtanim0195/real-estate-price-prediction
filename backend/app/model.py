import pickle
import json
from pathlib import Path

# Load model and columns
MODEL_PATH = Path(__file__).parent.parent / "data" / "banglore_home_prices_model.pickle"
COLUMNS_PATH = Path(__file__).parent.parent / "data" / "columns.json"

def load_model():
    """Load the pre-trained model and location columns."""
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(COLUMNS_PATH, "r") as f:
        columns = json.load(f)["data_columns"]
    return model, columns

model, columns = load_model()