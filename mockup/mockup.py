import pyautogui, random, time

gui = pyautogui
randomA = 1
randomB = 10
n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
n2 = random.randint(randomA, randomB) #Segundo valor random.
continueA = True

def __start__():
    gui.alert(text='¡Bienvenido al mundo de las matematicas!', title='Bienvenida')
    
    try:
        control = gui.confirm(text='¿Que deseas hacer hoy?', title='Eleccion', buttons=['Sumar', 'Restar', 'Dividir', 'Multiplicar'])
    except:
        control = 'a'
    
    return control

def __siguiente__():
    control = gui.confirm(text='¿Que deseas hacer?', title='Eleccion', buttons=['Sumar', 'Restar', 'Dividir', 'Multiplicar'])
    return control

def __control__(control, n1, n2, continueA):
    match control:
        case 'Sumar':
            return __suma__(n1, n2, continueA)
        case 'Restar':
            return __resta__(n1, n2, continueA)
        case 'Dividir':
            return __divicion__(n1, n2, continueA)
        case 'Multiplicar:':
            return __multiplicacion__(n1, n2, continueA)
        case _:
            gui.alert(text='Opcion no encontrada...', title='404')
            return 0

def __suma__(n1, n2, continueA):
    puntos = 0
    continueCounter = 10
        
    gui.alert(text='Así que deseas sumar...', title='Suma')
    
    while continueA == True:
        print(continueCounter)
        
        respuesta = n1 + n2
        
        if continueCounter == 0 :
            return puntos
        else: 
            
            try:
                respuestaUsuario = int(gui.prompt(text=str(n1)+' + '+str(n2), title='¿Cuanto es?'))
            except:
                respuestaUsuario = 'none'    
        
            if respuesta == respuestaUsuario:
                puntos += 1
                
                gui.alert(text='¡Bien hecho!', title='¡Felicidades!')
                gui.alert(text='¡Continuemos!', title='Continuar')
            
                n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
                n2 = random.randint(randomA, randomB) #Segundo valor random.
            elif respuestaUsuario == 'none':
                break
            else:
                gui.alert(text='Es incorrecto... ¡Intentemos denuevo!', title='Incorrecto')
            continueCounter -= 1
    return puntos
    
def __resta__(n1, n2, continueA):
    puntos = 0
    continueCounter = 10
        
    gui.alert(text='Así que deseas restar...', title='Resta')
    
    while continueA == True:
        print(continueCounter)
        
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
            return puntos
        else: 
            
            try:
                respuestaUsuario = int(gui.prompt(text=msg, title='¿Cuanto es?'))
            except:
                respuestaUsuario = 'none'    
        
            if respuesta == respuestaUsuario:
                puntos += 1
                
                gui.alert(text='¡Bien hecho!', title='¡Felicidades!')
                gui.alert(text='¡Continuemos!', title='Continuar')
            
                n1 = random.randint(randomA, randomB) #Valores random enteros desde punto A a punto B
                n2 = random.randint(randomA, randomB) #Segundo valor random.
            elif respuestaUsuario == 'none':
                break
            else:
                gui.alert(text='Es incorrecto... ¡Intentemos denuevo!', title='Incorrecto')
            continueCounter -= 1
    return puntos
    
    
    
def __divicion__(n1, n2, continueA):
    print("")
    return 0
    
def __multiplicacion__(n1, n2, continueA):
    print("")
    return 0

def __gmp__(control):
    try:
        controlIn = "Ok"
        continueB = True
        puntos = 0
        
        while continueB == True: #Controlador de actividad.
           
           if (controlIn == 'Ok'): 
                puntos += __control__(control, n1, n2, continueA)
                gui.alert(text='¡Felicidades tienes '+str(puntos)+' puntos!', title= 'Puntaje')
                controlInIn = gui.confirm(text='¿Continuar en '+ str(control) +' ?', title='Eleccion', buttons=['Si', 'No'])
                if controlInIn == 'No':
                    controlIn = gui.confirm(text='¿Continuar?', title='Eleccion', buttons=['Ok', 'Cancel'])
                    if controlIn == 'Ok':
                        control = __siguiente__()
           else:
                continueB = False

        gui.alert(text='¡Que estes super!', title='¡Adios!')   
    except KeyboardInterrupt: #Activador de salida desde consola.
        print('\n')    


def App():
    __gmp__(__start__())

App()