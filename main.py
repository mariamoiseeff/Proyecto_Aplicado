import pandas as pd
from sec.validacion import validar_input
import clases
from src.clases import agregar_persona
# pedir datos para empezar la simulacion 
cant_altruistas = input("Ingresar las cantidad de altruistas: ")
cant_egoistas = input("Ingresar la cantidad de egoistas: ")
cant_turnos = input("Ingresar la cantidad de turnos: ")

try: 
    cant_altruistas_validado = validar_input(cant_altruistas)
except (ValueError, TypeError) as e:
    print(e)
    
try:
    cant_egoistas_validado = validar_input(cant_egoistas)
except (ValueError, TypeError) as e:
    print(e)
    
try:
    cant_turnos_validados = validar_input(cant_turnos)
except (ValueError, TypeError) as e:
    print(e)
    
# convertir datos en personas 
ID = 1
for range in cant_altruistas_validado:
    persona = clases.Persona(True, ID)
    ID += 1
    agregar_persona(persona)
    
for range in cant_egoistas_validado:
    persona = clases.Persona(False, ID)
    ID += 1
    agregar_persona(persona)

    