from src.validacion import validar_input

def pedir_inputs(mensaje):
    while True:
        numero = input(mensaje)
        try:
            return validar_input(numero)
        except (ValueError, TypeError) as e:
            print(e)