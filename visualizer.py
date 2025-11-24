"""
visualizer.py
Creates simple plots using matplotlib if available.
"""
def plot_temperature_timeseries(data, outpath="temperature.png"):
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        print("matplotlib not available. Install it to enable plotting.")
        return
    dates = [r["date"] for r in data]
    temps = [r["temperature_c"] for r in data]
    plt.figure(figsize=(10,4))
    plt.plot(dates, temps)
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.title("Temperature Time Series")
    plt.tight_layout()
    plt.savefig(outpath)
    print(f"Saved plot to {outpath}")
