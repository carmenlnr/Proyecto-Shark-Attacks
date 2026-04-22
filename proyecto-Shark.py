import pandas as pd

df = pd.read_excel("GSAF5.xls", engine= "xlrd")

df.to_pickle("data.pkl")

print(df.head())

print ("Dimensiones:", df.shape)
print ("Filas:", df.shape[0])
print("Columns:", df.shape[1])

print(df.dtypes)
print(df.nunique()) #num de valores unicos
print(df["Type"].unique()) #para ver valores exactos de una columna


df = pd.read_pickle("data.pkl") # ya se puede usar para futuros scripts sin necesidad de releer excel


# ERIKA LIMPIEZA DATOS
# 1 elimino columnas
# DE NOMBRES IGUALES PERO ESCRITOS DE DIFERETNES MANERA UNIFICARLOS, ESTANDARIZAR
#Paso 1: Erika: Eliminación de las colummnas no deseadas.
df = pd.read_pickle("data.pkl")
df= pd.read_pickle("data.pkl")
df= df[['Country','Activity','Age','Sex']]
print(df.head())
print(df.shape)
df.to_pickle("data.pkl")

## CARMEN LIMPIEZA DATOS
# 2 Carmen maneja valores nulos
print(df.isna().sum()) # nos dice cuantos nan hay 
print((df == "?").sum()) # nos dice cuantos ? hay


df = df.replace("?", pd.NA) # reemplazamos "? por NA que panda es considerado como nulo NaN
print(df.isna().sum()) # vemos cuantos NaN tenemos ahora
print(df.head())

for col in df.columns:
    print(col, df[col].unique()) # para ver valores unicos

# hay muchos valores sucios 
# age
df["Age"] = df["Age"].astype(str).str.strip()



