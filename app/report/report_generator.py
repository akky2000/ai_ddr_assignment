# from jinja2 import Environment, FileSystemLoader
# import os

# def generate_report(report_text, images):

#     env = Environment(loader=FileSystemLoader("app/report"))

#     template = env.get_template("template.html")

#     html = template.render(
#         report_content=report_text.replace("\n","<br>"),
#         images=images
#     )

#     output_path = "outputs/ddr_report.html"

#     with open(output_path,"w",encoding="utf-8") as f:
#         f.write(html)

# #     # return output_path
# from jinja2 import Environment, FileSystemLoader
# import os

# def attach_images(observations, images):

#     for i, obs in enumerate(observations):

#         if i < len(images):
#             obs["image"] = images[i]
#         else:
#             obs["image"] = "Image Not Available"

#     return observations

# def generate_report(report_text, images):

#     env = Environment(loader=FileSystemLoader("app/report"))

#     template = env.get_template("template.html")

#     images = [os.path.abspath(img) for img in images]

#     html = template.render(
#         report_content=report_text.replace("\n","<br>"),
#         images=images
#     )

#     output_path = "outputs/ddr_report.html"

#     with open(output_path,"w",encoding="utf-8") as f:
#         f.write(html)

#     return output_path


# from jinja2 import Environment, FileSystemLoader
# import os


# def attach_images(observations, images):

#     for i, obs in enumerate(observations):

#         if i < len(images):
#             obs["image"] = images[i]
#         else:
#             obs["image"] = "Image Not Available"

#     return observations


# def generate_report(data, observations, conflicts, missing):

#     env = Environment(loader=FileSystemLoader("app/report"))

#     template = env.get_template("template.html")

#     html = template.render(
#         data=data,
#         observations=observations,
#         conflicts=conflicts,
#         missing=missing
#     )

#     output_path = "outputs/ddr_report.html"

#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(html)

#     return output_path


# import pdfkit
# from jinja2 import Environment, FileSystemLoader
# import os

# def attach_images(observations, images):

#     img_index = 0

#     for obs in observations:

#         obs["images"] = []

#         for _ in range(2):

#             if img_index < len(images):

#                 abs_path = os.path.abspath(images[img_index])
#                 obs["images"].append(abs_path)

#                 img_index += 1

#     return observations


# def generate_report(data, observations, conflicts, missing):

#     env = Environment(loader=FileSystemLoader("app/report"))
#     template = env.get_template("template.html")

#     html_content = template.render(
#         data=data,
#         observations=observations,
#         conflicts=conflicts,
#         missing=missing
#     )

#     os.makedirs("outputs", exist_ok=True)

#     html_path = "outputs/ddr_report.html"
#     pdf_path = "outputs/ddr_report.pdf"

#     with open(html_path, "w", encoding="utf-8") as f:
#         f.write(html_content)

#     config = pdfkit.configuration(
#         wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
#     )

#     options = {
#         "enable-local-file-access": None
#     }

#     pdfkit.from_file(
#         html_path,
#         pdf_path,
#         configuration=config,
#         options=options
#     )

#     return pdf_path

import os
import pdfkit


def generate_report(ai_data, images):

    os.makedirs("outputs", exist_ok=True)

    html_file = "outputs/ddr_report.html"
    pdf_file = "outputs/ddr_report.pdf"

    summary = ai_data.get("summary", "Not Available")
    observations = ai_data.get("observations", [])

    html_content = f"""
    <html>

    <head>

    <style>

    body {{
        font-family: Arial;
        background:#0f172a;
        color:white;
        padding:40px;
    }}

    .container {{
        max-width:900px;
        margin:auto;
        background:#1e293b;
        padding:40px;
        border-radius:10px;
    }}

    h1 {{
        color:#38bdf8;
        text-align:center;
    }}

    h2 {{
        color:#fbbf24;
        margin-top:30px;
    }}

    .obs {{
        background:#020617;
        padding:20px;
        border-radius:8px;
        margin-top:20px;
    }}

    img {{
        width:100%;
        margin-top:10px;
        border-radius:6px;
    }}

    </style>

    </head>

    <body>

    <div class="container">

    <h1>Detailed Diagnostic Report</h1>

    <h2>Property Issue Summary</h2>
    <p>{summary}</p>

    <h2>Area-wise Observations</h2>
    """

    for i, obs in enumerate(observations):

        area = obs.get("area", "Unknown")
        desc = obs.get("description", "Not Available")
        root = obs.get("root_cause", "Not Available")
        severity = obs.get("severity", "Not Available")
        action = obs.get("recommendation", "Not Available")

        html_content += f"""
        <div class="obs">

        <h3>{area}</h3>

        <p><b>Observation:</b> {desc}</p>
        <p><b>Probable Root Cause:</b> {root}</p>
        <p><b>Severity:</b> {severity}</p>
        <p><b>Recommended Action:</b> {action}</p>
        """

        if i < len(images):
            img_path = images[i]
            abs_path = os.path.abspath(img_path)
            html_content += f'<img src="file:///{abs_path}">'

        html_content += "</div>"

    html_content += """

    <h2>Additional Notes</h2>
    <p>Report generated automatically using AI analysis.</p>

    <h2>Missing Information</h2>
    <p>If any inspection data was unclear, it has been marked as Not Available.</p>

    </div>

    </body>

    </html>
    """

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    )

    options = {
    "enable-local-file-access": ""
}

    pdfkit.from_file(
    html_file,
    pdf_file,
    configuration=config,
    options=options
)

    return pdf_file