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
        self.datos = pd.DataFrame( columns = ["turno" , "cant_egoistas" , "cant_altruistas" , "cant_interacciones_EE", "cant_interacciones_EA" , "cant_interacciones_AA" , "cant_reproducciones" , "total_personas"])
        
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
        
        #falta registrar la info que despues hay q agregar al dataframe
        ''' 
        
        if len(self.personas) %2 == 0: 
            lista_emparejamientos = self.personas
            for persona in lista_emparejamientos: 
                indice_pareja = random.randint(0, len(lista_emparejamientos))
                pareja = lista_emparejamientos[indice_pareja]
                if (persona.egoista == True and pareja.egoista == False): 
                    persona.recursos += 5 #hay que definir valor definitivo
                    pareja.recursos -= 5
                elif persona.egoista == False and pareja.egoista == True: 
                    persona.recursos -= 5
                    pareja.recursos += 5
                elif persona.egoista == False and pareja.egoista == False: 
                    persona.recursos += 1
                    pareja.recursos +=1
                    #hacemos que si son parientes suman mas??
                elif (persona.egoista == True and pareja.egoista == True) and (persona.id == pareja.id): 
                    #esto es si los dos egoistas son parientes
                    persona.recursos +=1
                    pareja.recursos +=1
                lista_emparejamientos.pop(indice_pareja)
                lista_emparejamientos.remove(persona)
        
        elif len(self.personas) %2 != 0: 
            lista_emparejamientos = self.personas
            indice_excluido = random.randint(0, len(lista_emparejamientos))
            lista_emparejamientos.pop(indice_excluido)
            for persona in lista_emparejamientos: 
                indice_pareja = random.randint(0, len(lista_emparejamientos))
                pareja = lista_emparejamientos[indice_pareja]
                if (persona.egoista == True and pareja.egoista == False): 
                    persona.recursos += 5 #hay que definir valor definitivo
                    pareja.recursos -= 5
                elif persona.egoista == False and pareja.egoista == True: 
                    persona.recursos -= 5
                    pareja.recursos += 5
                elif persona.egoista == False and pareja.egoista == False: 
                    persona.recursos += 1
                    pareja.recursos +=1
                    #hacemos que si son parientes suman mas??
                elif (persona.egoista == True and pareja.egoista == True) and (persona.id == pareja.id): 
                    #esto es si los dos egoistas son parientes
                    persona.recursos +=1
                    pareja.recursos +=1
                lista_emparejamientos.pop(indice_pareja)
                lista_emparejamientos.remove(persona)

    def filtrar_poblacion(self): 
        '''
        filtra a las personas de la lista si se mueren o si se reproducen agrega otra
        cambia la lista del atributo de personas. 
        '''
        
        for persona in self.personas: 
            if persona.recursos <= 0: 
                self.muerte(persona)
            if persona.recursos > 50: 
                hijo = persona.reproduccion(persona)
                self.agregar_personas(hijo)
                persona.recursos -= 50
                
    def simulacion(self, rondas):
        '''
        genera simulacion
        paramentros: 
            rondas: int --> numero de rondas ingresado por el ususario
        '''
        
        for ronda in range(rondas): 
            self.ronda_interaccion()
            self.filtrar_poblacion()
    
        
                
            
            
                
            
                    
                    
                    
            
        
        
