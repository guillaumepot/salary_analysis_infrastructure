#api

from fastapi import FastAPI
import joblib
import pandas as pd
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel, Field
import uvicorn



app = FastAPI(
    title = 'Exam API',
    description = 'Exam3',
    version = '1',
    debug = True
)

Instrumentator().instrument(app).expose(app)


# Pydantic validation
class DataModel(BaseModel):
    company: int = Field(..., description = "Company index")
    gender: int = Field(..., description = "Gender")
    position_level: int = Field(..., description = "Position level")
    performance_score: float = Field(..., description = "Performance score")
    work_hours_per_week: int = Field(..., description = "Work hours per week")
    experience_years: int = Field(..., description = "Experience years")
    has_certifications: bool = Field(..., description = "Has certifications")
    promoted: bool = Field(..., description = "Promoted")


# Routes
@app.get('/hello')
def hello():
        return {'message': 'Hello World!'}

@app.post('/predict')
def predict(data: DataModel):
    model = joblib.load('./models/model.pkl')
    scaler = joblib.load('./models/scaler.pkl')

    data_dict = data.model_dump()
    columns = ["company", "gender", "position_level", "performance_score", 
               "work_hours_per_week", "experience_years", "has_certifications",
               "promoted"]

    df = pd.DataFrame([data_dict], columns = columns)
    df_scaled = scaler.transform(df)

    preds = model.predict(df_scaled)

    return {'predictions': preds.tolist()}


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)