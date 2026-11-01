import json
from python_development.extract import save_country_date


def test_writes_file_to_expected_path(tmp_path):
    fake_data = {"unix_seconds": [1,2,3,4]}

    result = save_country_date(data= fake_data,country= "de",date= "2026-10-30", base_dir = tmp_path )

    expected_result = tmp_path / "public_power"/ "de" / "2026-10-30.json"

    assert result == expected_result

    assert result.exists()

def test_saved_file_contains_original_data(tmp_path):
    fake_data = {"unix_seconds": [1,2,3,4]}

    result = save_country_date(data= fake_data, country= "de", date= "2026-10-30", base_dir = tmp_path)

    loaded_data = json.loads(result.read_text())

    assert loaded_data == fake_data


















