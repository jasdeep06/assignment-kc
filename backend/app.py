from fastapi import FastAPI, File, UploadFile
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict/")
def predict(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    records = df.to_dict('records')
    
    return records

