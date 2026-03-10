import pandas as pd

df = pd.read_csv("C:\\git\\itcsi250\\Lab5\\student_data.csv")

df['Оноо'].mean()
df['above_average'] = df['Оноо'] > df['Оноо'].mean()
print(df['above_average'].value_counts())

