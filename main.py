from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import Optional
import requests
import uvicorn
import os

load_dotenv()

app = FastAPI()

bridge_ip = os.getenv("BRIDGE_IP")
application_key = os.getenv("HUE_APP_KEY")

if not bridge_ip or not application_key:
    raise RuntimeError("Fehlende Umgebungsvariablen: Bitte überprüfe .env Datei (BRIDGE_IP, HUE_APP_KEY)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class XYColor(BaseModel):
    x: float
    y: float


class Dimming(BaseModel):
    brightness: float


class Color(BaseModel):
    xy: XYColor


class ColorTemperature(BaseModel):
    mirek: int


class LightState(BaseModel):
    dimming: Optional[Dimming] = None
    color: Optional[Color] = None
    color_temperature: Optional[ColorTemperature] = None


@app.get("/devices")
def get_devices():
    try:
        res = requests.get(
            f"https://{bridge_ip}/clip/v2/resource/device",
            headers={"hue-application-key": application_key},
            verify=False
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}


@app.post("/lights/status")
async def get_light_states(rids: list[str]):
    try:
        res = requests.get(
            f"https://{bridge_ip}/clip/v2/resource/light",
            headers={"hue-application-key": application_key},
            verify=False
        )
        lights = res.json().get("data", [])

        output = []
        for light in lights:
            if light["id"] in rids:
                output.append({
                    "rid": light["id"],
                    "on": light["on"]["on"],
                    "brightness": light.get("dimming", {}).get("brightness", None),
                    "color_xy": light.get("color", {}).get("xy", None)
                })

        return output
    except Exception as e:
        return {"error": str(e)}


@app.get("/lights/{rid}")
def get_light_details(rid: str):
    try:
        res = requests.get(
            f"https://{bridge_ip}/clip/v2/resource/light/{rid}",
            headers={"hue-application-key": application_key},
            verify=False
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}


@app.put("/lights/{light_id}")
async def update_light(light_id: str, state: LightState):
    payload = state.dict(exclude_unset=True)
    print(f"Aktualisiere Lampe {light_id} mit:", payload)

    res = requests.put(
        f"https://{bridge_ip}/clip/v2/resource/light/{light_id}",
        headers={"hue-application-key": application_key},
        json=payload,
        verify=False
    )

    return {"message": f"Lampe {light_id} aktualisiert", "bridge_response": res.json()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
