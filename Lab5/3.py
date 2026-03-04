import pandas as pd
df = pd.read_csv("C:\\git\\itcsi250\\Lab5\\student_data.csv")


df['grade_letter'] = pd.cut(df['Оноо'], bins=[0, 60, 70, 80, 90, 100], labels=['F', 'D', 'C', 'B', 'A'])
print(df[['Оноо', 'grade_letter']].head())