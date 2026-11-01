import requests
import json
from pathlib import Path

BASE_URL= "https://api.energy-charts.info/public_power"

def get_country_date(country: str, date: str) -> dict:
    """ Fetching the energy power data for a specific date in the chosen country"""
    
    response = requests.get(
        BASE_URL,params={"country":country, "start": date}, timeout=10
        )
    response.raise_for_status()
    return response.json()

def save_country_date(data: dict, country: str, date: str, base_dir: Path = Path("data/raw")) -> Path:
    """ Saves the energy data JSON to a structured path: data/raw/public_power/<country>/<date>.json"""
    dir_path = base_dir/f"public_power/{country}"
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path/f"{date}.json"

    with open(file_path, "w", encoding="utf-8") as f :
        json.dump(data, f, indent=4)

    return file_path 

if __name__ == "__main__":
    country_code = "de"
    target_date = "2026-10-30"

    data = get_country_date(country_code, target_date)
    saved_path = save_country_date(data, country_code, target_date)
    print(f"Saved to {saved_path}")




