import pandas as pd
from sodapy import Socrata

dict_columnas = {
    'ciudad_municipio_nom': 'Ciudad ubicacion',
    'departamento_nom': 'Departamento',
    'edad': 'Edad',
    'tipo_recuperacion': 'Tipo recuperacion',
    'estado': 'Estado',
    'pais_viajo_1_nom': 'Pais procedencia',
}


def obtener_informacion(nombre_departamento='RISARALDA', limite_registros=100):
    columnas_api = dict_columnas.keys()
    nombre_depto = nombre_departamento.upper()

    client = Socrata('www.datos.gov.co', None)
    results = client.get("gt2j-8ykr", limit=limite_registros,
                         departamento_nom=nombre_depto)

    results_df = pd.DataFrame.from_records(results, columns=columnas_api)
    results_df.rename(columns=dict_columnas, inplace=True)
    return results_df
