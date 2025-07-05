from fastapi import FastAPI
from faster_whisper import WhisperModel

AUDIO_PATH = "/tmp/recording.wav"

# Load the Faster Whisper Medium model on GPU
model = WhisperModel("medium", device="cuda", compute_type="float16")

app = FastAPI()

@app.get("/transcribe")
async def transcribe():
    # Transcribe the audio file
    segments, info = model.transcribe(AUDIO_PATH)
    # Join all segments text
    full_text = " ".join([segment.text for segment in segments])
    return {"text": full_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
