import joblib
from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
async def root(size: int, nb_bedrooms: int, garden: int):
    model = joblib.load('regression.joblib')
    print(size, nb_bedrooms, garden)
    return model.predict([[size, nb_bedrooms, garden]])[0]