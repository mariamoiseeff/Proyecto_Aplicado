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
  TypeError
   Si el tipo de dato ingresado por el usuario es incorrecto.
  ValueError
   Si el numero ingresado es negativo.
   '''
  if type(numero) != int:
     raise TypeError("el dato ingresado es tipo incorrecto, debe ser un numero entero")
  if numero <= 0:
     raise ValueError("el numero ingresado no puede ser negativo, debe ser positivo")
  
  return int(numero)
  

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
      graficos que estan disponibles.
    TypeError
      Si el numero ingresado es un tipo de dato incorrecto. 
    '''
    if type(num) != int:
        raise TypeError("el dato ingresado es incorrecto, debe ser un numero entero")
    if num < 1 or num > 7:
        raise ValueError("el numero ingresado debe estar entre 1 y 7 ")
        
    return num

def validar_respuesta(otro_grafico):
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
    TypeError
      Si el dato ingresado es incorrecto 
    ValueError
      Si la respuesta ingresada es distinto a ("si, no")
    """
    
    if type(otro_grafico) != str:
        raise TypeError("el tipo de dato ingresado es incorrecto")
    if otro_grafico != "si" and otro_grafico != "no":
        raise ValueError("no es la respuesta esperada, ingrese (si o no)")
        
    return otro_grafico 
