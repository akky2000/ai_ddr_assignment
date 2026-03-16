# DDR_PROMPT = """

# You are an expert building diagnostic reports.

# Based on the inspection and thermal report data below,
# generate a structured DDR report.

# Rules:
# - Do NOT invent facts
# - If information missing write "Not Available"
# - Use simple client friendly language

# Structure:

# 1 Property Issue Summary

# 2 Area-wise Observations

# 3 Probable Root Cause

# 4 Severity Assessment (with reasoning)

# 5 Recommended Actions

# 6 Additional Notes

# 7 Missing or Unclear Information

# Inspection Report:
# {inspection}

# Thermal Report:
# {thermal}

# """




DDR_PROMPT = """

You are an AI system that converts inspection data into a structured diagnostic report.
Return ONLY valid JSON. Do not include explanations.

Format:

{{
 "property_issue_summary": "",
 "area_observations": [
   {{
     "area": "",
     "observation": "",
     "thermal_finding": "",
     "image_required": true
   }}
 ],
 "probable_root_cause": "",
 "severity_assessment": "",
 "recommended_actions": "",
 "additional_notes": "",
 "missing_information": ""
}}

Inspection Report:
{inspection}

Thermal Report:
{thermal}

"""