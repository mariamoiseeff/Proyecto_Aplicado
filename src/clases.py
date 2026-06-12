#aca creo las clases de persona y poblacion

import random
import pandas as pd


class Persona:
    def __init__ (self, condicion, ID):
        '''
        inicializa un objeto persona.

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
             "cant_reproducciones_E" , "cant_reproducciones_A", "cant_muertes_E", "cant_muertes_A"]
            )
        
    def agregar_datos_turno(self, turno, interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes, reproducciones_E, reproducciones_A , muertes_E , muertes_A): 
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
        "cant_muertes_A": muertes_A 
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
        ''' 
        interacciones_EE = 0
        interacciones_EA = 0
        interacciones_AA = 0
        interacciones_parientes = 0
        
        lista_emparejamientos = self.personas.copy()
        
        #unifico codigo con par e inpar y corrigo proque de esa forma antes se salteaba personas de la lista
        
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
                
            elif persona.egoista == False and pareja.egoista == True: 
                persona.recursos -= 5
                pareja.recursos += 5
                interacciones_EA +=1
                
            elif persona.egoista == False and pareja.egoista == False: 
                interacciones_AA +=1
                if persona.id == pareja.id: #si los altruistas son parientes suman mas
                    interacciones_parientes +=1
                    persona.recursos +=2
                    pareja.recursos +=2
                else: 
                    persona.recursos += 1
                    pareja.recursos +=1
                    
            elif persona.egoista == True and pareja.egoista == True: 
                interacciones_EE +=1
                if  persona.id == pareja.id: #esto es si los dos egoistas son parientes
                    persona.recursos +=1
                    pareja.recursos +=1

        
        return interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes
  
  
    def filtrar_poblacion(self): 
        '''
        filtra a las personas de la lista si se mueren o si se reproducen agrega otra
        cambia la lista del atributo de personas. 
        
        returns: 
            repro
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
            interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes = self.ronda_interaccion()
            reproducciones_E, reproducciones_A, muertes_E, muertes_A = self.filtrar_poblacion()
            self.agregar_datos_turno(turno, interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes, reproducciones_E, reproducciones_A, muertes_E, muertes_A)
            if len(self.personas) == 0: 
                print(f"Termino la simulacion antes de tiempo porque la poblacion se quedo in personas. Duro {turno} rondas. ")
                break
        


p1 = Persona(True, 1)
Poblacion.agregar_personas(p1)
p2 = Persona(False, 1)
Poblacion.agregar_personas(p2)
p3 = Persona(False, 2)
Poblacion.agregar_personas(p3)
p4 = Persona(False, 3)
Poblacion.agregar_personas(p4)

Poblacion.simulacion(10)



            
            
                    
                    
                    
            
        
        
