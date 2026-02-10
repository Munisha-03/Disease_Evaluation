from pydantic import BaseModel, Field
from typing import List

class DiseaseDetails(BaseModel):
    disease_name: str = Field(description="Name of the disease")
    description: str = Field(description="Brief explanation of the disease")
    symptoms: List[str] = Field(description="Common symptoms")
    causes: List[str] = Field(description="Main causes of the disease")
    risk_factors: List[str] = Field(description="Risk factors")
    diagnosis: str = Field(description="How the disease is diagnosed")
    treatment: str = Field(description="Available treatments")
    prevention: str = Field(description="Prevention methods")    


class DiseaseVerify(BaseModel):
    disease: List[str] = Field(description="Name of the disease")

class TextInput(BaseModel):
    disease: str = Field(description="Name of the disease")


class DiseaseResponse(BaseModel):
    disease_details: DiseaseDetails
    # symptoms_and_causes: SymptomsCauses
    # action_plan: Action
