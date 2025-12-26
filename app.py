from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
import uvicorn
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Image Remover API is running!"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    image_data = await file.read()
    # Background remove karne ka main function
    output_data = remove(image_data)
    return Response(content=output_data, media_type="image/png")

if __name__ == "__main__":
    # Render ka port detect karne ke liye ye lines sabse zaroori hain
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
import os
import uvicorn

# ... aapka baki code ...

if __name__ == "__main__":
    # Ye line Render ke dynamically assigned port ko uthayegi
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)