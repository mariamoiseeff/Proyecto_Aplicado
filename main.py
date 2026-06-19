from src.inputs import pedir_inputs
import src.clases
from src.validacion import validar_eleccion_graficos
from src.validacion import validar_respuesta
from graficos import grafico_1_poblacion_por_turno
from graficos import grafico_2_torta_final
from graficos import grafico_3_torta_inicial
from graficos import grafico_4_interacciones_por_tipo
from graficos import grafico_5_recursos_promedio_final
from graficos import grafico_6_reproducciones
from graficos import grafico_7_muertes

# pedir datos para empezar la simulacion 
cant_altruistas_validado = pedir_inputs("Ingresar las cantidad de altruistas: ")
cant_egoistas_validado = pedir_inputs("Ingresar la cantidad de egoistas: ")
cant_turnos_validado = pedir_inputs("Ingresar la cantidad de turnos: ")

    
# convertir datos en personas 
poblacion = src.clases.Poblacion()
ID = 1
for numero in range(cant_altruistas_validado):
    persona = src.clases.Persona(False, ID)
    poblacion.agregar_personas(persona)
    ID += 1
    
for numero in range(cant_egoistas_validado):
    persona = src.clases.Persona(True, ID)
    poblacion.agregar_personas(persona)
    ID += 1

# comienza simulacion
poblacion.simulacion(cant_turnos_validado)


#graficos

grafico = input("Graficos disponibles:\n 1: Poblacion por turnos\n 2: Ver la proporcion entre egoistas y altruistas\n 3: Porcentaje de altruistas y egoistas al inicio de la simulacion\n 4: Interacciones por tipo\n 5: Promedio de recursos al final de la simulacion\n 6: Reproducciones de altruistas y de egoistas\n 7: Total de muertes de egoistas y de altruistas\n Ingresar grafico: ")


try:
    grafico_validado = validar_eleccion_graficos(grafico)    
except (ValueError, TypeError) as e:
    print(e)
else: 
    if grafico_validado == 1:
        grafico_pedido = grafico_1_poblacion_por_turno(poblacion.datos)
    elif grafico_validado == 2:
        grafico_pedido = grafico_2_torta_final(poblacion.datos)
    elif grafico_validado == 3:
        grafico_pedido = grafico_3_torta_inicial(poblacion.datos)
    elif grafico_validado == 4:
        grafico_pedido = grafico_4_interacciones_por_tipo(poblacion.datos)
    elif grafico_validado == 5:
        grafico_pedido = grafico_5_recursos_promedio_final(poblacion.datos)
    elif grafico_validado == 6:
        grafico_pedido = grafico_6_reproducciones(poblacion.datos)
    elif grafico_validado == 7:
        grafico_pedido = grafico_7_muertes(poblacion.datos)


while True:
    otro_grafico = input("Desea ver otro grafico? (Si/No) ") 
    try:
        otro_grafico_valido = validar_respuesta(otro_grafico)
        break
    except ValueError as e:
        print(e)

if otro_grafico_valido == "No":
    print("Simulacion finalizada")


while otro_grafico_valido == "Si":
   grafico = input("Graficos disponibles:\n 1: Poblacion por turnos\n 2: Ver la proporcion entre egoistas y altruistas\n 3: Porcentaje de altruistas y egoistas al inicio de la simulacion\n 4: Interacciones por tipo\n 5: Promedio de recursos al final de la simulacion\n 6: Reproducciones de altruistas y de egoistas\n 7: Total de muertes de egoistas y de altruistas\n Ingresar grafico: ")
   try:
       grafico_validado = validar_eleccion_graficos(grafico)
   except (ValueError, TypeError) as e:
       print(e)                  

   if grafico_validado == 1:
     grafico_pedido = grafico_1_poblacion_por_turno(poblacion.datos)
   elif grafico_validado == 2:
     grafico_pedido = grafico_2_torta_final(poblacion.datos)
   elif grafico_validado == 3:
     grafico_pedido = grafico_3_torta_inicial(poblacion.datos)
   elif grafico_validado == 4:
     grafico_pedido = grafico_4_interacciones_por_tipo(poblacion.datos)
   elif grafico_validado == 5:
     grafico_pedido = grafico_5_recursos_promedio_final(poblacion.datos)
   elif grafico_validado == 6:
     grafico_pedido = grafico_6_reproducciones(poblacion.datos)
   elif grafico_validado == 7:
     grafico_pedido = grafico_7_muertes(poblacion.datos)        

   while True:
       otro_grafico = input("Desea ver otro grafico? (Si/No) ") 
       try:
           otro_grafico_valido = validar_respuesta(otro_grafico)
           break
       except ValueError as e:
           print(e)
   if otro_grafico_valido == "No":
       print("Simulacion finalizada")
    


