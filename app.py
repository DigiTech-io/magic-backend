from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

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
    input_data = await file.read()
    img = Image.open(io.BytesIO(input_data))

    # इमेज को छोटा करना ताकि सर्वर क्रैश न हो
    max_size = 800
    if img.width > max_size:
        ratio = max_size / float(img.width)
        new_height = int(float(img.height) * float(ratio))
        img = img.resize((max_size, new_height), Image.LANCZOS)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    output_image = remove(img_byte_arr.getvalue())

    return Response(content=output_image, media_type="image/png")


