# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, confusion_matrix

# # 1. Load data
# df = pd.read_csv("ml_ready_dataset.csv")

# # 2. Encode protocol
# le = LabelEncoder()
# df['protocol_encoded'] = le.fit_transform(df['protocol'])

# # 3. Features and label
# features = ['protocol_encoded', 'mean_length', 'std_length', 'max_length', 'attack_ratio', 'total_count']
# X = df[features]
# y = df['label']

# # 4. Scale features (اختیاری ولی مفید برای بعضی مدل‌ها)
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 5. Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # 6. Train model
# model = RandomForestClassifier(n_estimators=200, random_state=42, max_depth=10)
# model.fit(X_train, y_train)

# # 7. Evaluation
# y_pred = model.predict(X_test)
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))

# # Optional: show encoded protocol mapping
# print("\n🔠 Protocol Mapping:")
# for proto, code in zip(le.classes_, le.transform(le.classes_)):
#     print(f"{proto} → {code}")





import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import RandomOverSampler

# 1. Load data
df = pd.read_csv("ml_ready_dataset.csv")

# 2. Encode protocol
le = LabelEncoder()
df['protocol_encoded'] = le.fit_transform(df['protocol'])

# 3. Features and label
X = df[['protocol_encoded', 'mean_length']]
y = df['label']

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Oversampling
ros = RandomOverSampler(random_state=42)
X_train, y_train = ros.fit_resample(X_train, y_train)

# 6. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Evaluation
y_pred = model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. Protocol encoding map
print("\n🔠 Protocol Mapping:")
for proto, code in zip(le.classes_, le.transform(le.classes_)):
    print(f"{proto} → {code}")



#1
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, confusion_matrix

# # 1. Load data
# df = pd.read_csv("ml_ready_dataset.csv")

# # 2. Encode protocol
# le = LabelEncoder()
# df['protocol_encoded'] = le.fit_transform(df['protocol'])

# # 3. Features and label
# X = df[['protocol_encoded', 'mean_length']]
# y = df['label']

# # 4. Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 5. Train model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # 6. Evaluation
# y_pred = model.predict(X_test)
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))

# # Optional: show encoded protocol mapping
# print("\n🔠 Protocol Mapping:")
# for proto, code in zip(le.classes_, le.transform(le.classes_)):
#     print(f"{proto} → {code}")
