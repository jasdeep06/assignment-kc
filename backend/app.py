from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.post("/predict")
def predict(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    records = df.to_dict('records')
    
    return {"data": records}

