"""
preprocess.py
Basic cleaning and aggregation utilities.
"""
from collections import defaultdict
from datetime import date

def remove_missing_rows(data):
    return [r for r in data if r.get("date") is not None]

def aggregate_monthly(data):
    """Aggregate data by (year, month) -> compute averages"""
    agg = defaultdict(lambda: {"count":0, "temperature_c":0.0, "humidity_percent":0.0, "wind_kmph":0.0, "precip_mm":0.0})
    for r in data:
        y,m = r["date"].year, r["date"].month
        key = (y,m)
        agg[key]["count"] += 1
        agg[key]["temperature_c"] += r["temperature_c"]
        agg[key]["humidity_percent"] += r["humidity_percent"]
        agg[key]["wind_kmph"] += r["wind_kmph"]
        agg[key]["precip_mm"] += r["precip_mm"]
    # finalize averages
    results = []
    for (y,m), vals in agg.items():
        c = vals["count"]
        results.append({
            "year": y, "month": m,
            "avg_temperature_c": vals["temperature_c"]/c,
            "avg_humidity_percent": vals["humidity_percent"]/c,
            "avg_wind_kmph": vals["wind_kmph"]/c,
            "total_precip_mm": vals["precip_mm"]
        })
    return results
