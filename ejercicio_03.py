from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get ("/zapatillas")
async def obtenerzapatillas ():
    return [
        {"id": 1, "marca": "Nike", "talla": 40-50},
        {"id": 2, "marca": "Addidas", "talla": 30-35},
        {"id": 3, "marca": "Nike", "talla": 35-45}
    ]