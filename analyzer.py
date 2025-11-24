"""
analyzer.py
Compute summary statistics and simple trend checks.
"""
from statistics import mean

def summary_statistics(data):
    temps = [r["temperature_c"] for r in data]
    hums = [r["humidity_percent"] for r in data]
    winds = [r["wind_kmph"] for r in data]
    precs = [r["precip_mm"] for r in data]
    return {
        "count": len(data),
        "temp_mean": mean(temps) if temps else None,
        "temp_min": min(temps) if temps else None,
        "temp_max": max(temps) if temps else None,
        "humidity_mean": mean(hums) if hums else None,
        "wind_mean": mean(winds) if winds else None,
        "total_precip": sum(precs) if precs else None
    }

def detect_heatwave(data, threshold=35.0, window=3):
    """Return True if there exists 'window' consecutive days above threshold temperature."""
    consecutive = 0
    for r in data:
        if r["temperature_c"] >= threshold:
            consecutive += 1
            if consecutive >= window:
                return True
        else:
            consecutive = 0
    return False
