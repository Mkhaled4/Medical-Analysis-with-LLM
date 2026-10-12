# BioInsight — AI-Powered Biomarker Analysis

BioInsight is a Python-based prototype that analyzes structured patient biomarker data and uses a Large Language Model (LLM) to generate understandable explanations of laboratory measurements.

The project combines rule-based biomarker classification with generative AI to produce structured, interpretable health information.

> **Disclaimer:** BioInsight is an educational prototype using synthetic patient data. It is not intended for medical diagnosis, treatment, or clinical decision-making.

## Features

- **Patient Data Validation:** Uses Pydantic schemas to validate patient profiles, biomarkers, lifestyle information, and medical history.
- **Biomarker Classification:** Classifies measurements as low, normal, or high based on supplied reference intervals.
- **LLM Integration:** Uses the OpenAI API to generate human-readable explanations of biomarker results.
- **Structured AI Outputs:** Uses Pydantic to enforce a consistent format for generated explanations.
- **JSON Support:** Accepts structured patient data in JSON format.

## Technologies Used

- **Python** — Core application logic
- **Pydantic** — Data validation and structured outputs
- **OpenAI API** — LLM-powered explanations
- **JSON** — Patient data storage and interchange
- **python-dotenv** — Environment variable management

## System Architecture

BioInsight follows a modular processing pipeline:

```text
Patient JSON
    |
    v
Pydantic Validation
    |
    v
Biomarker Classification
    |
    v
Structured Analysis Report
    |
    v
OpenAI API
    |
    v
Structured LLM Explanation
```

### 1. Data Input

The application loads synthetic patient information from JSON files containing:

- Patient profile
- Biomarker measurements
- Lifestyle information
- Medical history

### 2. Data Validation

Nested Pydantic schemas validate the expected structure and data types of each section.

### 3. Biomarker Analysis

Each biomarker is compared against its supplied reference interval and classified as:

- **Low:** Below the reference minimum
- **Normal:** Within the reference interval
- **High:** Above the reference maximum

### 4. LLM Interpretation

The structured analysis report is passed to an OpenAI language model, which generates explanations of the measurements and their reported classifications.

The LLM is instructed not to invent medical findings, change classifications, or provide diagnoses.

## Example Input

```json
{
  "name": "vitamin_d",
  "value": 15.0,
  "unit": "ng/mL",
  "reference_min": 20.0,
  "reference_max": 50.0,
  "date": "2026-10-05"
}
```

This represents one biomarker within a larger patient JSON file.

## Example Output

```json
{
  "name": "vitamin_d",
  "status": "low",
  "explanation": "The measured vitamin D value is below the supplied reference interval. Vitamin D contributes to calcium regulation and bone health."
}
```

The example explanation is illustrative. Actual LLM responses may vary.

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd BioInsight
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project's root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Ensure `.env` is included in `.gitignore` to prevent accidental exposure of API credentials.

### 4. Run the Application

Prepare a synthetic patient JSON file that follows the defined schemas, then run the application's main Python script.

## Limitations

- Biomarker classifications depend on the reference intervals provided in the input data.
- Reference intervals may differ across laboratories, methods, and patient populations.
- LLM-generated explanations may contain inaccuracies.
- Pydantic validates data structures but does not guarantee medical correctness.
- The system is not intended for real patient diagnosis or treatment.

## Future Improvements

- Automated unit testing using Pytest
- LLM evaluation to verify consistency between input data and generated explanations
- Improved handling of missing or inconsistent data
- FastAPI integration for exposing the analysis pipeline through REST endpoints
- Evidence-grounded explanations using validated medical references

## Project Purpose

BioInsight was developed to explore the integration of structured data processing, validation, and Large Language Models in health-related software.

The project emphasizes modular design, separation of deterministic analysis from AI-generated explanations, and the importance of correctness and reliability in health-oriented applications.