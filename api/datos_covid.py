import pandas as pd
from sodapy import Socrata


def obtener_informacion(nombre_departamento='RISARALDA', limite_registros=100):
    columnas = ['ciudad_municipio_nom', 'departamento', 'edad',
                'tipo_recuperacion', 'estado', 'pais_viajo_1_nom']
    nombre_depto = nombre_departamento.upper()

    client = Socrata('www.datos.gov.co', None)
    results = client.get("gt2j-8ykr", limit=limite_registros,
                         departamento_nom=nombre_depto)

    results_df = pd.DataFrame.from_records(results, columns=columnas)
    return results_df
