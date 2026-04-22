# Proyecto: Shark Attack Analysis for Tourism Safety

## Objetivo del proyecto

El objetivo de este proyecto es analizar datos históricos de ataques de tiburón para identificar patrones de riesgo y ayudar a una empresa de turismo acuático a tomar decisiones más seguras sobre destinos y actividades. Este análisis permite reducir riesgos y mejorar la seguridad del cliente.

---

## Dataset

- **Fuente:** Dataset histórico global de ataques de tiburón  
- **Tipo:** Datos reales con valores incompletos  

### Variables principales:
- `Country` → País del incidente  
- `Activity` → Actividad realizada en el momento del ataque  
- `Age` → Edad de la víctima  
- `Sex` → Género  
- `Fatal (Y/N)` → Resultado del ataque  #Dato a añadir.

---

## Proceso de análisis

### 1. Data Cleaning
- Eliminación de colummnas que no tendremos en cuenta para el análisis
- Reemplazo de valores faltantes (`? → NaN`)
- Conversión de `Age` a formato numérico
- Estandarización de `Activity`, `Country` y `Sex`
- Creación de variable binaria `Fatal` (0 = No, 1 = Sí)

### 2. Análisis Exploratorio (EDA)
- Distribución de ataques por país  
- Actividades con mayor número de incidentes  
- Tasa de fatalidad global  
- Tasa de fatalidad por actividad  

### 3. KPIs utilizados
- Número total de ataques  
- Top países por frecuencia  
- Top actividades  
- % de ataques fatales  
- Fatalidad media por actividad  

---

## Resultados / Insights



---

## Próximos pasos

 

---

## Cómo replicar el proyecto

