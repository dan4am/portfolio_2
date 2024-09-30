from fastapi import APIRouter
from .. import schemas

router = APIRouter()


@router.post('/areaofexpertise')
def add_area(request:schemas.AreaOfCompetence):
    return request