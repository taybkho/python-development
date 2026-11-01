import json
import pytest
import requests
from python_development import extract


#save tests
def test_writes_file_to_expected_path(tmp_path):
    fake_data = {"unix_seconds": [1,2,3,4]}

    result = extract.save_country_date(data= fake_data,country= "de",date= "2026-10-30", base_dir = tmp_path )

    expected_result = tmp_path / "public_power"/ "de" / "2026-10-30.json"

    assert result == expected_result

    assert result.exists()

def test_saved_file_contains_original_data(tmp_path):
    fake_data = {"unix_seconds": [1,2,3,4]}

    result = extract.save_country_date(data= fake_data, country= "de", date= "2026-10-30", base_dir = tmp_path)

    loaded_data = json.loads(result.read_text())

    assert loaded_data == fake_data

#fetch tests 
class FakeResponse:
    def __init__(self, payload: dict, status_code: int = 200) -> None:
        self.payload = payload
        self.status_code = status_code
    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} error")
    def json(self) -> dict:
        return self.payload

def test_fetch_returns_api_json(monkeypatch):
    fake_payload = {"unix_seconds": [2, 4, 6],
                    "production_types": [],
                    "deprecated": False
                    }
    def fake_get(url, params, timeout):
        return FakeResponse(fake_payload)

    monkeypatch.setattr(extract.requests, "get", fake_get)

    result = extract.get_country_date("de", "2026-10-30")

    assert result == fake_payload

def test_fetch_raises_on_server_error(monkeypatch):
    def fake_get(url, params, timeout):
        return FakeResponse({}, status_code = 500)
    monkeypatch.setattr(extract.requests, "get", fake_get)
    with pytest.raises(requests.HTTPError):
        extract.get_country_date("de", "2026-10-30")

    





    

    
    

    






        



















