import pandas as pd

plataformas = pd.read_csv(r"C:\Users\bossi\Downloads\3 Juegos en steam.csv", usecols=["plataformas"])
list_plataformas = plataformas.plataformas.str.split(";")
set_plataformas = set(item for lista in list_plataformas.values.flatten() for item in lista)
df_plataformas = pd.DataFrame(set_plataformas, columns=["plataformas"])
print(df_plataformas)
