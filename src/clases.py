#aca creo las clases de persona y poblacion

import random
import pandas as pd

#donde agrego esto?? nose si un metodo de poblacion o que sea una funcion aparte
'''
crear_personas (cant_altruistas_validada , cant_egoista_validada)
crea objetos de persona con condición
agrega (llamando al método de Población) a la lista de población
'''
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
            ValueError si la persona que se quiere eliminar no esta en la lista
        '''
        if persona not in self.personas: 
            raise ValueError("La persona que se esta queriendo eliminar de la poblacion no esta en la lista.")
       
        self.personas.remove(persona)
        
    def ronda_interaccion(self):
        '''
        empareja aleatoriamente dos personas de la población, y depende la condición de altruista/egoísta distribuye recursos. 
        
        ''' 
        interacciones_EE = 0
        interacciones_EA = 0
        interacciones_AA = 0
        interacciones_parientes = 0
        
        lista_emparejamientos = self.personas.copy()
        
        if len(self.personas) %2 == 0: 

            for persona in lista_emparejamientos: 
                lista_emparejamientos.remove(persona)
                indice_pareja = random.randint(0, len(lista_emparejamientos)-1)
                pareja = lista_emparejamientos[indice_pareja]
               
                if (persona.egoista == True and pareja.egoista == False): 
                    persona.recursos += 5 #hay que definir valor definitivo
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
                lista_emparejamientos.pop(indice_pareja)

        
        elif len(self.personas) %2 != 0: 
            lista_emparejamientos = self.personas
            indice_excluido = random.randint(0, len(lista_emparejamientos))
            lista_emparejamientos.pop(indice_excluido)
            
            for persona in lista_emparejamientos: 
                lista_emparejamientos.remove(persona)
                indice_pareja = random.randint(0, len(lista_emparejamientos)-1)
                pareja = lista_emparejamientos[indice_pareja]
                
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
                    if persona.id == pareja.id: 
                        interacciones_parientes +=1
                        persona.recursos +=2
                        pareja.recursos +=2
                    else: 
                        persona.recursos += 1
                        pareja.recursos +=1
                    
                    
                elif (persona.egoista == True and pareja.egoista == True): 
                    interacciones_EE +=1
                    if persona.id == pareja.id: 
                        persona.recursos +=1
                        pareja.recursos +=1
                        interacciones_parientes +=1
                
                lista_emparejamientos.pop(indice_pareja)
                lista_emparejamientos.remove(persona)
        
        return interacciones_EE, interacciones_EA, interacciones_AA, interacciones_parientes
    
    def filtrar_poblacion(self): 
        '''
        filtra a las personas de la lista si se mueren o si se reproducen agrega otra
        cambia la lista del atributo de personas. 
        '''
        reproducciones_E = 0
        reproducciones_A = 0
        muertes_E = 0
        muertes_A = 0
        
        for persona in self.personas: 
            if persona.recursos <= 0: 
                if persona.egoista == True: 
                    muertes_E =+1
                else: 
                    muertes_A +=1
                    
                self.muerte(persona)
                
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
            if len(self.pesonas) == 0: 
                print(f"Termino la simulacion antes de tiempo porque la poblacion se quedo in personas. Duro {turno} rondas. ")
                break
        

                
            
            
                    
                    
                    
            
        
        
