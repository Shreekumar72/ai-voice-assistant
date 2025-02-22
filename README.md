# AI Voice Assistant Project

## 📜 Description
An AI Voice Assistant API built with FastAPI. It processes text input and provides responses using NLP techniques.

## 🌐 Deployed URL
- [API Endpoint](https://ai-voice-assistant-production-42b1.up.railway.app)
- [API Documentation (Swagger UI)](https://ai-voice-assistant-production-42b1.up.railway.app/docs/)

## 💻 Installation (Local Setup)
```bash
# Clone the repository
git clone https://github.com/Shreekumar72/ai-voice-assistant.git

# Navigate into the project directory
cd ai-voice-assistant

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
