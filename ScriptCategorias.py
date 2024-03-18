import pandas as pd

categorias = pd.read_csv(r"C:\Users\bossi\Downloads\3 Juegos en steam.csv", usecols=["categorias"])
list_categorias = categorias.categorias.str.split(";")
set_categorias = set(item for lista in list_categorias.values.flatten() for item in lista)
df_categorias = pd.DataFrame(set_categorias, columns=["categorias"])
print(df_categorias)
