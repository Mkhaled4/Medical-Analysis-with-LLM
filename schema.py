from pydantic import BaseModel, Field


class ProfileSchema(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    sex: str
    height_cm: float = Field(gt=0)
    weight_kg: float = Field(gt=0)


class BiomarkerSchema(BaseModel):
    name: str
    value: float
    unit: str
    reference_min: float
    reference_max: float
    date: str


class LifestyleSchema(BaseModel):
    sleep_hours: float = Field(ge=0, le=24)
    exercise_days_per_week: int = Field(ge=0, le=7)
    diet_type: str
    stress_level: str


class MedicalHistorySchema(BaseModel):
    conditions: list[str]
    medications: list[str]
    allergies: list[str]


class PatientSchema(BaseModel):
    patient_id: str
    profile: ProfileSchema
    biomarkers: list[BiomarkerSchema]
    lifestyle: LifestyleSchema
    medical_history: MedicalHistorySchema










