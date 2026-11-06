from fastapi import FastAPI
import httpx, csv, io

app = FastAPI()
URL = "https://raw.githubusercontent.com/csmith651/video-games/refs/heads/main/games.csv"

@app.get("/data")
async def get_data():
    async with httpx.AsyncClient() as client:
        r = await client.get(URL)
        r.raise_for_status()
        csv_text = r.text  # Fixed: extracted the text from the response

    reader = csv.DictReader(io.StringIO(csv_text))
    rows = list(reader)
    return {"count": len(rows), "data": rows}