import json
from schema import PatientSchema
from llm_response_gen import explain_biomarkers

def classify_biomarker(biomarker):
    if biomarker.value < biomarker.reference_min:
        return "low"

    elif biomarker.value > biomarker.reference_max:
        return "high"

    else:
        return "normal"


def clean_data(data):
    if data.isna().any().any():
        print("Missing Data Values")
    data = data.drop_duplicates
    validated_data = PatientSchema.model_validate(data)
    return validated_data


def import_data():
    with open("patient.json", "r") as file:
        data = json.load(file)

    patient = clean_data(data)

    results = []
    for biomarker in patient.biomarkers:
        biomarker_analysis = {
            "name": biomarker.name,
            "value": biomarker.value,
            "unit": biomarker.unit,
            "status": classify_biomarker(biomarker),
            "reference_min": biomarker.reference_min,
            "reference_max": biomarker.reference_max
        }
        explanation = explain_biomarkers(biomarker_analysis)
        results.append((biomarker_analysis,explanation))

    print(results)

    print(results)


if __name__ == '__main__':
    import_data()

