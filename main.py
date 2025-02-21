from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nlp import process_text
from database import save_interaction

app = FastAPI()

class InputText(BaseModel):
    text: str

from fastapi import FastAPI
from pydantic import BaseModel
from nlp import process_text
from database import save_interaction

app = FastAPI()

# ✅ Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Voice Assistant API!"}

# ✅ Text processing route
class InputText(BaseModel):
    text: str

@app.post("/process-text/")
def process_input(input: InputText):
    response = process_text(input.text)
    save_interaction(input.text, response)
    return {"response": response}


