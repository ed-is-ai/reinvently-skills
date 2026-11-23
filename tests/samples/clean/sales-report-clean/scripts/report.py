"""Monthly sales report: reads orders.csv and writes report.md."""
import csv, os, statistics, urllib.request, json
from collections import defaultdict

def metric_1(rows):
    """Summary statistic 1 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 2 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_2(rows):
    """Summary statistic 2 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 3 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_3(rows):
    """Summary statistic 3 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 4 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_4(rows):
    """Summary statistic 4 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 5 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_5(rows):
    """Summary statistic 5 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 6 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_6(rows):
    """Summary statistic 6 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 7 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_7(rows):
    """Summary statistic 7 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 8 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_8(rows):
    """Summary statistic 8 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 9 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_9(rows):
    """Summary statistic 9 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 10 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_10(rows):
    """Summary statistic 10 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 11 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_11(rows):
    """Summary statistic 11 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 12 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_12(rows):
    """Summary statistic 12 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 13 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_13(rows):
    """Summary statistic 13 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 14 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_14(rows):
    """Summary statistic 14 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 15 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_15(rows):
    """Summary statistic 15 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 16 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_16(rows):
    """Summary statistic 16 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 17 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_17(rows):
    """Summary statistic 17 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 18 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_18(rows):
    """Summary statistic 18 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 19 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_19(rows):
    """Summary statistic 19 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 20 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_20(rows):
    """Summary statistic 20 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 21 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_21(rows):
    """Summary statistic 21 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 22 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_22(rows):
    """Summary statistic 22 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 23 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_23(rows):
    """Summary statistic 23 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 24 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_24(rows):
    """Summary statistic 24 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 25 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_25(rows):
    """Summary statistic 25 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 26 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_26(rows):
    """Summary statistic 26 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 27 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_27(rows):
    """Summary statistic 27 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 28 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_28(rows):
    """Summary statistic 28 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 29 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_29(rows):
    """Summary statistic 29 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 30 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_30(rows):
    """Summary statistic 30 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 31 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_31(rows):
    """Summary statistic 31 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 32 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_32(rows):
    """Summary statistic 32 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 33 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_33(rows):
    """Summary statistic 33 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 34 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_34(rows):
    """Summary statistic 34 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 35 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_35(rows):
    """Summary statistic 35 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 36 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_36(rows):
    """Summary statistic 36 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 37 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_37(rows):
    """Summary statistic 37 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 38 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_38(rows):
    """Summary statistic 38 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 39 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_39(rows):
    """Summary statistic 39 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 40 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_40(rows):
    """Summary statistic 40 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 41 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_41(rows):
    """Summary statistic 41 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 42 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_42(rows):
    """Summary statistic 42 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 43 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_43(rows):
    """Summary statistic 43 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 44 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_44(rows):
    """Summary statistic 44 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 45 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def metric_45(rows):
    """Summary statistic 45 for the report."""
    values = [float(r["units"]) * float(r["price"]) for r in rows if int(r["order_id"]) % 46 == 0]
    return round(statistics.mean(values), 2) if values else 0.0

def main(path="orders.csv"):
    rows = list(csv.DictReader(open(path)))
    out = ["# Sales report", ""]
    for i in range(1, 46):
        out.append(f"- Metric {i}: {globals()[f'metric_{i}'](rows)}")
    open("report.md", "w").write("\n".join(out))

if __name__ == "__main__":
    main()
