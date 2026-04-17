import streamlit as st
import requests

st.title("🏠 AI DDR Report Generator")

inspection = st.file_uploader("Upload Inspection Report", type="pdf")
thermal = st.file_uploader("Upload Thermal Report", type="pdf")

if st.button("Generate DDR"):
    if inspection and thermal:
        files = {
            "inspection": ("inspection.pdf", inspection, "application/pdf"),
            "thermal": ("thermal.pdf", thermal, "application/pdf"),
        }

        with st.spinner("Generating report..."):
            response = requests.post(
                "http://localhost:8000/generate-ddr",
                files=files
            )

        data = response.json()

        st.subheader("📄 DDR Report")
        st.write(data["report"])

        st.subheader("🖼️ Extracted Images")
        for img_path in data["images"]:
            try:
                st.image(img_path)
            except:
                st.write(f"Image not available: {img_path}")
    else:
        st.warning("Please upload both files")