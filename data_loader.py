"""
data_loader.py
Simple CSV loader without external dependencies. If pandas is available, the code will use it for convenience.
""" 
import csv
from datetime import datetime

def load_csv(filepath):
    """Load CSV into list of dicts. Expects columns: date, temperature_c, humidity_percent, wind_kmph, precip_mm"""
    data = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # parse fields with safe conversions
            try:
                row_parsed = {
                    "date": datetime.strptime(row["date"].strip(), "%Y-%m-%d").date(),
                    "temperature_c": float(row.get("temperature_c", "") or 0.0),
                    "humidity_percent": float(row.get("humidity_percent", "") or 0.0),
                    "wind_kmph": float(row.get("wind_kmph", "") or 0.0),
                    "precip_mm": float(row.get("precip_mm", "") or 0.0)
                }
                data.append(row_parsed)
            except Exception as e:
                # skip malformed rows but continue processing
                print(f"Skipping row due to parse error: {e}")
                continue
    return data

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        rows = load_csv(sys.argv[1])
        print(f"Loaded {len(rows)} rows.")
