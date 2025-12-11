from fpdf import FPDF
# pip install fpdf

image_list = [
    "image1.jpg",
    "image2.jpg"
]

pdf = FPDF()

for image in image_list:
    pdf.add_page()
    pdf.image(image, x=10, y=10, w=190)

pdf.output("your file.pdf", "F")
print("PDF created successfully!")
