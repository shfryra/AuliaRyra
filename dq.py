import pandas as pd

# load dataset
dataset = 'https://storage.googleapis.com/dqlab-dataset/SuperStore.csv'
df = pd.read_csv(dataset)

# Pisahkan Customer Name menjadi dua komponen yaitu First_Name dan Last_Name
name = []
df['First_Name'] = []
df['Last_Name'] = []
# tampilkan 5 baris pertama
print(df.head())