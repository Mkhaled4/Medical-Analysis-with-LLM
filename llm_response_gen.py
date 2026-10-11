import json
from openai import OpenAI
from dotenv import load_dotenv
from test_api_key import system_check

load_dotenv()

client = OpenAI()


def explain_biomarkers(report):

    system_check()

    response = client.responses.create(
        model="gpt-5-mini",
        instructions="""
        You are BioInsight, an AI assistant that explains
        synthetic patient biomarker reports.

        Your responsibilities:
        1. Explain each biomarker's reported status.
        2. Compare the value against its supplied reference range.
        3. Explain what the biomarker generally measures.
        4. Highlight measurements outside their reference ranges.
        5. Use clear, understandable language.

        Rules:
        - Never invent patient information or laboratory results.
        - Never change the supplied biomarker classifications.
        - Do not diagnose diseases or prescribe treatments.
        - Do not assume that an abnormal value means a disease.
        - State when information is insufficient.
        - Explain that laboratory reference ranges can vary.
        """,
        input=json.dumps(report),
        max_output_tokens=1000
    )

    return response.output_text