
# import fitz
# import os


# def extract_pdf_data(pdf_path, image_output="outputs/images"):

#     os.makedirs(image_output, exist_ok=True)

#     doc = fitz.open(pdf_path)

#     full_text = ""
#     images = []

#     for page_index in range(len(doc)):

#         page = doc.load_page(page_index)

#         full_text += page.get_text()

#         image_list = page.get_images(full=True)

#         for img_index, img in enumerate(image_list):

#             xref = img[0]
#             base_image = doc.extract_image(xref)

#             image_bytes = base_image["image"]
#             image_ext = base_image["ext"]

#             image_name = f"img_{page_index}_{img_index}.{image_ext}"

#             image_path = os.path.join(image_output, image_name)

#             with open(image_path, "wb") as f:
#                 f.write(image_bytes)

#             # convert windows path to web path
#             web_path = image_path.replace("\\", "/")

#             images.append(web_path)

#     print("Extracted Images:", images)

#     return {
#         "text": full_text,
#         "images": images
#     }


import fitz
import os

def extract_pdf_data(pdf_path, image_output="uploads/images"):

    os.makedirs(image_output, exist_ok=True)

    doc = fitz.open(pdf_path)

    text = ""
    images = []

    for page_index in range(len(doc)):

        page = doc.load_page(page_index)

        text += page.get_text()

        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):

            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"img_{page_index}_{img_index}.{image_ext}"
            image_path = os.path.join(image_output, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            images.append(os.path.abspath(image_path))

    return {
        "text": text,
        "images": images[:10]   # limit images
    }