from fastapi import FastAPI

app = FastAPI(title="Student CI/CD Demo")


@app.get("/")
def home():
    return {
        "message": "Hello FastAPI Iam The Krishhh!",
        "version": "v1"
    }


@app.get("/students")
def students():
    return {
        "students": [
            "D Boss Darshan",
            "Rocking Star Yash",
            "Kiccha Suddep",
            "Power Star Punith",
            "Rebel Star Ambresh",
            "Rishab Shetty"
        ]
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }