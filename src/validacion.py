#validacion.py

def validar_input(numero):
    '''
    Valida que el numero ingresado por el usuario sea del tipo de dato correcto y lo convierte a entero(int).

    Parametros:
    -----------
    numero: int
      numero ingresado por el usuario.

    Returns:
    --------
    numero: int 

    Raises:
    -----
    ValueError
        Si el numero ingresado es negativo o si el numero no se pudo convertir a entero.
     '''
    try: 
        resultado = int(numero)

    except ValueError:
        raise ValueError("El dato ingresado debe ser un numero entero. ")
        
    if resultado <= 0: 
       raise ValueError("el numero ingresado no puede ser negativo, debe ser positivo")
   
    return resultado
  

def validar_eleccion_graficos(num):
    '''
    Valida que el numero ingresado por el usuario sea tipo de dato correcto 
    y se encuentre dentro del rango indicado(1-7).
    Parametros:
    ----------
    num : int
        Numero ingresado del usuario para visualizar graficos.

    Returns:
    -------
    num: int
    
    Raises:
    -------

    ValueError
      Si el numero ingresado por el usuario es distinto a los 
      graficos que estan disponibles o por si no se puede convertir el numero a entero. 
    '''
    try: 
        resultado = int(num)
    except ValueError: 
        raise ValueError("Informacion ingresada debe ser un numero entre 1 y 7")
    else:
        if resultado < 1 or resultado > 7:
            raise ValueError("el numero ingresado debe estar entre 1 y 7 ")
        
    return resultado

def validar_respuesta(otro_grafico_valido):
    """
    Parameters
    ----------
    otro_grafico : str
        Ingresa la respuesta del usuario si es que desea o no seguir visualizando.
        

    Returns
    -------
    otro_grafico = str
    
    Raises:
    -------
    ValueError
      Si la respuesta ingresada es distinto a ("Si, No")
    """
    if otro_grafico_valido != "Si" and otro_grafico_valido != "No":
        raise ValueError("no es la respuesta esperada, ingrese (Si o No)")
        
    return otro_grafico_valido
