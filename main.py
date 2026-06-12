import pandas as pd
from src.inputs import pedir_inputs
import src.clases
from src.clases import agregar_persona
from src.clases import simulacion 
from graficos import generar_graficos
from graficos import validar_eleccion_graficos


# pedir datos para empezar la simulacion 
cant_altruistas_validado = pedir_inputs("Ingresar las cantidad de altruistas: ")
cant_egoistas_validado = pedir_inputs("Ingresar la cantidad de egoistas: ")
cant_turnos_validado = pedir_inputs("Ingresar la cantidad de turnos: ")

    
# convertir datos en personas 
poblacion = src.clases.Poblacion()
ID = 1
for numero in range(cant_altruistas_validado):
    persona = src.clases.Persona(False, ID)
    poblacion.agregar_persona(persona)
    ID += 1
    
for numero in range(cant_egoistas_validado):
    persona = src.clases.Persona(True, ID)
    poblacion.agregar_persona(persona)
    ID += 1

# comienza simulacion
src.clases.Poblacion.simulacion(cant_turnos_validado)


#graficos
grafico = input("Graficos disponibles:\n 1: Poblacion por turnos\n  2: Ver la proporcion entre egoistas y altruistas\n 3: Porcentaje de altruistas y egoistas al inicio de la simulacion\n 4: Interacciones por tipo\n 5: Promedio de recursos al final de la simulacion\n 6: Reproducciones de altruistas y de egoistas\n 7: Total de muertes de egoistas y de altruistas\n Ingresar grafico: ")
try:
    grafico_validado = validar_eleccion_graficos(grafico)
    grafico_pedido = generar_graficos(grafico)    
except (ValueError, TypeError) as e:
    print(e)


try:
    otro_grafico = input("Desea ver otro grafico? (Si/No) ")
except TypeError as e:
    print(e)

  
while otro_grafico != "No":
   grafico = input("Graficos disponibles:\n 1: Poblacion por turnos\n  2: Ver la proporcion entre egoistas y altruistas\n 3: Porcentaje de altruistas y egoistas al inicio de la simulacion\n 4: Interacciones por tipo\n 5: Promedio de recursos al final de la simulacion\n 6: Reproducciones de altruistas y de egoistas\n 7: Total de muertes de egoistas y de altruistas\n Ingresar grafico: ")
   try:
       grafico_validado = validar_eleccion_graficos(grafico)
       grafico_pedido = generar_graficos(grafico)
   except (ValueError, TypeError) as e:
       print(e)                  

          



