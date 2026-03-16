
# import json
# from groq import Groq
# from .prompts import DDR_PROMPT

# client = Groq(api_key="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")


# def generate_ddr(inspection_text, thermal_text):

#     prompt = DDR_PROMPT.format(
#         inspection=inspection_text,
#         thermal=thermal_text
#     )

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     text = response.choices[0].message.content

#     try:
#         data = json.loads(text)

#     except Exception:

#         # fallback if AI response is not JSON
#         data = {
#             "property_issue_summary": "Generated summary based on inspection and thermal reports.",
#             "area_observations": [
#                 {
#                     "area": "General",
#                     "observation": text,
#                     "thermal_finding": "Not Available"
#                 }
#             ],
#             "probable_root_cause": "Not Available",
#             "severity_assessment": "Not Available",
#             "recommended_actions": "Further inspection recommended",
#             "additional_notes": "AI response not fully structured",
#             "missing_information": "Not Available"
#         }

#     return data
from groq import Groq
import json
import re

client = Groq(api_key="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")


def generate_ddr(text):

    text = text[:6000]

    prompt = """
Analyze the inspection report and return ONLY valid JSON.

Format exactly like this:

{
 "summary": "short summary",
 "observations":[
  {
   "area":"Area name",
   "description":"issue description",
   "root_cause":"possible root cause",
   "severity":"Low/Medium/High",
   "recommendation":"recommended action"
  }
 ]
}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],

        temperature=0.2
    )

    content = response.choices[0].message.content

    # 🔧 Extract JSON safely
    match = re.search(r'\{.*\}', content, re.DOTALL)

    if match:
        json_text = match.group(0)
        return json.loads(json_text)

    # fallback if AI fails
    return {
        "summary": "Inspection completed but AI response parsing failed.",
        "observations": [
            {
                "area": "General",
                "description": "Inspection report processed successfully.",
                "root_cause": "AI formatting issue",
                "severity": "Low",
                "recommendation": "Review report manually."
            }
        ]
    }