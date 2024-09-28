from fastapi import FastAPI
from .routers import area_of_expertise, certificates, education, languages, professional_experiences, volunteering

app = FastAPI(title="Dan's Portfolio",
              description="An API to Access my portfolio",
              # terms_of_service="http://www.google.com",
              contact={"developper name": "Dan Freeman MAHORO",
                       "email": "danfreemanmahoro@gmail.com",
                       "website": "http://www.github.com/dan4am"
                       },
              # docs_url="/documentation"
              )

app.include_router(router=area_of_expertise.router)
app.include_router(router=education.router)
app.include_router(router=certificates.router)
app.include_router(router=languages.router)
app.include_router(router=professional_experiences.router)
app.include_router(router=volunteering.router)
