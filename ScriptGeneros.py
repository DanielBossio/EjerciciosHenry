import pandas as pd

generos = pd.read_csv(r"C:\Users\bossi\Downloads\3 Juegos en steam.csv", usecols=["generos"])
list_generos = generos.generos.str.split(";")
set_generos = set(item for lista in list_generos.values.flatten() for item in lista)
df_generos = pd.DataFrame(set_generos, columns=["generos"])
print(df_generos)
