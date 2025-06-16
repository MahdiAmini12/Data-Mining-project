import pandas as pd

# خواندن فایل بدون هدر و تعریف نام ستون‌ها
df = pd.read_csv("new_data.csv", header=None)

# تنظیم نام ستون‌ها به‌صورت دستی
df.columns = ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'Extra']

# نمایش تعداد مقادیر گمشده قبل از پاک‌سازی
print("Missing values before:")
print(df.isnull().sum())

# اصلاح مقادیر گمشده
df['Time'] = df['Time'].ffill().bfill()
df['Source'] = df['Source'].fillna('Unknown_Source')
df['Destination'] = df['Destination'].fillna('Unknown_Dest')
df['Protocol'] = df['Protocol'].fillna(df['Protocol'].mode()[0])

# تبدیل Length به عددی (در صورت وجود داده متنی)
df['Length'] = pd.to_numeric(df['Length'], errors='coerce')
df['Length'] = df['Length'].fillna(df['Length'].median())

# پر کردن Info
df['Info'] = df['Info'].fillna('No_Info')

# حذف ستون Extra
df = df.drop(columns=['Extra'])

# نمایش تعداد مقادیر گمشده بعد از پاک‌سازی
print("\nMissing values after:")
print(df.isnull().sum())

# ذخیره دیتافریم نهایی در فایل CSV جدید
df.to_csv("cleaned_data.csv", index=False)





# import pandas as pd

# # خواندن فایل CSV بدون استفاده از ردیف اول به‌عنوان نام ستون‌ها
# df = pd.read_csv("new_data.csv", header=None)

# # نمایش نمونه‌ای از داده‌ها برای شناخت ساختار
# print("First 5 rows:")
# print(df.head())

# # حالا با توجه به ساختار، فرض می‌گیریم که ستون‌های زیر وجود دارند
# # شما باید بر اساس ساختار واقعی CSV خود این‌ها را تنظیم کنید
# df.columns = ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'Extra']

# # نمایش تعداد مقادیر گمشده قبل از اصلاح
# print("\nMissing values before:")
# print(df.isnull().sum())

# # پر کردن ستون Time با مقدار قبلی و بعدی
# df['Time'] = df['Time'].fillna(method='ffill')
# df['Time'] = df['Time'].fillna(method='bfill')

# # پر کردن Source و Destination با مقدار متنی جایگزین
# df['Source'] = df['Source'].fillna('Unknown_Source')
# df['Destination'] = df['Destination'].fillna('Unknown_Dest')

# # پر کردن Protocol با رایج‌ترین مقدار
# df['Protocol'] = df['Protocol'].fillna(df['Protocol'].mode()[0])

# # پر کردن Length با مقدار میانه
# df['Length'] = pd.to_numeric(df['Length'], errors='coerce')
# df['Length'] = df['Length'].fillna(df['Length'].median())

# # پر کردن Info با مقدار متنی پیش‌فرض
# df['Info'] = df['Info'].fillna('No_Info')

# # حذف ستون اضافی در صورت نیاز (مثلاً Extra)
# df = df.drop(columns=['Extra'])

# # نمایش مقادیر گمشده بعد از اصلاح
# print("\nMissing values after:")
# print(df.isnull().sum())

# # ذخیره دیتافریم پاک‌سازی‌شده در فایل جدید
# df.to_csv("cleaned_data.csv", index=False)





# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.cluster import KMeans

# # بارگذاری داده‌ها با تعیین نام ستون‌ها
# columns = ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info']
# df = pd.read_csv('new_data.csv', names=columns)

# # بررسی مقدارهای غیرموجود
# print("Missing values:\n", df.isnull().sum())

# # فقط ستون پروتکل را برای کلاسترینگ استفاده می‌کنیم
# df = df.dropna(subset=['Protocol'])

# # کدگذاری پروتکل‌ها به عدد
# le = LabelEncoder()
# df['Protocol_encoded'] = le.fit_transform(df['Protocol'])

# # اجرای KMeans با 3 کلاستر (می‌تونی تعداد رو تغییر بدی)
# kmeans = KMeans(n_clusters=3, random_state=0)
# df['Cluster'] = kmeans.fit_predict(df[['Protocol_encoded']])

# # نمایش نتایج
# print(df[['Protocol', 'Protocol_encoded', 'Cluster']])

# # ذخیره فایل خروجی
# df.to_csv("clustered_output.csv", index=False)
