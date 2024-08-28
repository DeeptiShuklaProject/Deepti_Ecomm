# from fastapi import FastAPI
# from api.endpoints import router

# app = FastAPI()

# # Include the API router
# app.include_router(router)



# from fastapi import FastAPI
# from api.endpoints import router as api_router

# app = FastAPI()

# app.include_router(api_router)

from fastapi import FastAPI
from api.endpoints import router as api_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

app.include_router(api_router)



