from fastapi import FastAPI

app = FastAPI(title="DevOps Task Manager")


@app.get("/health")
def health_check():
    return {"status": "healthy"}