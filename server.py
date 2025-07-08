import torch
import os
import atexit
import signal
from fastapi import FastAPI
from faster_whisper import WhisperModel

AUDIO_PATH = "/tmp/recording.wav"

# Load the Faster Whisper Medium model on GPU
model = WhisperModel("medium", device="cuda", compute_type="float16")

def cleanup():
    """Free CUDA memory and release resources."""
    print("Cleaning up CUDA memory...")
    if model is not None:
        model = None  # Remove reference to model
    torch.cuda.empty_cache()  # Clear CUDA memory cache
    print("CUDA memory cleared.")

# Register cleanup for normal exit
atexit.register(cleanup)

# Handle interrupt signals (e.g., Ctrl+C)
def signal_handler(sig, frame):
    cleanup()
    import sys
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

app = FastAPI()

@app.get("/transcribe")
async def transcribe():
    if not os.path.exists(AUDIO_PATH):
        return "No audio file. Please, record it."
    # Transcribe the audio file
    segments, info = model.transcribe(AUDIO_PATH)
    # Join all segments text
    full_text = "".join([segment.text for segment in segments])
    return full_text

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=False)  # Disable reload
