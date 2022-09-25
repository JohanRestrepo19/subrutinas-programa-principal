from api.datos_covid import obtener_informacion
from iu.interfaz_usuario import mostrar_menu, mostrar_resultado
from iu.interfaz_usuario import solicitar_campos


def main():
    opcion = -1
    nombre_departamento = ''
    limite_registros = 0

    while True:
        opcion = mostrar_menu()
        if (opcion == 1):
            nombre_departamento, limite_registros = solicitar_campos()
            results = obtener_informacion(
                nombre_departamento, limite_registros)
            mostrar_resultado(results)
        elif (opcion == 2):
            break
        else:
            print('Opcion no válida!')
