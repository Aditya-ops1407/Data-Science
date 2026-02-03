import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print(df.head())
print(df.info)

print(df[["math","science","english"]].mean())

df["total"] = df["math"] + df["science"] + df["english"]
print(df.loc[df["total"].idxmax()])

print(df[df["science"]>85])

df.describe()
df.sort_values(by="math", ascending = False)
df[df["science"]>85]