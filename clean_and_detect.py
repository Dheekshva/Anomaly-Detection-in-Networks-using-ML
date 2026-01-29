import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('features.csv')

df.dropna(inplace=True)

df['length'] = pd.to_numeric(df['length'], errors='coerce')

df_encoded = pd.get_dummies(df[['protocol', 'info']])
df_final = pd.concat([df[['length']], df_encoded], axis=1)

model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(df_final)

df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)

print(f"Detected {df['anomaly'].sum()} anomalies out of {len(df)} packets.")

df.to_csv('labeled_traffic.csv', index=False)

plt.figure(figsize=(10,5))
sns.scatterplot(x=range(len(df)), y='length', hue='anomaly', data=df, palette={0: "blue", 1: "red"})
plt.title("Packet Lengths - Red = Anomalies")
plt.show()
