from pprint import pprint


def mostrar_resultado(results):
    # for index, row in results.iterrows():
    #     print(f'{row}\n')

    print()
    print(results.to_markdown())
    # pprint(results.dtypes)


def mostrar_menu():
    print(
        '\n'
        '1. Buscar información en departamento\n'
        '2. Salir\n'
    )
    try:
        opcion = int(input('Ingerese la opcion deseada: '))
    except Exception as e:
        opcion = -1
        raise e
    finally:
        return opcion


def solicitar_campos():
    try:
        nombre_departamento = input('Nombre del departamento: ')
        limite_registros = int(input('Numero de registros: '))
        campos = [nombre_departamento, limite_registros]
    except Exception as e:
        campos = ['', 0]
        raise e
    finally:
        return campos
