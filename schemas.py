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

class Language(BaseModel):
    name: str
    Level: int
    
class Certificate(BaseModel):
    date: int
    desc: str
    url: str
    
class Portfolio:
    areas_of_expertise: Set[AreaOfCompetence]
    education: Set[Education]
    professional_experiences: Set[ProfessionalExperience]
    languages: Set[Education]
    volunteering: Set[Volunteering] = None
    certificates: Set[Certificate] = None

