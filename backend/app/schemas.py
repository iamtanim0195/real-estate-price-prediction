from pydantic import BaseModel

class PropertyInput(BaseModel):
    """Input schema for prediction request."""
    area: float      # Square footage
    bhk: int         # Number of bedrooms
    bath: int        # Number of bathrooms
    location: str    # Bangalore location (e.g., "Rajaji Nagar")