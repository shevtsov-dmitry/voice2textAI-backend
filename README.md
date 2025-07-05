### Model to convert voice to text:

__Faster Whisper Medium__
`https://huggingface.co/guillaumekln/faster-whisper-medium`


### Requirements 
```bash
pip install faster-whisper fastapi uvicorn
pip install torch --index-url https://download.pytorch.org/whl/cu121 # Needed for Nvidia Cuda support
pip install --upgrade ctranslate2
```


### Run app from venv using command
```bash
python3 server.py
```
