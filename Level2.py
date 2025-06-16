import pandas as pd

# فایل خروجی مرحله اول
df = pd.read_csv("extracted_features.csv")

# لیست نهایی از نمونه‌ها
rows = []

for _, row in df.iterrows():
    protocol = row['protocol']

    if pd.notnull(row['mean_length_attack']):
        rows.append({
            'protocol': protocol,
            'mean_length': row['mean_length_attack'],
            'std_length': row['std_length_attack'],
            'max_length': row['max_length_attack'],
            'attack_ratio': row['attack_ratio'],
            'total_count': row['total_count'],
            'label': 1
        })

    if pd.notnull(row['mean_length_normal']):
        rows.append({
            'protocol': protocol,
            'mean_length': row['mean_length_normal'],
            'std_length': row['std_length_normal'],
            'max_length': row['max_length_normal'],
            'attack_ratio': 0,  # برای normal مقدار attack_ratio رو صفر در نظر می‌گیریم
            'total_count': row['total_count'],
            'label': 0
        })

# تبدیل به دیتافریم نهایی
final_df = pd.DataFrame(rows)

# ذخیره فایل آماده‌ی یادگیری ماشین
final_df.to_csv("ml_ready_dataset.csv", index=False)

print("✅ فایل ml_ready_dataset.csv ساخته شد. تعداد نمونه‌ها:", len(final_df))


# import pandas as pd

# # فایل خروجی مرحله اول
# df = pd.read_csv("extracted_features.csv")

# # لیست نهایی از نمونه‌ها
# rows = []

# for _, row in df.iterrows():
#     protocol = row['protocol']
    
#     # اگر مقدار attack وجود دارد
#     if pd.notnull(row['mean_length_attack']):
#         rows.append({
#             'protocol': protocol,
#             'mean_length': row['mean_length_attack'],
#             'label': 1  # attack
#         })
    
#     # اگر مقدار normal وجود دارد
#     if pd.notnull(row['mean_length_normal']):
#         rows.append({
#             'protocol': protocol,
#             'mean_length': row['mean_length_normal'],
#             'label': 0  # normal
#         })

# # تبدیل به دیتافریم نهایی
# final_df = pd.DataFrame(rows)

# # ذخیره فایل آماده‌ی یادگیری ماشین
# final_df.to_csv("ml_ready_dataset.csv", index=False)

# print("✅ فایل ml_ready_dataset.csv ساخته شد. تعداد نمونه‌ها:", len(final_df))
