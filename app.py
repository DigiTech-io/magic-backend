from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from rembg import remove
import io

app = FastAPI()

# Frontend से जुड़ने के लिए अनुमति (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Magic Toolbox Backend is READY!"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)
    return Response(content=output_image, media_type="image/png")