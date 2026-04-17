from fastapi import FastAPI, UploadFile, File
import shutil
from extractor import extract_pdf_data
from llm import generate_ddr

app = FastAPI()

@app.post("/generate-ddr")
async def generate_ddr_api(
    inspection: UploadFile = File(...),
    thermal: UploadFile = File(...)
):
    # Save uploaded files
    with open("inspection.pdf", "wb") as f:
        shutil.copyfileobj(inspection.file, f)

    with open("thermal.pdf", "wb") as f:
        shutil.copyfileobj(thermal.file, f)

    # Extract data
    inspection_text, inspection_images = extract_pdf_data("inspection.pdf")
    thermal_text, thermal_images = extract_pdf_data("thermal.pdf")

    # Generate report
    report = generate_ddr(inspection_text, thermal_text)

    return {
        "report": report,
        "images": inspection_images + thermal_images
    }