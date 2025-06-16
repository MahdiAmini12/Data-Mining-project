import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# مسیر فایل CSV (مسیر خودت رو بزار)
file_path = 'new_data.csv'

# نام‌گذاری ستون‌ها
column_names = ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'Extra']
df = pd.read_csv(file_path, header=None, names=column_names)

print("📊 تعداد کل ردیف‌ها:", len(df))

# حذف ردیف‌هایی که Source یا Destination ندارند (مثل ARP)
df = df.dropna(subset=['Source', 'Destination'])

# تبدیل Time و Length به عدد
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
df['Length'] = pd.to_numeric(df['Length'], errors='coerce')

# حذف ردیف‌هایی که Time یا Length خالی‌اند
df = df.dropna(subset=['Time', 'Length'])

print("✅ تعداد ردیف‌های قابل استفاده پس از پاکسازی:", len(df))

# انتخاب ویژگی‌ها برای خوشه‌بندی
X = df[['Time', 'Length']]

# اجرای الگوریتم KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# رسم نمودار
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue']
for cluster in range(3):
    clustered = df[df['Cluster'] == cluster]
    plt.scatter(clustered['Time'], clustered['Length'], 
                color=colors[cluster], label=f'Cluster {cluster}', alpha=0.6)

plt.title('KMeans Clustering of Network Traffic')
plt.xlabel('Time (seconds)')
plt.ylabel('Packet Length')
plt.legend()
plt.grid(True)
plt.show()
