
    
    
# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import HTMLResponse
# import shutil
# import os

# from app.parsers.pdf_parser import extract_pdf_data
# from app.ai.extractor import generate_ddr
# from app.report.report_generator import generate_report

# app = FastAPI()

# UPLOAD_DIR = "uploads"
# os.makedirs("uploads", exist_ok=True)
# os.makedirs("outputs", exist_ok=True)

# # HOME PAGE
# @app.get("/", response_class=HTMLResponse)
# def home():

#     return """
#     <html>

#     <head>
#         <title>DDR AI Generator</title>

#         <style>

#         body{
#         font-family:Arial;
#         background:#0f172a;
#         color:white;
#         text-align:center;
#         padding:80px;
#         }

#         .box{
#         background:#1e293b;
#         padding:40px;
#         border-radius:10px;
#         width:400px;
#         margin:auto;
#         }

#         input{
#         margin:10px;
#         }

#         button{
#         background:#38bdf8;
#         border:none;
#         padding:12px 25px;
#         color:black;
#         font-weight:bold;
#         border-radius:6px;
#         cursor:pointer;
#         }

#         </style>

#     </head>

#     <body>

#     <div class="box">

#     <h2>AI DDR Report Generator</h2>

#     <form action="/generate-ddr" enctype="multipart/form-data" method="post">

#         <p>Inspection Report</p>
#         <input name="inspection" type="file">

#         <p>Thermal Report</p>
#         <input name="thermal" type="file">

#         <br><br>

#         <button type="submit">Generate DDR</button>

#     </form>

#     </div>

#     </body>
#     </html>
#     """


# @app.post("/generate-ddr")
# async def generate_ddr_report(
# inspection: UploadFile = File(...),
# thermal: UploadFile = File(...)
# ):

#     inspection_path = os.path.join(UPLOAD_DIR, inspection.filename)
#     thermal_path = os.path.join(UPLOAD_DIR, thermal.filename)

#     with open(inspection_path,"wb") as f:
#         shutil.copyfileobj(inspection.file,f)

#     with open(thermal_path,"wb") as f:
#         shutil.copyfileobj(thermal.file,f)

#     inspection_data = extract_pdf_data(inspection_path)
#     thermal_data = extract_pdf_data(thermal_path)

#     report_text = generate_ddr(
#         inspection_data["text"],
#         thermal_data["text"]
#     )

#     report_path = generate_report(
#         report_text,
#         inspection_data["images"] + thermal_data["images"]
#     )

#     return {"report": report_path}



# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import HTMLResponse, FileResponse
# import shutil
# import os

# from app.parsers.pdf_parser import extract_pdf_data
# from app.ai.extractor import generate_ddr
# from app.report.report_generator import generate_report


# from app.utils.validation import detect_conflicts
# from app.utils.validation import detect_missing
# from app.utils.validation import remove_duplicates
# from app.report.report_generator import attach_images

# app = FastAPI()

# UPLOAD_DIR = "uploads"

# os.makedirs("uploads", exist_ok=True)
# os.makedirs("outputs", exist_ok=True)


# # HOME PAGE
# @app.get("/", response_class=HTMLResponse)
# def home():
#     return """
#     <html>
#     <head>
#         <title>AI DDR Generator</title>

#         <style>
#         body{
#             font-family:Arial;
#             background:#0f172a;
#             color:white;
#             text-align:center;
#             padding:60px;
#         }

#         .box{
#             background:#1e293b;
#             padding:40px;
#             border-radius:10px;
#             width:400px;
#             margin:auto;
#         }

#         input{
#             margin:10px;
#         }

#         button{
#             background:#38bdf8;
#             border:none;
#             padding:12px 25px;
#             color:black;
#             font-weight:bold;
#             border-radius:6px;
#             cursor:pointer;
#         }

#         </style>
#     </head>

#     <body>

#     <div class="box">

#         <h2>AI DDR Report Generator</h2>

#         <form action="/generate-ddr" enctype="multipart/form-data" method="post">

#         <p>Upload Inspection Report</p>
#         <input name="inspection" type="file" required>

#         <p>Upload Thermal Report</p>
#         <input name="thermal" type="file" required>

#         <br><br>

#         <button type="submit">Generate DDR</button>

#         </form>

#     </div>

#     </body>
#     </html>
#     """


# # DDR GENERATION
# @app.post("/generate-ddr")
# async def generate_ddr_report(
#     inspection: UploadFile = File(...),
#     thermal: UploadFile = File(...)
# ):

#     inspection_path = os.path.join(UPLOAD_DIR, "inspection.pdf")
#     thermal_path = os.path.join(UPLOAD_DIR, "thermal.pdf")

#     with open(inspection_path, "wb") as f:
#         shutil.copyfileobj(inspection.file, f)

#     with open(thermal_path, "wb") as f:
#         shutil.copyfileobj(thermal.file, f)

#     inspection_data = extract_pdf_data(inspection_path)
#     thermal_data = extract_pdf_data(thermal_path)

#     report_text = generate_ddr(
#         inspection_data["text"],
#         thermal_data["text"]
#     )

#     report_path = generate_report(
#         report_text,
#         inspection_data["images"] + thermal_data["images"]
#     )

#     return FileResponse(
#         report_path,
#         media_type="text/html",
#         filename="DDR_Report.html"
#     )


# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import HTMLResponse, FileResponse
# import shutil
# import os

# from app.parsers.pdf_parser import extract_pdf_data
# from app.ai.extractor import generate_ddr
# from app.report.report_generator import generate_report, attach_images

# from app.utils.validation import detect_conflicts
# from app.utils.validation import detect_missing
# from app.utils.validation import remove_duplicates

# app = FastAPI()

# UPLOAD_DIR = "uploads"

# os.makedirs("uploads", exist_ok=True)
# os.makedirs("outputs", exist_ok=True)


# # HOME PAGE
# @app.get("/", response_class=HTMLResponse)
# def home():
#     return """
#     <html>
#     <head>
#         <title>AI DDR Generator</title>

#         <style>

#         body{
#             font-family:Arial;
#             background-image:url('https://images.unsplash.com/photo-1581093588401-22b6c1e90e9d');
#             background-size:cover;
#             background-position:center;
#             color:white;
#             text-align:center;
#             padding:80px;
#         }

#         .overlay{
#             background:rgba(0,0,0,0.6);
#             padding:60px;
#             border-radius:10px;
#             width:420px;
#             margin:auto;
#         }

#         h2{
#             color:#38bdf8;
#             margin-bottom:20px;
#         }

#         input{
#             margin:10px;
#             padding:8px;
#         }

#         button{
#             background:#38bdf8;
#             border:none;
#             padding:12px 25px;
#             color:black;
#             font-weight:bold;
#             border-radius:6px;
#             cursor:pointer;
#             transition:0.3s;
#         }

#         button:hover{
#             background:#0ea5e9;
#         }

#         </style>

#     </head>

#     <body>

#     <div class="overlay">

#         <h2>AI DDR Report Generator</h2>

#         <form action="/generate-ddr" enctype="multipart/form-data" method="post">

#         <p>Upload Inspection Report</p>
#         <input name="inspection" type="file" required>

#         <p>Upload Thermal Report</p>
#         <input name="thermal" type="file" required>

#         <br><br>

#         <button type="submit">Generate DDR</button>

#         </form>

#     </div>

#     </body>
#     </html>
#     """


# # DDR GENERATION
# @app.post("/generate-ddr")
# async def generate_ddr_report(
#     inspection: UploadFile = File(...),
#     thermal: UploadFile = File(...)
# ):

#     inspection_path = os.path.join(UPLOAD_DIR, "inspection.pdf")
#     thermal_path = os.path.join(UPLOAD_DIR, "thermal.pdf")

#     with open(inspection_path, "wb") as f:
#         shutil.copyfileobj(inspection.file, f)

#     with open(thermal_path, "wb") as f:
#         shutil.copyfileobj(thermal.file, f)

#     # Extract data
#     inspection_data = extract_pdf_data(inspection_path)
#     thermal_data = extract_pdf_data(thermal_path)

#     # AI extraction
#     ai_data = generate_ddr(
#         inspection_data["text"],
#         thermal_data["text"]
#     )

#     # Remove duplicates
#     observations = remove_duplicates(ai_data["area_observations"])

#     # Attach images to observations
#     observations = attach_images(
#         observations,
#         inspection_data["images"] + thermal_data["images"]
#     )

#     # Detect conflicts
#     conflicts = detect_conflicts(
#         inspection_data["text"],
#         thermal_data["text"]
#     )

#     # Detect missing data
#     missing = detect_missing(ai_data)

#     # Generate report
#     report_path = generate_report(
#         ai_data,
#         observations,
#         conflicts,
#         missing
#     )

#     return FileResponse(
#     report_path,
#     media_type="application/pdf",
#     filename="DDR_Report.pdf"
# )



from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
import shutil
import os

from app.parsers.pdf_parser import extract_pdf_data
from app.ai.extractor import generate_ddr
from app.report.report_generator import generate_report

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)


# -----------------------------
# HOME PAGE
# -----------------------------

@app.get("/", response_class=HTMLResponse)
def home():

    return """

    <html>

    <head>

    <title>AI DDR Generator</title>

    <style>

    body{
        font-family:Arial;
        background:#0f172a;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;
        height:100vh;
    }

    .box{
        background:#1e293b;
        padding:40px;
        border-radius:10px;
        text-align:center;
    }

    h1{
        color:#38bdf8;
    }

    a{
        display:inline-block;
        margin-top:20px;
        padding:12px 25px;
        background:#38bdf8;
        color:black;
        text-decoration:none;
        border-radius:6px;
        font-weight:bold;
    }

    </style>

    </head>

    <body>

    <div class="box">

    <h1>AI DDR Report Generator</h1>

    <p>Upload inspection & thermal reports to generate AI diagnostic report.</p>

    <a href="/docs">Open Upload Interface</a>

    </div>

    </body>

    </html>

    """


# -----------------------------
# DDR GENERATION
# -----------------------------

@app.post("/generate-ddr")
async def generate_ddr_report(

    inspection: UploadFile = File(...),
    thermal: UploadFile = File(...)

):

    inspection_path = os.path.join(UPLOAD_DIR, "inspection.pdf")
    thermal_path = os.path.join(UPLOAD_DIR, "thermal.pdf")

    with open(inspection_path, "wb") as f:
        shutil.copyfileobj(inspection.file, f)

    with open(thermal_path, "wb") as f:
        shutil.copyfileobj(thermal.file, f)

    inspection_data = extract_pdf_data(inspection_path)
    thermal_data = extract_pdf_data(thermal_path)

    combined_text = inspection_data["text"] + "\n" + thermal_data["text"]

    ai_data = generate_ddr(combined_text)

    images = inspection_data["images"] + thermal_data["images"]

    pdf_path = generate_report(ai_data, images)

    return FileResponse(

        pdf_path,
        media_type="application/pdf",
        filename="DDR_Report.pdf"

    )