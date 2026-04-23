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
#df= pd.read_pickle("data.pkl") #Quito esta línea porque estaba duplicada por mi parte
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

print (df["Age"].unique())

import re

def clean_age(value):
    if value is None:
        return None

    value = str(value).lower().strip()

    # basura directa
    if value in ["", "?", "x", "!!", "a.m.", "make line green", "\xa0", "f"]:
        return None

    # texto interpretativo
    if "teen" in value:
        return 15
    if "adult" in value:
        return None
    if "elderly" in value:
        return 75
    if "young" in value:
        return 18

    # meses
    if "month" in value:
        return None

    # décadas
    if "20s" in value:
        return 25
    if "30s" in value:
        return 35
    if "40s" in value:
        return 45
    if "50s" in value:
        return 55
    if "60s" in value:
        return 65

    # extraer números
    nums = re.findall(r"\d+", value)

    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return float(nums[0])
    else:
        return sum(map(float, nums)) / len(nums)

df["Age_clean"] = df["Age"].apply(clean_age) #limpieza aplicda

print (df["Age_clean"].value_counts().sort_index())
print (df["Age_clean"].unique()) # vemos decimales (resultado de rangos aplicados en la funcion estos vienen de 16 to 18 = 17, 34 y 35 = 34,5 o 36,67, 35 = promedio)

# insight de edad tras limpiar hay edad de 1, 2,3 4 , 87 por ejemplo, edades demasiado pequeñas o grandes  entonces podrian ser niños
# reales o errores de registro. los decimales lo redondearemos.
df["Age_clean"] = df["Age_clean"].round()
print (df["Age_clean"].unique()) # edad ya estaria limpia sin decimales

#SEX: dejaremos M y F como validos, todo lo demás NaN
df["Sex_clean"] = df["Sex"].astype(str).str.strip().str.upper() #normalizamos texto

valid = ["M", "F"]
df.loc[~df["Sex_clean"].isin(valid), "Sex_clean"] = None

print (df["Sex_clean"].value_counts())
print (df["Sex_clean"].unique())
#Limpieza Country.

df["Country"]= df["Country"].str.upper() #Pone todas las letras en mayúsculas.
df["Country"]= df["Country"].str.strip() #Quita los espacios extra
reemplazos = {
"MALDIVE ISLANDS": "MALDIVES",
"COLUMBIA": "COLOMBIA",
"TURKS AND CAICOS":"TURKS & CAICOS",
"REUNION ISLAND": "REUNION",
"CEYLON": "SRI LANKA",
"CEYLON (SRI LANKA)": "SRI LANKA",
"ENGLAND": "UNITED KINGDOM",
"SCOTLAND": "UNITED KINGDOM",
"GRAND CAYMAN": "CAYMAN ISLANDS",
"HAWAII": "USA",
"OKINAWA": "JAPAN",
"ST. MARTIN": "ST MARTIN",
"ST. MAARTIN": "ST MARTIN",
"UNITED ARAB EMIRATES (UAE)": "UNITED ARAB EMIRATES"
}
df["Country"]= df["Country"].replace(reemplazos)
df["Country"] = df["Country"].str.replace("?","",regex=False).str.strip()
df.to_pickle("data.pkl")
print(df["Country"].unique())
# Erika, comienzo con limpieza de "activity"
pd.set_option('display.max_seq_items', None)
print(df["Activity"].value_counts().to_string())
# Muestra 1612 valores únicos con descripciones detalladas, es imposible limpiar 1 por 1, hay que agruparlos.


