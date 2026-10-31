import requests

def get_country_date(country, date):
    """ Fetching the energy power data for a specific date in the chosen country"""
    response = requests.get(f"https://api.energy-charts.info/public_power",params={"country":country, "start": date}, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = get_country_date("de", "2026-10-30")
    print(data.keys())



    



