import pandas as pd

df = pd.read_csv('1000-russian-words-raw.txt', delimiter=' ')
df.drop(df.columns[1], axis=1, inplace=True)
df.to_csv("1000-russian-words-cleaned.csv", index=False, encoding="UTF-8")
# NEED TO CREATE LANGUAGE NAME HEADINGS FOR CSV