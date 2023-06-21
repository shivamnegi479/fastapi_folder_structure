from fastapi import FastAPI
from router.router import users

app = FastAPI()

app.include_router(users)

    


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
