#aca creo las clases de persona y poblacion

import random
import pandas as pd


class Persona:
    def __init__ (self, condicion, ID):
        '''
        inicializa un objeto persona

        Parameters
        ----------
        condicion : bool
            TRUE si la persona creada es egoista y FALSE si la persona es altruista.
        ID : int
            id de persona creada (la usaremos despues para identificar a los "parientes" despues de la reproduccion).


        '''
        self.egoista = condicion
        self.id = ID
        self.recursos =  40 #tenemos que decidir el valor fijo
        
    def reproduccion(self): 
        '''
        crea un objeto persona con mismo ID y condicion
        
        returns: 
            hijo --> un objeto persona
            
        '''
        
        hijo = Persona(self.egoista , self.id)
        
        return hijo
    

class Poblacion: 
    def __init__ (self):
        '''
        inicializa un objeto de Poblacion

        '''
        
        self.personas = []
        self.datos = pd.DataFrame(
            columns = 
            ["turno" , "cant_egoistas" , "cant_altruistas" , "total_personas", 
             "cant_interacciones_EE", "cant_interacciones_EA" , "cant_interacciones_AA" , "cant_interacciones_parientes" ,
             "cant_reproducciones_E" , "cant_reproducciones_A", "cant_muertes_E", "cant_muertes_A",
             "recursos_promedio_E" , "recursos_promedio_A"]
            )
        
    def agregar_datos_turno(self, turno, interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes, reproducciones_E, reproducciones_A , muertes_E , muertes_A, recursos_E, recursos_A): 
        '''
        Agrega los datos de una ronda de interacciones a un dataframe que registra la informacion de todo el turno

        Parameters
        ----------
        turno : int
            numero de ronda de la interaccion.
        interacciones_EE : int
            cantidad de interacciones entre dos egoistas registradas en la simulacion.
        interacciones_EA : int
            cantidad de interacciones entre un egoista y un altruista registradas en la simulacion.
        interacciones_AA : int
            cantidad de interacciones entre dos altruistas registradas en la simulacion.
        interacciones_parientes : int
            cantidad de interacciones entre dos parientes (EE - AA) registradas en la simulacion..
        reproducciones_E : int
            cant de reproducciones de los egoistas de una ronda.
        reproducciones_A : int
            cant de reproducciones de los egoistas de una ronda.
        muertes_E : int
            cant de muertes de los egoistas de una ronda.
        muertes_A : int
            cant de muertes de los altruistas de una ronda.
        recursos_E: 
            cant de recursos promedio acumulados por los egoistas en una ronda
        recursos_A:
            cant de recursos promedio acumulados por los altruistas en una ronda

        Returns
        -------
        None.

        '''
        cant_egoistas = 0
        cant_altruistas = 0
        
        for persona in self.personas: 
            if persona.egoista == True: 
                cant_egoistas+= 1
            else: 
                cant_altruistas +=1 
        
        nueva_fila = {
        "turno": turno,
        "cant_egoistas": cant_egoistas,
        "cant_altruistas": cant_altruistas,
        "total_personas": len(self.personas),
        "cant_interacciones_EE": interacciones_EE,
        "cant_interacciones_EA": interacciones_EA,
        "cant_interacciones_AA": interacciones_AA,
        "cant_interacciones_parientes": interacciones_parientes,
        "cant_reproducciones_E": reproducciones_E,
        "cant_reproducciones_A": reproducciones_A,
        "cant_muertes_E": muertes_E,
        "cant_muertes_A": muertes_A ,
        "recursos_totales_E": recursos_E,
        "recursos_totales_A": recursos_A
        
        }
        
        self.datos.loc[len(self.datos)] = nueva_fila
        
    def agregar_personas(self, persona): 
        '''
        agrega un objeto Persona a la lista de las personas de la poblacion
        
        parametros: 
            persona: objeto tipo Persona
        return: None
        '''
        
        self.personas.append(persona)
    
    def muerte(self, persona): 
        '''
        saca a una persona de la lista de la poblacion. 
        
        parametros: 
            persona: objeto tipo Persona
        raise: 
            ValueError si la persona que se quiere eliminar no esta en la lista o si la lista esta vacia
        '''
        if len(self.personas) == 0: 
            raise ValueError("La lista esta vacia")
        if persona not in self.personas.copy(): 
            raise ValueError("La persona que se esta queriendo eliminar de la poblacion no esta en la lista.")
       
        self.personas.remove(persona)
        
    def ronda_interaccion(self):
        '''
        empareja aleatoriamente dos personas de la población, y depende la condición de altruista/egoísta distribuye recursos. 
        
        returns: 
            interacciones_EE: int --> cantidad de interacciones entre dos egoistas por ronda
            interacciones_EA: int --> cantidad de interacciones entre egoista/altruista y altruista/egoista por ronda
            interacciones_AA: int --> cantidad de interacciones entre dos altruista por ronda
            interacciones_parientes: int --> cantidad de interacciones entre parientes por ronda (egoista/egoista y altruista/altruista)
            recursos_E: int --> cantidad de recursos acumulados por todos los egoistas por ronda
            recursos_A: int --> cantidad de recursos acumulados por todos los altruistas por ronda
        ''' 
        interacciones_EE = 0
        interacciones_EA = 0
        interacciones_AA = 0
        interacciones_parientes = 0
        recursos_E = 0
        recursos_A = 0
        
        lista_emparejamientos = self.personas.copy()
                
        if len(lista_emparejamientos) % 2 != 0:
            indice_excluido = random.randint(0, len(lista_emparejamientos)-1)
            lista_emparejamientos.pop(indice_excluido)

        while len(lista_emparejamientos) >= 2:

            persona = lista_emparejamientos[0]
            lista_emparejamientos.remove(persona)

            indice_pareja = random.randint(0, len(lista_emparejamientos)-1)
            pareja = lista_emparejamientos[indice_pareja]

            lista_emparejamientos.remove(pareja)
            
            if (persona.egoista == True and pareja.egoista == False): 
                persona.recursos += 5 
                pareja.recursos -= 5
                interacciones_EA +=1
                recursos_E += 5
                recursos_A -=5
                
            elif persona.egoista == False and pareja.egoista == True: 
                persona.recursos -= 5
                pareja.recursos += 5
                interacciones_EA +=1
                recursos_E += 5
                recursos_A -=5
                
                
            elif persona.egoista == False and pareja.egoista == False: 
                interacciones_AA +=1
                if persona.id == pareja.id: #si los altruistas son parientes suman mas
                    interacciones_parientes +=1
                    persona.recursos +=2
                    pareja.recursos +=2
                    recursos_A +=4
                else: 
                    persona.recursos += 1
                    pareja.recursos +=1
                    recursos_A =+ 2
                    
            elif persona.egoista == True and pareja.egoista == True: 
                interacciones_EE +=1
                if  persona.id == pareja.id: #esto es si los dos egoistas son parientes
                    persona.recursos +=1
                    pareja.recursos +=1
                    recursos_E += 2
        
        return interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes, recursos_E, recursos_A
  
  
    def filtrar_poblacion(self): 
        '''
        filtra a las personas de la lista si se mueren o si se reproducen agrega otra
        cambia la lista del atributo de personas. 
        
        returns: 
            reproducciones_E : int
                cant de reproducciones de los egoistas de una ronda.
            reproducciones_A : int
                cant de reproducciones de los egoistas de una ronda.
            muertes_E : int
                cant de muertes de los egoistas de una ronda.
            muertes_A : int
                cant de muertes de los altruistas de una ronda.
        '''
        reproducciones_E = 0
        reproducciones_A = 0
        muertes_E = 0
        muertes_A = 0
        
        for persona in self.personas: 
            if persona.recursos <= 0: 
                try: 
                    self.muerte(persona)
                except ValueError as e: 
                    return e
                else: 
                    if persona.egoista == True: 
                        muertes_E += 1
                    else: 
                        muertes_A +=1   
                
            if persona.recursos > 50: 
                if persona.egoista == True: 
                    reproducciones_E +=1
                else: 
                    reproducciones_A +=1
                
                hijo = persona.reproduccion()
                hijo.recursos = 15
                self.agregar_personas(hijo)
                persona.recursos -= 40
        
        return reproducciones_E, reproducciones_A, muertes_E, muertes_A
    
    def simulacion(self, rondas):
        '''
        genera simulacion
        paramentros: 
            rondas: int --> numero de rondas ingresado por el ususario
        '''        
        for turno in range(1, rondas + 1): 
            interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes, recursos_E, recursos_A = self.ronda_interaccion()
            reproducciones_E, reproducciones_A, muertes_E, muertes_A = self.filtrar_poblacion()
            self.agregar_datos_turno(turno, interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes, reproducciones_E, reproducciones_A, muertes_E, muertes_A, recursos_E, recursos_A)
            if len(self.personas) == 0: 
                print(f"Termino la simulacion antes de tiempo porque la poblacion se quedo in personas. Duro {turno} rondas. ")
                break
        print("Simulacion terminada")
        

poblacion = Poblacion()

p1 = Persona(True, 1)
poblacion.agregar_personas(p1)

p2 = Persona(False, 1)
poblacion.agregar_personas (p2)

p3 = Persona(False, 2)
poblacion.agregar_personas(p3)

p4 = Persona(False, 3)
poblacion.agregar_personas(p4)

poblacion.simulacion(30)

import matplotlib.pyplot as plt
import os
 

#  COLORES Y ESTILO GENERAL:

COLOR_EGOISTA   = "#c0392b"   # rojo  → representa a los egoístas
COLOR_ALTRUISTA = "#2980b9"   # azul  → representa a los altruistas
 

ESTILO = {
    "font.family":        "DejaVu Sans",
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "axes.grid":          True,
    "grid.linestyle":     "--",
    "grid.alpha":         0.4,
    "figure.facecolor":   "white",
    "axes.facecolor":     "#f9f9f9",
}
plt.rcParams.update(ESTILO)
 

#  FUNCIÓN PRINCIPAL:
 
def generar_graficos(df):
    """
    Función principal del módulo. Es la única que el resto del grupo
    necesita llamar desde el main para generar todos los gráficos.
 
    Recibe el DataFrame de la simulación con UNA FILA POR TURNO,
    verifica que tenga las columnas necesarias, crea la carpeta de
    salida si no existe, y llama a cada una de las 7 funciones de gráficos.
 
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con una fila por turno.
        Columnas necesarias:
            - turno                   (int)   → número de turno
            - cant_egoistas           (int)   → cantidad de egoístas ese turno
            - cant_altruistas         (int)   → cantidad de altruistas ese turno
            - cant_interacciones_EE        (int)   → interacciones egoísta-egoísta sin parentesco
            - cant_interacciones_EA        (int)   → interacciones altruista-egoísta sin parentesco
            - cant_interacciones_AA        (int)   → interacciones altruista-altruista sin parentesco
            - cant_interacciones_parientes (int)   → interacciones entre cualquier par con mismo ID
            - cant_reproducciones_A        (int)   → reproducciones de altruistas ese turno
            - cant_reproducciones_E        (int)   → reproducciones de egoístas ese turno
            - total_personas               (int)   → total de personas ese turno
            - recursos_totales_A           (int)   → suma de recursos de todos los altruistas ese turno
            - recursos_totales_E           (int)   → suma de recursos de todos los egoístas ese turno
 
    Returns
    -------
    None
        Guarda los 7 gráficos como archivos .png en la carpeta 'graficos/'.
    """
 
    
    columnas_necesarias = [
        "turno", "cant_egoistas", "cant_altruistas",
        "cant_interacciones_EE", "cant_interacciones_EA", "cant_interacciones_AA",
        "cant_interacciones_parientes",
        "cant_reproducciones_A", "cant_reproducciones_E", "total_personas",
        "recursos_promedio_A", "recursos_promedio_E"
    ]
    for col in columnas_necesarias:
        if col not in df.columns:
            print(f"Error: falta la columna '{col}' en el DataFrame.")
            return
 
    os.makedirs("graficos", exist_ok=True)
 
    # Llama a cada gráfico en orden
    grafico_1_poblacion_por_turno(df)
    grafico_2_torta_final(df)
    grafico_3_torta_inicial(df)
    grafico_4_interacciones_por_tipo(df)
    grafico_5_recursos_promedio_final(df)
    grafico_6_reproducciones(df)
    grafico_7_muertes(df)
 
    print("\nTodos los gráficos fueron guardados en la carpeta 'graficos/'.")
 

#  GRÁFICO 1 — Población por turno (líneas):
 
def grafico_1_poblacion_por_turno(df):
    """
    Gráfico de líneas con dos líneas: una azul para altruistas y una roja
    para egoístas. Muestra cuántos individuos de cada tipo hay en cada turno.
 
    Como el DataFrame tiene una fila por turno con columnas cant_altruistas
    y cant_egoistas, se grafican directamente esas columnas contra el turno.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
 
    ax.plot(df["turno"], df["cant_altruistas"],
            color=COLOR_ALTRUISTA, linewidth=2,
            marker="o", markersize=4, label="Altruistas")
 
    ax.plot(df["turno"], df["cant_egoistas"],
            color=COLOR_EGOISTA, linewidth=2,
            marker="o", markersize=4, label="Egoístas")
 
    ax.set_title("Evolución de la Población por Turno",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Turno", fontsize=11)
    ax.set_ylabel("Cantidad de individuos", fontsize=11)
    ax.legend(fontsize=10)
    plt.tight_layout()
 
    plt.savefig("graficos/1_poblacion_por_turno.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/1_poblacion_por_turno.png")
 

#  GRÁFICO 2 — Torta final:
 
def grafico_2_torta_final(df):
    """
    Gráfico de torta que muestra el porcentaje de altruistas y egoístas
    al final de la simulación (último turno).
 
    Toma la última fila del DataFrame (último turno) y lee directamente
    cant_altruistas y cant_egoistas para armar las porciones de la torta.
    """
    ultima_fila = df.iloc[-1]  # última fila = último turno
 
    conteo = {
        "altruista": int(ultima_fila["cant_altruistas"]),
        "egoista":   int(ultima_fila["cant_egoistas"])
    }
    _grafico_torta(
        conteo,
        titulo="Distribución Final de la Población",
        nombre_archivo="graficos/2_torta_final.png"
    )
    print("Gráfico guardado: graficos/2_torta_final.png")
 

#  GRÁFICO 3 — Torta inicial:
 
def grafico_3_torta_inicial(df):
    """
    Gráfico de torta que muestra el porcentaje de altruistas y egoístas
    al inicio de la simulación (primer turno).
 
    Igual que grafico_2 pero tomando la primera fila del DataFrame.
    Sirve para comparar visualmente cómo cambió la distribución.
    """
    primera_fila = df.iloc[0]  # primera fila = primer turno
 
    conteo = {
        "altruista": int(primera_fila["cant_altruistas"]),
        "egoista":   int(primera_fila["cant_egoistas"])
    }
    _grafico_torta(
        conteo,
        titulo="Distribución Inicial de la Población",
        nombre_archivo="graficos/3_torta_inicial.png"
    )
    print("Gráfico guardado: graficos/3_torta_inicial.png")
 
 
def _grafico_torta(conteo, titulo, nombre_archivo):
    """
    Función interna reutilizable para gráficos de torta.
    La usan grafico_2 y grafico_3 para no repetir código.
 
    Recibe un diccionario {condicion: cantidad}, arma los colores
    dinámicamente (azul para altruistas, rojo para egoístas),
    y guarda el gráfico.
 
    autopct="%1.1f%%" muestra el porcentaje con un decimal dentro de cada porción.
    startangle=90 hace que la torta empiece desde arriba.
    wedgeprops con edgecolor blanco separa visualmente las porciones.
    """
    etiquetas = list(conteo.keys())
    valores   = list(conteo.values())
    colores   = [
        COLOR_ALTRUISTA if e == "altruista" else COLOR_EGOISTA
        for e in etiquetas
    ]
 
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        valores,
        labels=[e.capitalize() for e in etiquetas],
        colors=colores,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    ax.set_title(titulo, fontsize=13, fontweight="bold", pad=15)
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=300)
    plt.close()
 

#  GRÁFICO 4 — Interacciones por tipo (barras):
 
def grafico_4_interacciones_por_tipo(df):
    """
    Gráfico de barras con cuatro barras: AA, AE, EE y Parientes.
    Muestra cuántas veces ocurrió cada tipo de interacción
    durante TODA la simulación (suma de todos los turnos).
 
    Las cuatro barras son:
      - AA        → dos altruistas sin parentesco
      - AE        → altruista con egoísta (sin parentesco)
      - EE        → dos egoístas sin parentesco
      - Parientes → cualquier combinación donde los dos tienen el mismo ID
                    (puede ser AA, EE o AE pero son parientes)
 
    Como el DataFrame tiene una columna por tipo de interacción y una fila
    por turno, se suman todas las filas con .sum() para obtener el total
    acumulado de cada tipo durante toda la simulación.
 
    Encima de cada barra se muestra el número exacto con ax.text().
    """
    # Suma acumulada de cada tipo de interacción en todos los turnos
    total_AA        = int(df["cant_interacciones_AA"].sum())
    total_AE        = int(df["cant_interacciones_EA"].sum())  # EA y AE es lo mismo
    total_EE        = int(df["cant_interacciones_EE"].sum())
    total_parientes = int(df["cant_interacciones_parientes"].sum())
 
    etiquetas = ["AA", "AE", "EE", "Parientes"]
    valores   = [total_AA, total_AE, total_EE, total_parientes]
    # AA → azul, AE → púrpura (mezcla), EE → rojo, Parientes → verde
    colores   = [COLOR_ALTRUISTA, "#8e44ad", COLOR_EGOISTA, "#27ae60"]
 
    fig, ax = plt.subplots(figsize=(9, 5))
    barras = ax.bar(etiquetas, valores,
                    color=colores, edgecolor="white",
                    linewidth=1.2, alpha=0.85)
 
    # Agrega el número exacto encima de cada barra
    for barra in barras:
        altura = barra.get_height()
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.5,
            str(int(altura)),
            ha="center", va="bottom", fontsize=10
        )
 
    ax.set_title("Cantidad de Interacciones por Tipo (total simulación)",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Tipo de interacción", fontsize=11)
    ax.set_ylabel("Cantidad", fontsize=11)
    plt.tight_layout()
 
    plt.savefig("graficos/4_interacciones_por_tipo.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/4_interacciones_por_tipo.png")
 

#  GRÁFICO 5 — Recursos promedio final (barras):
 
def grafico_5_recursos_promedio_final(df):
    """
    Gráfico de barras con dos barras: una para altruistas y una para egoístas.
    Muestra el promedio de recursos por individuo de cada condición
    al final de la simulación (último turno).
 
    El promedio se calcula acá directamente dividiendo los recursos totales
    de cada condición por la cantidad de personas de esa condición en el
    último turno:
        promedio_A = recursos_totales_A / cant_altruistas  (último turno)
        promedio_E = recursos_totales_E / cant_egoistas    (último turno)
 
    Para evitar división por cero (si una condición se extinguió), se verifica
    que cant_altruistas y cant_egoistas sean mayores a 0 antes de dividir.
    Si alguna condición tiene 0 individuos, su promedio se muestra como 0.
 
    El DataFrame necesita las columnas 'recursos_totales_A' y 'recursos_totales_E'
    que agrega el grupo en la parte de simulación.
 
    Encima de cada barra se muestra el valor con un decimal.
    """
    # Verificar que existan las columnas de recursos totales
    if "recursos_promedio_A" not in df.columns or "recursos_promedio_E" not in df.columns:
        print("Gráfico 5 omitido: el DataFrame necesita columnas "
              "'recursos_totales_A' y 'recursos_totales_E'.")
        return
 
    ultima_fila = df.iloc[-1]
 
    # Calcular promedio evitando división por cero
    cant_A = int(ultima_fila["cant_altruistas"])
    cant_E = int(ultima_fila["cant_egoistas"])
    promedio_A = float(ultima_fila["recursos_promedio_A"]) / cant_A if cant_A > 0 else 0
    promedio_E = float(ultima_fila["recursos_promedio_E"]) / cant_E if cant_E > 0 else 0
 
    etiquetas = ["Altruista", "Egoísta"]
    valores   = [promedio_A, promedio_E]
    colores   = [COLOR_ALTRUISTA, COLOR_EGOISTA]
 
    fig, ax = plt.subplots(figsize=(7, 5))
    barras = ax.bar(etiquetas, valores,
                    color=colores, edgecolor="white",
                    linewidth=1.2, alpha=0.85, width=0.5)
 
    for barra in barras:
        altura = barra.get_height()
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.3,
            f"{altura:.1f}",
            ha="center", va="bottom", fontsize=11
        )
 
    ax.set_title("Recursos Promedio por Condición al Final",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Condición", fontsize=11)
    ax.set_ylabel("Recursos promedio", fontsize=11)
    plt.tight_layout()
 
    plt.savefig("graficos/5_recursos_promedio_final.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/5_recursos_promedio_final.png")
 

#  GRÁFICO 6 — Reproducciones A vs E (barras):

def grafico_6_reproducciones(df):
    """
    Gráfico de barras con dos barras: una para altruistas y una para egoístas.
    Muestra el TOTAL de reproducciones de cada condición durante toda
    la simulación (suma de todos los turnos).
 
    Como el DataFrame tiene cant_reproducciones_A y cant_reproducciones_E
    con una fila por turno, se suman todas las filas con .sum() para
    obtener el acumulado total de cada condición.
 
    Encima de cada barra se muestra el número exacto.
    """
    total_repro_A = int(df["cant_reproducciones_A"].sum())
    total_repro_E = int(df["cant_reproducciones_E"].sum())
 
    etiquetas = ["Altruistas", "Egoístas"]
    valores   = [total_repro_A, total_repro_E]
    colores   = [COLOR_ALTRUISTA, COLOR_EGOISTA]
 
    fig, ax = plt.subplots(figsize=(7, 5))
    barras = ax.bar(etiquetas, valores,
                    color=colores, edgecolor="white",
                    linewidth=1.2, alpha=0.85, width=0.5)
 
    for barra in barras:
        altura = barra.get_height()
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.3,
            str(int(altura)),
            ha="center", va="bottom", fontsize=11
        )
 
    ax.set_title("Total de Reproducciones por Condición",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Condición", fontsize=11)
    ax.set_ylabel("Cantidad de reproducciones", fontsize=11)
    plt.tight_layout()
 
    plt.savefig("graficos/6_reproducciones.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/6_reproducciones.png")
 

#  GRÁFICO 7 — Muertes A vs E (barras):
 
def grafico_7_muertes(df):
    """
    Gráfico de barras con dos barras: una para altruistas y una para egoístas.
    Muestra el TOTAL de muertes de cada condición durante toda la simulación.
 
    Las muertes se calculan a partir del DataFrame: la diferencia entre
    la cantidad de personas de un turno y el siguiente, descontando
    las reproducciones de ese turno. Fórmula por turno:
        muertes_A = cant_altruistas[t] - cant_altruistas[t+1] + cant_reproducciones_A[t]
        muertes_E = cant_egoistas[t]   - cant_egoistas[t+1]   + cant_reproducciones_E[t]
 
    Se usa diff() con shift() para calcular las diferencias entre turnos consecutivos.
    Los valores negativos (cuando la población crece) se reemplazan por 0 con clip().
    Finalmente se suman todos los turnos para obtener el total acumulado.
    """
    # Diferencia de población entre turnos consecutivos (valor positivo = bajó)
    diff_A = df["cant_altruistas"].diff(-1).fillna(0)  # turno t - turno t+1
    diff_E = df["cant_egoistas"].diff(-1).fillna(0)
 
    # Muertes = bajada de población + reproducciones de ese turno
    # (si hubo reproducciones pero igual bajó la población, hubo más muertes que lo visible)
    muertes_A_por_turno = (diff_A + df["cant_reproducciones_A"]).clip(lower=0)
    muertes_E_por_turno = (diff_E + df["cant_reproducciones_E"]).clip(lower=0)
 
    total_muertes_A = int(muertes_A_por_turno.sum())
    total_muertes_E = int(muertes_E_por_turno.sum())
 
    etiquetas = ["Altruistas", "Egoístas"]
    valores   = [total_muertes_A, total_muertes_E]
    colores   = [COLOR_ALTRUISTA, COLOR_EGOISTA]
 
    fig, ax = plt.subplots(figsize=(7, 5))
    barras = ax.bar(etiquetas, valores,
                    color=colores, edgecolor="white",
                    linewidth=1.2, alpha=0.85, width=0.5)
 
    for barra in barras:
        altura = barra.get_height()
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.3,
            str(int(altura)),
            ha="center", va="bottom", fontsize=11
        )
 
    ax.set_title("Total de Muertes por Condición",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Condición", fontsize=11)
    ax.set_ylabel("Cantidad de muertes", fontsize=11)
    plt.tight_layout()
 
    plt.savefig("graficos/7_muertes.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/7_muertes.png")
 

generar_graficos(poblacion.datos)


            
            
                    
                    
                    
            
        
        
