# Proyecto_Aplicado
proyecto final de programación: simulación de interacciones entre egoistas y altruistas - selección natural

 1.⁠ ⁠Título de nuestro proyecto: 
 Simulacion de seleccion Natural del egoismo
 
 2.⁠ ⁠Integrantes: 
 Clara Antelo Cernadas, Sofia Davidov, Maria Moiseeff y Guadalupe Margiotta. 
 
 3.⁠ ⁠Objetivo, descripción general del funcionamiento del sistema, principales
funcionalidades y adjudicación de la parte del programa que realizó cada integrante:
El objetivo de nuestro programa es realizar una simulacion natural del comportamiento de los egoistas y altruistas, nuestra idea es demostrar que sobreviven mayormente los egoistas, ya que como plantea la teoria evolutiva, los humanos egoistas finalmente son los que se terminan reproduciendo y subsistiendo en el tiempo.

DIVISION DEL TRABAJO:
- Clara Antelo Cernadas: inputs, main.py
- Maria Moiseff: clases.py
- Guadalupe Margiotta: validacion.py
- Sofia Davivov: graficos.py

 4.⁠ ⁠Descripción de la fuente de datos (en caso de haber utilizado una).
No utilizamos 

 5.⁠ ⁠Instrucciones para ejecutar el programa.
1) Correr el programa con el "run file"
2) Responder inputs
3) Elegir las metricas que se desean ver

 
 6.⁠ ⁠Librerías utilizadas.
 - Matplotlib.pyplot --> Creación y visualización de gráficos estadísticos de los resultados de la simulación
 - Random: Selección aleatoria de parejas e individuos para interactuar durante la simulación.
 - Pandas: Almacenamiento y procesamiento de los datos de cada turno mediante DataFrames.

 7.⁠ ⁠Estructura del repositorio.
 (falta)
 
 
 8.⁠ ⁠Explicación breve de las clases implementadas (si corresponde).
 Clase Persona: 
 - crea objetos de tipo "persona", que representan una persona de la poblacion.
 - tienen una cantidad de recursos que se van modificando en las interacciones y rondas. 
 - tienen su condicion de egoista o no egoista, y un "ID" que usamos para establecer parentezcos
 - pueden reproducirse, es decir si pasan el umbral de 50 recursos acumulados, se crea una persona nueva con el mimo ID (el indicador de parentezco) y misma condicion de egoista / altruista. 
 - tambien, si llegan a tener 0 o menos recursos, se mueren (se los saca de la poblacion)
 
 Clase Poblacion: 
 - contiene a las personas de la poblacion e=almacenadas en una lista
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
 - validar_input →  recibe como parametro un numero, que luego es transformado en entero. Funcion: Validar que el numero ingresado por el usuario sea del tipo de dato correcto y lo convierte a entero(int).
 - validar_eleccion_grafico → recibe como parametro un numero
Funcion: Validar que el numero ingresado por el usuario sea tipo de dato correcto y se encuentre dentro del rango indicado(1-7).
- validar_respuesta → recibe como parametro un string
Funcion: Validar que el tipo de dato sea correcto y que el string corresponda a un "si" o "no". 
 
10.⁠ ⁠Resultados, salidas, métricas, gráficos o funcionalidades generadas, según
corresponda 
(falta) 

11.⁠ ⁠Diagramas de diseño.
Se encuentran en la carpeta "diagramas.py". 
Se realizaron diagramas de:
- Codigo principal
- Funciones principales. 

12.⁠ ⁠Declaración de uso de IA.
Para realizar este proyecto, utilizamos la herramienta Claude.ai para ayudarnos con algunas dudas que nos fueron surgiendo.
- Para validacion, le pedi a Claude: "recomendame una herramienta de programacion para validar un tipo de dato", asi fue como me recomendo utilizar isinstance().
- Se le pidio a Claude que nos encuentre el error en el codigo si es que nosotras no lo podiamos encontrar.
- Fue utilizada tambien para la elaboracion mas formal de algunos docstrings de los graficos
(completar cada uno los prompts utilizados) 

13.⁠ ⁠Notas o explicaciones adicionales para correr correctamente el programa.
- Leer atentamente lo que les pide los inputs para responder correctamente y evitar que el programa no salte con un ERROR. 
