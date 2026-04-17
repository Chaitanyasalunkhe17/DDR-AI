import fitz  # PyMuPDF
import os

def extract_pdf_data(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    image_paths = []

    os.makedirs("images", exist_ok=True)

    for page_index in range(len(doc)):
        page = doc[page_index]
        full_text += page.get_text()

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            img_path = f"images/page{page_index}_img{img_index}.png"
            with open(img_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(img_path)

    return full_text, image_paths