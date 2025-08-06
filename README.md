Here's a comprehensive `README.md` file for your Real Estate Price Prediction Project:

```markdown
# Real Estate Price Prediction Project
A machine learning project that predicts Bengaluru house prices based on location, square footage, number of bathrooms, and BHK (bedroom-hall-kitchen) count.

## Live Demo

👉 [Frontend Application](https://real-estate-frontend-jet-three.vercel.app/)

## Dataset

The model was trained using the [Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) from Kaggle.

## Machine Learning Approach

### Model Selection
We evaluated three regression models using GridSearchCV:
1. **Linear Regression**
   - Best score: 0.8297
   - Best params: {'fit_intercept': False, 'positive': False}
2. **Lasso Regression**
   - Best score: 0.6729
   - Best params: {'alpha': 1, 'selection': 'cyclic'}
3. **Decision Tree Regressor**
   - Best score: 0.6963
   - Best params: {'criterion': 'friedman_mse', 'splitter': 'best'}

### Selected Model
We proceeded with **Linear Regression** as it showed the best performance.

### Prediction Function
```python
def predict_price(location, sqft, bath, bhk):
    loc_index = np.where(X.columns==location)[0][0]
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return lr_clf.predict([x])[0]
```

## Technologies Used

### Backend
- Python 3.8+
- FastAPI (REST API framework)
- scikit-learn (Machine Learning)
- pandas (Data processing)
- uvicorn (ASGI server)

### Frontend
- Next.js 14
- React
- Tailwind CSS (Styling)
- Axios (API calls)

## Deployment

The project is deployed using:
- **Backend**: Render (FastAPI)
- **Frontend**: Vercel (Next.js)

## How to Run Locally

### Backend Setup
1. Navigate to backend folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

- `POST /predict`: Accepts JSON with location, sqft, bath, bhk parameters
- `GET /locations`: Returns list of available locations


Would you like me to add or modify any sections? For example, we could include:
- Screenshots of the application
- More detailed API documentation
- Contribution guidelines
- Troubleshooting section
