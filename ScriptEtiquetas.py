import pandas as pd

steamspy_tags = pd.read_csv(r"C:\Users\bossi\Downloads\3 Juegos en steam.csv", usecols=["steamspy_tags"])
list_steamspy_tags = steamspy_tags.steamspy_tags.str.split(";")
set_steamspy_tags = set(item for lista in list_steamspy_tags.values.flatten() for item in lista)
df_steamspy_tags = pd.DataFrame(set_steamspy_tags, columns=["steamspy_tags"])
print(df_steamspy_tags)
