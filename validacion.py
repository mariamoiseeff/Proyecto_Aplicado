#validacion.py

def validar_input(cant_altruistas, cant_egoistas, cant_turnos):
  '''
  Valida que la informacion ingresada por el usuario sea del tipo de dato correcto 
  y dentro del rango permitido. 

  Parametros:
  -----------
  cant_altruistas: int 
    Cantidad de personas altruistas ingresadas por el usuario.
  cant_egoistas: int
    Cantidad de personas egoistas ingresadas por el usuario.
  cant_turnos: int
    Cantidad de turnos ingresados por el usuario para realizar la simulacion. #(no sabemos todavia las restricciones de los turnos)

  Returns:
  --------
  # no se que retorna, una tupla?, valores por separado? 
  cant_altruistas: int
  cant_egoistas:int
  cant_turnos: int

  Raises:
  -----
 TypeError
   Si el tipo de dato ingresado por el usuario es incorrecto.
 ValueError
   Si algunos de los datos ingresados es cero, negativo o supera el rango permitido
   Si cant_altruistas y cant_egoistas son cero al mismo tiempo (poblacion vacia). 
   '''
  
