
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import Base, engine
from app.routers import items, auth, orders


Base.metadata.create_all(bind=engine)

app:FastAPI = FastAPI(
    title= "Savannah Informatics",
    description="Interview Test",
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
        'http://127.0.0.1:8000'
        'https://savannah-api.azurewebsites.net'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(auth.router)
app.include_router(orders.router)



@app.get("/healthcheck")
def read_root():
    return {"message": f"Health Check {app.version}"}