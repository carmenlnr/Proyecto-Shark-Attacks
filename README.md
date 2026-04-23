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
- Eliminación de colummnas que no tendremos en cuenta para el análisis.
- Reemplazo de valores faltantes (`? → NaN`)
- Estandarización de `Activity`, `Country` y `Sex`
- Creación de variable binaria `Fatal` (0 = No, 1 = Sí)

### 2. Análisis Exploratorio (EDA)
- Distribución de ataques por país (E)
    -- Top 10 países con mas ataques (hay mas de 180 países)
    -- Porcentaje que representa cada país sobre el total
- Tasa de fatalidad global (E)
    -- En que países los ataques son más mortales¿?
- Actividades con mayor número de incidentes  (C)
- Tasa de fatalidad por actividad  (C)

### 3. KPIs utilizados
- Número total de ataques  
- Top países por frecuencia  
- Top actividades  
- % de ataques fatales (Distribución por sexo y edad) 
- Fatalidad media por actividad - 

---

## Resultados / Insights



---

## Próximos pasos
- Muestra 1612 valores únicos con descripciones detalladas, es imposible limpiar 1 por 1, hay que agruparlos.
- En fila "Others" hay casos especiales pendientes de revisión por varios erroes de escritura, que hay que separar de casos especiales. 
- Se analizaría con más detalle la edad de las personas que han sido victimas de ataques (por rangos) y la fatalidad.
- Qué sexo ha tenido más ataques y su relación con las actividaddes. 

---

## Cómo replicar el proyecto

