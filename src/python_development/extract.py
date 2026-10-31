import requests

BASE_URL= "https://api.energy-charts.info/public_power"
def get_country_date(country: str, date: str) -> dict:
    """ Fetching the energy power data for a specific date in the chosen country"""
    response = requests.get(BASE_URL,params={"country":country, "start": date}, timeout=10)
    response.raise_for_status()
    return response.json()
if __name__ == "__main__":
    data = get_country_date("de", "2026-10-30")
    print(data.keys())



