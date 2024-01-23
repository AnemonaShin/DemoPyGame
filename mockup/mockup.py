import pyautogui, random, time

# REVISAR ERROR DE ACOMULACION

gui = pyautogui
randomA = 1

def __strtValue__(randomB):
    n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
    n2 = random.randint(randomA, randomB) #Segundo valor random.
    
    return n1, n2

def __start__():
    gui.alert(text='¡Bienvenido al mundo de las matematicas!', title='Bienvenida')
    
    try:
        control = gui.confirm(text='¿Que deseas hacer hoy?', title='Eleccion', buttons=['Sumar', 'Restar','Multiplicar', 'Dividir'])
    except:
        control = 'none'
    return control

def __dificultad__(dControl):
    match dControl:
        case 'Facil':
            randomB = 10
            coninueCounter = 20
            puntos = 1
            failCounters = 10
            return randomB, coninueCounter, puntos, failCounters
        case 'Normal':
            randomB = 100
            coninueCounter = 10
            failCounters = 5
            puntos = 2
            return randomB, coninueCounter, puntos, failCounters
        case 'Dificil':
            randomB = 1000
            coninueCounter = 5
            failCounters = 3
            puntos = 5
            return randomB, coninueCounter, puntos, failCounters
        case 'Extremo':
            randomB = 10000
            coninueCounter = 3
            failCounters = 1
            puntos = 10
            return randomB, coninueCounter, puntos, failCounters
        case _:
            gui.alert(text='Opcion no encontrada... pero... ¡EXTREMO!', title='¡404!')
            randomB = 100000
            coninueCounter = 1
            failCounters = 0
            puntos = 1000
            return randomB, coninueCounter, puntos, failCounters

def __siguiente__():
    control = gui.confirm(text='¿Que deseas hacer?', title='Eleccion', buttons=['Sumar', 'Restar','Multiplicar', 'Dividir' ])

    return control

def __control__(control):    
    match control:
        case 'Sumar':
            try:
                dControl = gui.confirm(text='¿En que dificultad?', title='Eleccion', buttons=['Facil', 'Normal','Dificil', 'Extremo'])
            except:  
                dControl = 'Extremo'
            randomB, continueCounter, puntos, failCounters = __dificultad__(dControl)
            n1, n2 = __strtValue__(randomB)

            return __suma__(n1, n2, randomB, continueCounter, puntos, failCounters)
        case 'Restar':
            try:
                dControl = gui.confirm(text='¿En que dificultad?', title='Eleccion', buttons=['Facil', 'Normal','Dificil', 'Extremo'])
            except:  
                dControl = 'Extremo'
            randomB, continueCounter, puntos, failCounters = __dificultad__(dControl)
            n1, n2 = __strtValue__(randomB)

            return __resta__(n1, n2, randomB, continueCounter, puntos, failCounters)
        case 'Dividir':
            try:
                dControl = gui.confirm(text='¿En que dificultad?', title='Eleccion', buttons=['Facil', 'Normal'])
            except:  
                dControl = 'Extremo'
            randomB, continueCounter, puntos, failCounters = __dificultad__(dControl)
            n1, n2 = __strtValue__(randomB)
            
            return __divicion__(n1, n2, randomB, continueCounter, puntos, failCounters)
        case 'Multiplicar':
            try:
                dControl = gui.confirm(text='¿En que dificultad?', title='Eleccion', buttons=['Facil', 'Normal'])
            except:  
                dControl = 'Extremo'
            randomB, continueCounter, puntos, failCounters = __dificultad__(dControl)
            n1, n2 = __strtValue__(randomB)
            
            return __multiplicacion__(n1, n2, randomB, continueCounter, puntos, failCounters)
        case _:
            gui.alert(text='Opcion no encontrada...', title='404')
            n1, n2 = __strtValue__(1000000000)
            return __multiplicacion__(n1, n2, 1000000000, 1000, 0, 0)

def __suma__(n1, n2, randomB, continueCounter, puntos, failCounters):    
    puntosTotales = 0
        
    gui.alert(text='¡Empecemos a sumar!', title='Suma')
    gui.alert(text='¡Tienes '+str(continueCounter)+' preguntas!', title='Preguntas')
    gui.alert(text='¡Tienes '+str(failCounters)+' fallos posibles!', title='Oportunidades')

    while True:        
        respuesta = n1 + n2
        
        if continueCounter == 0 :
            gui.alert(text='¡Completaste el circuito!', title='¡Felicidades!')
            gui.alert(text='¡Felicidades!', title='¡Felicidades!')
            return puntosTotales, True
        else: 
            
            try:
                respuestaUsuario = int(gui.prompt(text=str(n1)+' + '+str(n2), title='¿Cuanto es?'))
            except:
                respuestaUsuario = 'none'    
        
            if respuesta == respuestaUsuario:
                puntosTotales += 1
                
                gui.alert(text='¡Bien hecho! ¡Has ganado '+ str(puntos)+' P!', title='¡Felicidades!')

                n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
                n2 = random.randint(randomA, randomB) #Segundo valor random.
            elif respuestaUsuario == 'none' or respuesta != respuestaUsuario:
                if failCounters == 0:
                    gui.alert(text='¡Lo lamento pero pierdes!', title='Pierdes')
                    break
                else:
                    failCounters -= 1
                    gui.alert(text='Es incorrecto... ¡Intentemos denuevo! Oportunidades = '+str(failCounters), title='Incorrecto')                    
            else:
                gui.alert(text='ERROR INESPERADO', title='500')

            continueCounter -= 1
    return puntosTotales, False
    
def __resta__(n1, n2, randomB, continueCounter, puntos, failCounters):
    puntosTotales = 0
        
    gui.alert(text='¡Empecemos a restar!', title='Resta')
    gui.alert(text='¡Tienes '+str(continueCounter)+' preguntas!', title='Preguntas')
    gui.alert(text='¡Tienes '+str(failCounters)+' fallos posibles!', title='Oportunidades')

    
    while True:        
        if (n1 > n2):
            msg = str(n1) + ' - ' + str(n2)
            respuesta = n1 - n2
        elif (n1 < n2):
            msg = str(n2) + ' - ' + str(n1)
            respuesta = n2 - n1
        elif (n1 == n2):
            msg = str(n1) + ' - ' + str(n2)
            respuesta = n1 - n2
        else:
            return 0
        
        if continueCounter == 0 :
            gui.alert(text='¡Completaste el circuito!', title='¡Felicidades!')
            gui.alert(text='¡Felicidades!', title='¡Felicidades!')
            return puntosTotales, True
        else: 
            
            try:
                respuestaUsuario = int(gui.prompt(text=msg, title='¿Cuanto es?'))
            except:
                respuestaUsuario = 'none'    
        
            if respuesta == respuestaUsuario:
                puntosTotales += 1
                
                gui.alert(text='¡Bien hecho! ¡Has ganado '+ str(puntos)+' P!', title='¡Felicidades!')

                n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
                n2 = random.randint(randomA, randomB) #Segundo valor random.
            elif respuestaUsuario == 'none' or respuesta != respuestaUsuario:
                if failCounters == 0:
                    gui.alert(text='¡Lo lamento pero pierdes!', title='Pierdes')
                    break
                else:
                    failCounters -= 1
                    gui.alert(text='Es incorrecto... ¡Intentemos denuevo! Oportunidades = '+str(failCounters), title='Incorrecto')                    
            else:
                gui.alert(text='ERROR INESPERADO', title='500')

            continueCounter -= 1
    return puntosTotales, False
    
def __divicion__(n1, n2, randomB, continueCounter, puntos, failCounters):
    
    gui.alert(text='Opcion aun no implementada', title=':C')
    
    return 0, False
    
def __multiplicacion__(n1, n2, randomB, continueCounter, puntos, failCounters):
    puntosTotales = 0
    
    gui.alert(text='¡Empecemos a multiplicar!', title='Multiplicacion')
    gui.alert(text='¡Tienes '+str(continueCounter)+' preguntas!', title='Preguntas')
    gui.alert(text='¡Tienes '+str(failCounters)+' fallos posibles!', title='Oportunidades')

    
    while True:       
                
        #if (n1 > 10 and n2 <= 100):
        #    msg = str(n1) + ' x ' + str(n2)
        #    respuesta = n1 * n2
        #elif (n2 > 10 and n1 <= 100):
        #    msg = str(n2) + ' x ' + str(n1)
        #    respuesta = n2 * n1
        #else:
        msg = str(n1) + ' x ' + str(n2)
        respuesta = n1 * n2
        
        if continueCounter == 0:
            gui.alert(text='¡Completaste el circuito!', title='¡Felicidades!')
            gui.alert(text='¡Felicidades!', title='¡Felicidades!')
            return puntosTotales, True
        else: 
            
            try:
                respuestaUsuario = int(gui.prompt(text=msg, title='¿Cuanto es?'))
            except:
                respuestaUsuario = 'none'    
        
            if respuesta == respuestaUsuario:
                puntosTotales += 1
                
                gui.alert(text='¡Bien hecho! ¡Has ganado '+ str(puntos)+' P!', title='¡Felicidades!')
                
                n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
                n2 = random.randint(randomA, randomB) #Segundo valor random.
            elif respuestaUsuario == 'none' or respuesta != respuestaUsuario:
                if failCounters == 0:
                    gui.alert(text='¡Lo lamento pero pierdes!', title='Pierdes')
                    break
                else:
                    failCounters -= 1
                    gui.alert(text='Es incorrecto... ¡Intentemos denuevo! Oportunidades = '+str(failCounters), title='Incorrecto')                    
            else:
                gui.alert(text='ERROR INESPERADO', title='500')

            continueCounter -= 1
    return puntosTotales, False

def __gmp__(control):
    try:
        controlIn = "Si"
        continueB = True
        puntosJugador = 0
        
        while True: #Controlador de actividad.
           
           if (controlIn == 'Si'):
                puntosTotales, continueB = __control__(control)
                puntosTotales += puntosJugador
                puntosJugador = puntosTotales

                if (control == None):
                    break
                elif continueB == False:
                    controlIn = gui.confirm(text='¿Continuar?', title='Eleccion', buttons=['Si', 'No'])
                    if controlIn == 'Si':
                        continueB = True
                        control= __siguiente__()
                    else:
                        break
                else:
                    gui.alert(text='¡Felicidades has logrado conseguir '+str(puntosTotales)+' puntos!', title= 'Puntaje')
                    
                    controlInIn = gui.confirm(text='¿Quieres '+ str(control) +' nuevamente?', title='Eleccion', buttons=['Si', 'No'])
                    if controlInIn == 'No':
                        controlIn = gui.confirm(text='¿Continuar?', title='Eleccion', buttons=['Si', 'No'])
                        if controlIn == 'Si':
                            control= __siguiente__()
                        else:
                            break
                    elif controlInIn == None:
                        break
           else:
               break
                        
        gui.alert(text='¡Que tengas un hermoso dia!', title='¡Adios!')   
    except KeyboardInterrupt: #Activador de salida desde consola.
        print('\n')
    #except:
    #    print('')


def App():
    __gmp__(__start__())

App()