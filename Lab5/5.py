import pandas as pd
df = pd.read_csv("C:\\git\\itcsi250\\Lab5\\student_data.csv")


df['Оноо_normalized'] = (df['Оноо'] - df['Оноо'].min()) / (df['Оноо'].max() - df['Оноо'].min())

print(df[['Оноо', 'Оноо_normalized']].head())