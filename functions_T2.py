def data_upload_and_cleaning(url = "https://www.sharkattackfile.net/spreadsheets/GSAF5.xls"):

  """
  - Cargamos el dataframe y desplegamos todas las columnas
  - Formateamos el nombre de las columnas poniendo todos los caracteres en minúscula, reemplazando los espacios y los puntos por '_' y los ':' por espacio.
  - Eliminamos las columnas que no necesitamos para el objetivo del proyecto
  """
  import pandas as pd
  df = pd.read_excel(url)
  pd.set_option("display.max_columns",None)
  df.columns = df.columns.str.lower().str.strip().str.replace(" ","_").str.replace(".","_").str.replace(":","")
  df.drop(["unnamed_11", "unnamed_21", "unnamed_22", "case_number_1", "case_number", "href", "href_formula", "pdf", "original_order", "source"], axis = 1, inplace = True)

  """
  Aqui lo que hacemos es cambiar todas las fechas a un formato apto para 'date'.

  Por lo tanto lo primero que hacemos es cambiar los meses a numero y quitar los guiones por espacios.

  Luego los tranformamos en formato 'date' en una nueva columna llamada 'date_clean'
  y en las filas que no se han cambiado las eliminamos ya que con esas filas no podemos trabajar
  que en total han sido unas 1000 de 4810(entre esas filas que hemos eliminado han sido las que no tenian dia o mes).

  Finalmente hemos pasado las fechas de 'date_clean' a 'date' y hemos eliminado 'date_clean'.
  """

  date_values_combine = {
    "Jan" : "01",
    "Feb" : "02",
    "Mar" : "03",
    "Apr" : "04",
    "May" : "05",
    "Jun" : "06",
    "Jul" : "07",
    "Aug" : "08",
    "Sep" : "09",
    "Oct" : "10",
    "Nov" : "11",
    "Dec" : "12"
  }

  for nombre, numero in date_values_combine.items():
    df["date"] = df["date"].str.replace(nombre, numero)

  df["date"] = df["date"].str.replace("-", " ")

  df["date_clean"] = pd.to_datetime(df["date"], format="%d %m %Y", errors='coerce')

  df = df.dropna(subset=["date_clean"])

  df["date"] = df["date_clean"]

  df = df.drop(columns = ["date_clean"])

  """ limpiamos 'type':
      - Creamos un nuevo diccionario con los nuevos valores para 'type"
      - Reemplazamos los nuevos valores en la columna
      - Creamos una lista con los valores que nos queremos quedar
      - Actualizamos la columna solo con los valores que queremos
  """
  type_values_combine = {
     " Provoked" : "Provoked",
      "Boat" : "Watercraft"
  }

  df["type"] = df["type"].replace(type_values_combine)

  type_list = ["Unprovoked", "Provoked", "Watercraft"]

  df = df[df["type"].isin(type_list) == True]

  """ limpiamos el género:
      - Combinamos todos los valores 'M'
      - Creamos un nuevo diccionario con los nuevos valores para sex
  """

  sex_values_combine = {
      " M" : "M",
      "M " : "M"
  }

  df["sex"] = df["sex"].replace(sex_values_combine)

  """limpiamos las actividades:
    - Eliminamos los espacios y reemplazamos las comas por espacios, separamos las frases por palabras y extraemos tan solo la primera
  """

  df["activity"] = df["activity"].str.strip().str.replace(",","").str.split(" ").str[0]

  """limpiamos los nombres:
    - Eliminamos los espacios
    - Creamos índice al valor Name y contamos cada uno
    - Creamos una lista con los nombres que se repiten menos de 3 veces y la llamamos valid_name
    - Actualizamos el df incluyendo los nombres que están dentro de esta lista
    - Creamos manualmente una lista 'invalid_name_values' con algunos de los valores incorrectos que vemos que permanecen
    - Actualizamos el dataframe para que elimine los valores incorrectos
  """

  df["name"] = df["name"].str.strip()

  #eliminamos espacios antes y después de cada string y eliminamos mayúsculas para que la columna 'country' tenga el mismo formato que el resto de columnas de ubicación.

  df["country"] = df["country"].str.strip().str.title()

  #eliminamos espacios antes y después de cada string

  df["state"] = df["state"].str.strip()

  #eliminamos espacios antes y después de cada string

  df["location"] = df["location"].str.strip()

  #quitamos espacios antes y después

  df["injury"] = df["injury"].str.strip()

  #quitamos comillas y espacios

  df["species"] = df["species"].str.strip().str.replace('"', "")

  return df


def last_10_years_data_calculator(df):

  """ Vamos a reducir los datos a los ultimos 10 años.
    -creamos una lista con los años deseados y solo dejamos los datos de esos años.
  """

  year_valid = []
  actual_year = 2024
  for x in range(10):
    y = actual_year-x
    year_valid.append(y)

  df_ultimos_anyos = df[df["year"].isin(year_valid) == True]

  return df_ultimos_anyos


def week_day_and_month_calculator(df_ultimos_anyos):

  df_ultimos_anyos['week_day'] = df_ultimos_anyos['date'].dt.day_name(locale='')

  df_ultimos_anyos["month"] = df_ultimos_anyos["date"].dt.month

  return df_ultimos_anyos
