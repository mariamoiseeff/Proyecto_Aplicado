from src.validacion import validar_input

def pedir_inputs(mensaje):
    '''
    Le pide el numero al usuario y la valida 

    Parameters
    ----------
    mensaje : str
        Pregunta cantidad de altruistas/egoistas/turnos que desea el usuario

    Returns
    -------
    int
        Devuelve cantidades validadas 
    '''
    while True:
        numero = input(mensaje)
        try:
            numero_valido = validar_input(numero)
        except (ValueError, TypeError) as e:
            print(e)
        else: 
            break
    return numero_valido


