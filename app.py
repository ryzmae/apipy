from fastapi import FastAPI

app = FastAPI(
    title="MerlBot API",
    description="MerlBot API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    version="0.0.1"
)

@app.get("/")
def root():
    return {"message": "Hello World"}
