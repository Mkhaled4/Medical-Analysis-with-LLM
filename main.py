import json
import pandas as pd
from schema import PatientSchema


def import_data():
    with open("patient.json", "r") as file:
        data = json.load(file)

    Patient = clean_data(data)


def clean_data(data):
    if data.isna().any().any():
        print("Missing Data Values")
    data = data.drop_duplicates
    validated_data = PatientSchema.model_validate(data)
    return validated_data

if __name__ == '__main__':
    import_data()

