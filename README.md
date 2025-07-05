### Model to convert voice to text:

__Faster Whisper Medium__
`https://huggingface.co/guillaumekln/faster-whisper-medium`

This model will be automatically downloaded from Hugging Face to the `.cache` directory when the application starts for the first time.

### Requirements 

Install python packages.

```bash
pip install faster-whisper fastapi uvicorn
pip install torch --index-url https://download.pytorch.org/whl/cu121 # Needed for Nvidia Cuda support
pip install --upgrade ctranslate2
```

Install CUDA Runtime for your OS from  `https://developer.nvidia.com/cudnn`. \
If not installed the app will crash requiring CUDA libraries.

### Run app from venv using command
```bash
python3 server.py
```

_HINT: you can use this command to record audio as an example for the app._

```bash
arecord -f cd /tmp/recording.wav
```

### API Endpoints

- **GET /transcribe**: Transcribes an audio file and returns the text transcription. The audio file should be located at `/tmp/recording.wav`.