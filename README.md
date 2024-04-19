
# 'Dark Blue' Project | Empresa de buceo | Análisis de datos

   <h2>Descripción general</h2>

  Este proyecto tiene como objetivo ayudar a la empresa de buceo 'Dark Blue' a encontrar las mejores ubicaciones para el avistamiento de tiburones de gran tamaño durante sus actividades. Partimos de la premisa de que el número de tiburones está directamente relacionado con la probabilidad de avistamiento. Para ello, se han analizado datos externos que nos han permitido identificar patrones y tendencias que permitirán mejorar la experiencia de sus clientes.


## Planteamiento y problema

La empresa ofrece actividades de buceo con la expectativa de avistar tiburones, pero algunos clientes no logran verlos. Por tanto, surge la necesidad de analizar los datos disponibles para recomendar ubicaciones donde sea más probable avistar tiburones. Se plantea que factores como el mes y la ubicación pueden influir en el avistamiento de tiburones.


## Hipótesis

Planteamos la hipótesis de que el número de ataques de tiburones está relacionado con la mayor presencia de tiburones. Por tanto, se espera encontrar patrones que permitan identificar momentos y lugares con mayor actividad de tiburones, lo que facilitará la recomendación de ubicaciones para el avistamiento.


## Objetivo

El objetivo principal de este proyecto de análisis de datos es identificar cuándo y en qué ubicación hay mayor actividad de tiburones con el fin de recomendar sitios para avistarlos durante las actividades de buceo.


## Tecnologías utilizadas

1. Python: Lenguaje de programación utilizado para el análisis de datos.
2. Pandas: Biblioteca de Python utilizada para la manipulación y análisis de datos.
3. Seaborn: Biblioteca de visualización de datos basada en Matplotlib.
4. Matplotlib: Biblioteca de trazado de gráficos de Python.
5. Plotly: Biblioteca de gráficos interactivos para Python.


## Funciones y análisis de datos

Se han desarrollado varias funciones en Python para realizar el análisis de datos:

- data_upload_and_cleaning: Esta función carga el conjunto de datos, realiza el formateo de columnas, limpia los datos y prepara el dataframe para el análisis.
- last_10_years_data_calculator: Reduce los datos a los últimos 10 años para un análisis más reciente.
- week_day_and_month_calculator: Calcula el día de la semana y el mes a partir de la fecha del avistamiento de tiburones.

Además, se han creado funciones para la generación de gráficos que ayudan a visualizar los resultados del análisis:

- sharks_seen_evolution_heatmap: Visualiza la evolución de los avistamientos de tiburones a lo largo de los años.
- top_week_day_graph: Muestra los días de la semana donde se registran más avistamientos de tiburones.
- number_of_sharks_per_country_graph: Representa el número de tiburones avistados por país y mes.
- number_of_sharks_per_state_graph: Muestra las ciudades donde se registran más avistamientos de tiburones.
- number_of_sharks_per_location_graph: Visualiza las ubicaciones donde se avistan más tiburones.
- top_species_graph: Muestra las especies de tiburones más vistas.


## Mejora y futuro desarrollo

El proyecto actual representa un MVP (Producto Mínimo Viable) que cumple con los requisitos básicos de análisis de datos para recomendar ubicaciones de avistamiento de tiburones durante actividades de buceo. Sin embargo, existen diversas áreas de mejora y posibilidades de desarrollo futuro que podrían ampliar y enriquecer la funcionalidad del sistema. A continuación, se detallan algunas sugerencias para mejorar el proyecto:

### **Búsqueda de más datos**

1. Incorporación de Datos Meteorológicos: Obtener datos meteorológicos históricos para las ubicaciones de avistamiento de tiburones podría proporcionar información adicional sobre las condiciones climáticas durante los ataques de tiburones. Esto podría incluir datos como la velocidad del viento y las condiciones de marea.

2. Integración de Datos de Temperatura del Agua: La temperatura del agua es un factor importante que puede influir en la actividad de los tiburones. La adición de datos de temperatura del agua en diferentes ubicaciones y momentos del año podría enriquecer el análisis y las recomendaciones.

### **Mejora de visualizaciones**

1. Gráficos Interactivos: Implementar gráficos interactivos utilizando bibliotecas como Plotly o Dash permitiría a los usuarios explorar los datos de manera más dinámica. Esto podría incluir gráficos interactivos de dispersión, mapas de calor y gráficos de líneas que permitan filtrar y explorar los datos según diferentes criterios.

2. Visualizaciones 3D: Explorar la posibilidad de crear visualizaciones en 3D para representar la distribución espacial de los avistamientos de tiburones. Esto podría proporcionar una perspectiva más inmersiva de las ubicaciones de avistamiento y facilitar la identificación de patrones espaciales.

### **Optimización del Análisis**

1. Modelos Predictivos: Desarrollar modelos predictivos utilizando técnicas de aprendizaje automático para predecir la probabilidad de avistamiento de tiburones en diferentes ubicaciones y condiciones. Esto podría implicar la creación de modelos de regresión o clasificación utilizando datos históricos de ataques de tiburones y factores ambientales.

2. Análisis de Sentimientos: Incorporar análisis de sentimientos en los datos de testimonios de avistamientos de tiburones podría proporcionar información adicional sobre la percepción y la experiencia de los buceadores. Esto podría ayudar a identificar ubicaciones con una mayor satisfacción del cliente o áreas de mejora en la experiencia de avistamiento.

### **Mejoras en la usabilidad**

1. Desarrollo de una Interfaz de Usuario: Crear una interfaz de usuario intuitiva y fácil de usar que permita a los usuarios explorar los datos y recibir recomendaciones personalizadas sobre ubicaciones de avistamiento de tiburones.

2. Integración con Plataformas Existentes: Integrar el sistema de recomendación de ubicaciones de avistamiento de tiburones con plataformas existentes de reservas de actividades de buceo podría mejorar la experiencia del usuario y facilitar la planificación de viajes.

<br>

<br>

