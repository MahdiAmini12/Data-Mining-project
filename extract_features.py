import pandas as pd

# خواندن داده‌ها
df = pd.read_csv("Final-Dataset.csv", header=None, sep=",", on_bad_lines='skip', low_memory=False)
df.columns = ["time", "src_ip", "dst_ip", "protocol", "length", "tcp_flags", "label"]

# شبیه‌سازی normal
df.loc[:17900, "label"] = "normal"

# تبدیل طول فریم به عددی
df["length"] = pd.to_numeric(df["length"], errors="coerce")
df.dropna(subset=["length"], inplace=True)

# استخراج لیست پروتکل‌ها
protocols = df["protocol"].unique()

# آماده‌سازی دیتا فریم خروجی
rows = []

for protocol in protocols:
    attack_rows = df[(df["protocol"] == protocol) & (df["label"] == "attack")]
    normal_rows = df[(df["protocol"] == protocol) & (df["label"] == "normal")]

    total = len(attack_rows) + len(normal_rows)

    row = {
        "protocol": protocol,
        "attack": len(attack_rows),
        "normal": len(normal_rows),
        "mean_length_attack": attack_rows["length"].mean(),
        "mean_length_normal": normal_rows["length"].mean(),
        "std_length_attack": attack_rows["length"].std(),
        "std_length_normal": normal_rows["length"].std(),
        "max_length_attack": attack_rows["length"].max(),
        "max_length_normal": normal_rows["length"].max(),
        "attack_ratio": len(attack_rows) / total if total > 0 else 0,
        "total_count": total
    }

# for protocol in protocols:
#     attack_rows = df[(df["protocol"] == protocol) & (df["label"] == "attack")]
#     normal_rows = df[(df["protocol"] == protocol) & (df["label"] == "normal")]

#     row = {
#         "protocol": protocol,
#         "attack": len(attack_rows),
#         "normal": len(normal_rows),
#         "mean_length_attack": attack_rows["length"].mean(),
#         "mean_length_normal": normal_rows["length"].mean()
#     }

    rows.append(row)

# ساخت دیتا فریم نهایی
result_df = pd.DataFrame(rows)

# ذخیره در فایل CSV
result_df.to_csv("extracted_features.csv", index=False)

print("✅ فایل ویژگی دقیق ساخته شد: extracted_features.csv")
