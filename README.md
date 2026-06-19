# Proyecto_Aplicado
Proyecto final de programación: simulación de interacciones entre egoistas y altruistas - selección natural

 1.⁠ ⁠Título de nuestro proyecto: 
 Simulacion de seleccion Natural del egoismo
 
 2.⁠ ⁠Integrantes: 
 Clara Antelo Cernadas, Sofia Davidov, Maria Moiseeff y Guadalupe Margiotta. 
 
 3.⁠ ⁠Objetivo, descripción general del funcionamiento del sistema, principales
funcionalidades y adjudicación de la parte del programa que realizó cada integrante:
El objetivo de nuestro programa es realizar una simulacion natural del comportamiento de los egoistas y altruistas, 
nuestra idea es demostrar que sobreviven mayormente los egoistas, ya que como plantea la teoria evolutiva, 
los humanos egoistas finalmente son los que se terminan reproduciendo y subsistiendo en el tiempo.

DIVISION DEL TRABAJO:
- Clara Antelo Cernadas: inputs.py, main.py
- Maria Moiseff: clases.py
- Guadalupe Margiotta: validacion.py, diagramas de flujo(validacion)
- Sofia Davivov: graficos.py, diagramas de flujo(main y graficos)

 4.⁠ ⁠Descripción de la fuente de datos (en caso de haber utilizado una).
No utilizamos 

 5.⁠ ⁠Instrucciones para ejecutar el programa.
1) Correr el programa con el "run file"
2) Responder inputs
3) Elegir las metricas que se desean ver

 
 6.⁠ ⁠Librerías utilizadas.
 - Matplotlib.pyplot  → Creación y visualización de gráficos estadísticos de los resultados de la simulación
 - Random: Selección aleatoria de parejas e individuos para interactuar durante la simulación.
 - Pandas: Almacenamiento y procesamiento de los datos de cada turno mediante DataFrames.

 7.⁠ ⁠Estructura del repositorio.
 - src
     - clases.py
     - validacion.py
      - inputs.py
 - main.py
 - graficos.py
 - graficos → carpeta que muestra los graficos al final de la simulacion
 - README
 
 
 8.⁠ ⁠Explicación breve de las clases implementadas (si corresponde).
 Clase Persona: 
 - crea objetos de tipo "persona", que representan una persona de la poblacion.
 - tienen una cantidad de recursos que se van modificando en las interacciones y rondas. 
 - tienen su condicion de egoista o no egoista, y un "ID" que usamos para establecer parentezcos
 - pueden reproducirse, es decir si pasan el umbral de 50 recursos acumulados, se crea una persona nueva con el mimo ID (el indicador de parentezco) y misma condicion de egoista / altruista. 
 - tambien, si llegan a tener 0 o menos recursos, se mueren (se los saca de la poblacion)
 
 Clase Poblacion: 
 - contiene a las personas de la poblacion almacenadas en una lista
 - guarda la informacion de los turnos de la simulacion en un DataFrames
 - tiene metodos para: 
     - agregar datos de una ronda a una fila del dataframe
     - agregar y sacar persoanas a la lista de la poblacion
     - hacer una ronda de interacciones de la poblacion: 
         - copia la lista de personas, la recorre y empareja aleatoriamente con otra persona de la lista. 
         - segun sus condiciones de egoista / altruista, suma o resta los recursos correspondientes
         - retorna datos necesarios para registrar en el data frame 
    - filtrar poblacion: 
        - si hay muertes o reproducciones fijandose los recursos
        - retorna datos necesarios para dataframe
    - generar la simulacion: 
        - segun la cantidad de rondas deseadas, empareja y hace la interaccion, filtra poblacion y agrega datos por cada ronda. 
 
 
 9.⁠ ⁠Explicación breve de las funciones principales.
 - validar_input → recibe como parametro un numero, que luego es transformado en entero. 
     - Funcion: Validar que el numero ingresado por el usuario sea del tipo de dato correcto y lo convierte a entero(int).
 - validar_eleccion_grafico → recibe como parametro un numero
     - Funcion: Validar que el numero ingresado por el usuario sea tipo de dato correcto y se encuentre dentro del rango indicado(1-7).
 - validar_respuesta → recibe como parametro un string
     - Funcion: Validar que el tipo de dato sea correcto y que el string corresponda a un "si" o "no". 
 -  pedir_inputs → recibe como parametro un mensaje, y pide los inputs 
     - Funcion: Obtener los inputs requeridos para poder correr el programa (empezar la simulacion)
 

10.⁠ ⁠Resultados, salidas, métricas, gráficos o funcionalidades generadas, según
corresponda 

FUNCIONALIDADES GENERADAS:

El sistema permite:
-  registrar la cantidad inicial de individuos altruistas y egoistas
- configurar la cantidad de rondas en la simulacion 
-  Validar los datos ingresados por el usuario para garantizar el correcto funcionamiento del programa 
- Ejecuta una simulacion de la evolucion de la poblacion entre altruistas y egoistas
-  Genera DataFrames por ronda para almacenar el estado de la poblacion en ese momento y poder visualizarla 
-  Calcula metricas relacionadas a como evoluciona la poblacion a lo largo del tiempo

SALIDAS Y RESULTADOS:

 Una vez que la simulacion finaliza, el programa permite visualizr el comportamiento de la problacion a traves de las decisiones de las cantidades ingresadas por el usuario:
- la cantidad de altruistas y egoistas en cada ronda 
-  como evoluciona la poblacion a lo largo del tiempo (inicio-final, que poblacion aumento, quien disminuyo, etc.)
-  el promedio de los recursos acumulados 
-  muestra las frecuencias de las distintas interacciones que se generaron(AA-EE,AA-AA, Etc)
-  muestra el numero total de muertes o reproducciones

 - GRAFICOS/OUTPUTS:

    Gráfico 1:  Gráfico de líneas: Evolución de la población por turno → Sirve para ver si una condición crece, decrece o desaparece a lo largo de la simulación.
  
    Gráfico 2: Gráfico de torta: Distribución final de la poblacion → Muestra en porcentaje cómo quedó repartida la población (entre egoistas y altruistas) al terminar la simulación. Es el resultado principal: qué condición dominó al final.
  
    Gráfico 3: Gráfico de torta: Distribución inicial de la problacion → Igual que el gráfico 2 pero con los datos del primer turno. Sirve para compararlo con el gráfico 2 y ver cuánto cambió la proporción entre el inicio y el final de la simulación.
  
    Gráfico 4: Gráfico de barras: Interacciones por tipo, iene cuatro barras: AA, AE, EE y parientes → La altura de cada barra muestra cuántas veces ocurrió ese tipo de encuentro durante toda la simulación. Sirve para ver qué combinación fue más frecuente y si eso tuvo relación con el resultado final.
  
    Gráfico 5: Gráfico de barras: Recursos promedio al final → La altura de cada barra muestra el promedio de recursos que tiene cada individuo de esa condición al terminar la simulación. Sirve para ver cuál de las dos condiciones terminó acumulando más recursos.
  
    Gráfico 6: Gráfico de barras: Reproducciones por condición → La altura de cada barra muestra el total de reproducciones que tuvo cada condición durante toda la simulación. Sirve para ver qué condición se reproduce más a lo largo del juego.
  
    Gráfico 7:  Gráfico de barras: Muertes por condición → La altura de cada barra muestra el total de muertes que tuvo cada condición durante toda la simulación. Sirve para ver qué condición tuvo más bajas y relacionarlo con el resultado final.

 
11.⁠ ⁠Diagramas de diseño.
Se encuentran en la carpeta "diagramas de flujo". 
Se realizaron diagramas de:
- Codigo principal
- Funciones principales. 

12.⁠ ⁠Declaración de uso de IA.
Para realizar este proyecto, utilizamos la herramienta Claude.ai y ChatGPT para ayudarnos con algunas dudas que nos fueron surgiendo.
- Para validacion, se le pidio a Claude: "recomendame una herramienta de programacion para validar un tipo de dato", asi fue como me recomendo utilizar isinstance().
- Se le pidio a Claude que nos encuentre el error en el codigo si es que nosotras no lo podiamos encontrar.
- Fue utilizada tambien para la elaboracion mas formal de algunos docstrings de los graficos
- Chat GPT nos ayudo a encontrar errores en el codigo y ver si funcionaba bien la simulacion antes de tener todo el programa listo. 
    - se le paso el documento de diseño del proyecto con el promt "esta bien mi codigo? funciona en crear las clases y los metodos de la simulacion?"
    - con la respuesta, ayudo a simplificar el codigo ya que habian cosas repetidas para llegar a la estructura del ciclo while de ahora. 
- Chat GPT nos ayudo a programar como se iba a guardar la informacion en el dataframe de cada turno, ya que nos costaba pensar como podiamos crear una fila con toda la informacion en un dataframe vacio. El prompt fue: 
    "rol: estudiante de programacion haciendo este trabajo aplicado que te explica el documento de diseño. necesito guardar la info de un turno en el dataframe. necesito que me ayudes con el codigo que no se como hacerlo. nose si hacer un metodo de poblacion por separado o que"
- Chat gpt me aconsejo la facilidad del programa en graficos sacando el diccionario para que el estilo no se haga de cada funcion, sino para que se haga directamente de forma global.

13.⁠ ⁠Notas o explicaciones adicionales para correr correctamente el programa.
- Leer atentamente lo que les pide los inputs para responder correctamente y evitar que el programa salte con un ERROR. 
