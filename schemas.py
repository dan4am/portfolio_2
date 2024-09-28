from typing import Optional, List, Set
from pydantic import BaseModel, Field

class ProfessionalExperience(BaseModel):
    role: str
    company: str
    tasks: str
    technical_stack: str
    salary: int

class Volunteering(BaseModel):
    role: str
    association: str
    tasks: str
    accomplishments: str

class Class(BaseModel):
    name: str
    desc: str
class Education(BaseModel):
    degree: str
    school: str
    classes: List[Class]
    results: str

class Competence(BaseModel):
    name: str
    level: int

class AreaOfCompetence(BaseModel):
    name: str
    compentences:List[Competence]

class Portfolio:
    area_of_compentences: Set[AreaOfCompetence]
    education: Set[Education]
    professional_experiences: Set[ProfessionalExperience]
    volunteering: Set[Volunteering]
