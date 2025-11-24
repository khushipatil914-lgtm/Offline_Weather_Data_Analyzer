"""
cli.py
Command-line interface for the Offline Weather Analyzer.
Modes:
- summary: prints summary stats
- visualize: saves a temperature timeseries (requires matplotlib)
- predict: runs the simple predictor (requires sklearn and numpy)
"""
import argparse
from src.data_loader import load_csv
from src.analyzer import summary_statistics, detect_heatwave
from src.visualizer import plot_temperature_timeseries
from src.predictor import predict_temperature

def main():
    parser = argparse.ArgumentParser(description="Offline Weather Analyzer CLI")
    parser.add_argument("--data", required=True, help="Path to CSV data file")
    parser.add_argument("--mode", default="summary", choices=["summary","visualize","predict"], help="Mode of operation")
    parser.add_argument("--out", default="results.txt", help="Output file for summary")
    parser.add_argument("--predict_days", type=int, default=1, help="Days ahead to predict (predict mode)")
    args = parser.parse_args()

    data = load_csv(args.data)
    if args.mode == "summary":
        s = summary_statistics(data)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(str(s))
        print("Summary written to", args.out)
        hw = detect_heatwave(data)
        print("Heatwave detected?" , hw)
    elif args.mode == "visualize":
        plot_temperature_timeseries(data, outpath="temperature.png")
    elif args.mode == "predict":
        try:
            preds = predict_temperature(data, days_ahead=args.predict_days)
            print("Predictions:", preds)
        except Exception as e:
            print("Prediction failed:", e)

if __name__ == "__main__":
    main()
