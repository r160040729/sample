import os
import fitz  # PyMuPDF

upload_dir = os.getenv('UPLOAD_DIR', 'uploads')
output_dir = os.getenv('OUTPUT_DIR', 'outputs')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(upload_dir):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(upload_dir, file_name)
        doc = fitz.open(file_path)

        # Example: Add a watermark to each page
        for page in doc:
            page.insert_text((72, 72), "Watermark", fontsize=20, color=(0, 0, 0))

        output_path = os.path.join(output_dir, file_name.replace('.pdf', '_watermarked.pdf'))
        doc.save(output_path)
        print(f'Processed {file_path} -> {output_path}')
