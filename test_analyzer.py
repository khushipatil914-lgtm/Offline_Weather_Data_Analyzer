"""
Basic test for analyzer.summary_statistics
Run: python -m pytest tests/test_analyzer.py
"""
from src.analyzer import summary_statistics

def test_summary_basic():
    sample = [
        {"temperature_c": 10.0, "humidity_percent": 50.0, "wind_kmph": 5.0, "precip_mm": 0.0},
        {"temperature_c": 20.0, "humidity_percent": 60.0, "wind_kmph": 3.0, "precip_mm": 1.0},
    ]
    res = summary_statistics(sample)
    assert res["count"] == 2
    assert abs(res["temp_mean"] - 15.0) < 1e-6
