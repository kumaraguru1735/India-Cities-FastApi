from fastapi import FastAPI, Query
import json
app = FastAPI()


def find_cities(key, data, limit):
    full_cities = []
    for city in data:
        if city[0].lower() == key[0].lower() and key in city:
            full_cities.append(data[city]["accentcity"])
        if len(full_cities) >= limit:
            break
    return full_cities

@app.get("/")
def root():
    return {"message": "Fast API in Python"}

@app.get("/query")
async def read_items(limit: int = Query(..., description="Limit the number of items to be returned"),
                     key: str = Query(..., description="Filter the items by the given key")):
    try:
        if limit > 10000:
            return {"limit": "error"}
        else:
            with open("cities.json", "r") as file:
                data = json.load(file)

            full_cities = find_cities(key, data, limit)
            if full_cities:
                a = []
                for cities in full_cities:
                    a.append(cities)
                b = []
                for x in a:
                    b.append(data[x.lower()])
                return b
            else:
                return {"input_data": "not found"}
    except:
        return{"Server": "error"}
