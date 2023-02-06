# Trabajo Práctico
# Autores: Abel Gutiérrez y Dayana Xie
# Menú principal del sistema bancario


def correr_menu_principal():
  '''
  Función principal para seleccionar el tipo de usuario que esté usando el sistema.
  No tiene parámetros.
  Return: Si el usuario es banquero se hace un llamado a la función correr_menu_banquero.
  Return: Si el usuario es cliente del banco se hace un llamado a la función correr_menu_usuario.
  Return: Si el usuario ingresa otro número que no está entre las opciones se hace un llamado recursivo.
  '''
  print('¡Bienvenido/a, gracias por elegir nuestro sistema bancario!')
  elegir_usuario_sistema = (input('''
  ¿Quién está usando el sistema?
  (1) Banquero 
  (2) Cliente del banco 

  '''))
  if(elegir_usuario_sistema == '1'):
    print('\n Usando el sistema: Banquero')
    return correr_menu_banquero()
  elif(elegir_usuario_sistema == "2"):
    print('\nUsando el sistema: Cliente del banco\n')
    return correr_menu_usuario()
  else:
    print('\n Sistema le informa: Por favor digite un número que esté entre las opciones')
    print('\n Volviendo al menú principal...\n')
    return correr_menu_principal()

def correr_menu_banquero():
  '''
  Función auxiliar del menú principal que posee las funcionalidades del banquero.
  No tiene parámetros.
  Return: Si el el banquero desea crear un cajero se hace llamado a la función crear_cajero()
  Return: Si el el banquero desea crear un usuario del banco se hace llamado a la función crear_usuario()
  Return: Si el banquero ingresa otro número que no está entre las opciones se hace un llamado recursivo.
  '''
  elegir_accion_banquero = (input(
  '''
  Digite el número de la acción a realizar:
  (1) Crear Cajero
  (2) Crear Usuario
  (3) Agregar Billetes a un cajero existente \n
  '''))
  if(elegir_accion_banquero == '1'):
    from Banquero import crear_cajero
    print('\n Acción a realizar: Crear Cajero')
    return crear_cajero()
  elif(elegir_accion_banquero == '2'):
    from Banquero import crear_usuario
    print('\n Acción a realizar: Crear Usuario')
    return crear_usuario()
  elif(elegir_accion_banquero == '3'):
    print('\n Acción a realizar: Agregar Billetes a un cajero existente')
    from Banquero import agregar_billetes_cajero_existente
    return agregar_billetes_cajero_existente()
  else:
    print('\n Sistema le informa: Por favor digite un número que esté entre las opciones')
    print('\n Regresando al menú principal...\n')
    return correr_menu_banquero

def correr_menu_usuario():
  '''
  Función auxiliar del menú principal encargado de hacer llamado a otras funciones para mostrar los cajeros disponibles,
  para que el usuario elija cuál usar.
  No tiene parámetros.
  No tiene retornos.
  '''
  print('-Lista de cajeros disponibles-')
  # se llama a la función para imprimir los cajeros disponibles
  # se envía un cero como posición inicial a verificar en el archivo
  cargar_datos_cajero(0)

def cargar_datos_cajero(linea_de_texto_cajero):
    """
    Función encargada de abrir el archivo de los cajeros y cargar los datos.
    Parámetro linea_de_texto_cajero: es la posición de la linea a leer en el archivo.
    Return: se devuelve la hilera de texto del archivo.
    """ 
    archivo_cajeros_lectura  = open('Lista_de_cajeros.txt', 'r')
    lineas_cajeros = archivo_cajeros_lectura.readlines()  
    archivo_cajeros_lectura.close
    if linea_de_texto_cajero <= (len(lineas_cajeros) -1):
      linea_cajero = lineas_cajeros[linea_de_texto_cajero]
      linea_cajero = linea_cajero.replace("'", "")
      linea_cajero = linea_cajero.replace("\n", "")
      linea_cajero = linea_cajero.replace("[", "")
      linea_cajero = linea_cajero.replace("]", "")
      lista_hileras_cajero = linea_cajero.split(",")
      return mostrar_cajeros_disponibles(lista_hileras_cajero, linea_de_texto_cajero)

    
def mostrar_cajeros_disponibles(lista_hileras_cajero, linea_de_texto_cajero):
  """"
  Función encargada de mostrar los cajeros disponibles 
  lista_hileras_cajero: lista de hileras representando la informacion de un cajero o un usuario
  diccionario: diccionario donde se construye el resultado
  elemento_actual: elemento actual en la lista de hileras (se aumenta cada 2)
  return: diccionario correspondiente a la lista de hileras
  """
  if(linea_de_texto_cajero <= (len(lista_hileras_cajero)-1)):
    # la posición del identificador del cajero siempre es la misma
    cajeros_disponibles = lista_hileras_cajero[1]
    archivo_cajeros_disponibles_escritura = open("Cajeros_disponibles.txt", "a")
    archivo_cajeros_disponibles_escritura.write(cajeros_disponibles + ',')
    archivo_cajeros_disponibles_escritura.close()
    archivo_cajeros_disponibles_lectura = open("Cajeros_disponibles.txt", "r")
    print('Cajero disponible:', cajeros_disponibles)
    lineas_archivo_cajeros_disponibles = archivo_cajeros_disponibles_lectura.read()
    archivo_cajeros_disponibles_lectura.close()
    return cargar_datos_cajero(linea_de_texto_cajero +1), elegir_cajero(lineas_archivo_cajeros_disponibles)


def elegir_cajero(lineas_archivo_cajeros_disponibles):
  """"
  Función auxiliar del menú de usuarios para que el cliente elija cual cajero usar.
  Parámetro lineas_archivo_cajeros_disponibles: lineas del archivo que contiene los cajeros disponibles.
  Return: se hace llamado a la funcion revisar_lineas para verificar que el cajero seleccionado exista y sea correcto.
  """
  cajero_seleccionado = input('\nEstimado usuario, por favor seleccione el cajero que desea utilzar: ')
  return revisar_lineas(cajero_seleccionado, 0, lineas_archivo_cajeros_disponibles)

def revisar_lineas(cajero_seleccionado, revisando_linea, lineas_archivo_cajeros_disponibles):
  """"
  Función auxiliar del menú de usuarios para verificar que el cajero seleccionado exista y sea correcto.
  Parámetro cajero_seleccionado: cajero seleccionado por el usuario.
  Parámetro revisando_linea: inicializado en cero para ir revisando todas las lineas del archivo.
  Parámetro lineas_archivo_cajeros_disponibles: hileras del archivo de los cajeros disponibles.
  Return: si se encuentra el cajero seleccionado se corre el menu de las acciones del usuario.
  Return: si no se encuentra en la línea actual se sigue con la linea siguiente. Es el llamado recursivo.
  Return si no se encuentra del todo, se hace llamado a la función para que escoja un cajero que exista.
  """
  archivo_cajeros_lectura = open('Lista_de_cajeros.txt', 'r')
  lectura_lineas_cajeros = archivo_cajeros_lectura.readlines()  
  # la linea siendo revisada no puede sobrepasar el largo del archivo 
  if revisando_linea <= (len(lectura_lineas_cajeros) -1):
    if cajero_seleccionado in lineas_archivo_cajeros_disponibles and len(cajero_seleccionado) >= 4:
      return correr_menu_usuario_aux(cajero_seleccionado)
    else:
      revisando_linea += 1
      return revisar_lineas(cajero_seleccionado, revisando_linea, lineas_archivo_cajeros_disponibles)
  else:
    print('Sistema le informa: "Estimado usuario, por favor seleccione un cajero que esté disponible"')
    return elegir_cajero(lineas_archivo_cajeros_disponibles)

def correr_menu_usuario_aux(cajero_seleccionado):
  """"
  Función auxiliar del menú de usuarios encargado de pedir el nombre de usuario y pin.
  Parámetro cajero_seleccionado: cajero seleccionado por el usuario.
  Return: si el nombre de usuario y el pin son correctos se llama a la función con las acciones del usuario.
  Return si el nombre de usuario o el pin está incorrecto se hace el llamado recursivo.
  """
  usuario_usando_el_sistema = input('Por favor digite su nombre de usuario: ')
  leer_base_de_datos_banquero = open("Lista_de_usuarios.txt", "r")  # se lee el archivo
  lectura_base_datos = leer_base_de_datos_banquero.read()
  leer_base_de_datos_banquero.close()
  # se verifica que el nombre de usuario esté correcto y exista
  if(usuario_usando_el_sistema in lectura_base_datos and (len(usuario_usando_el_sistema) >= 7)):
    pin_del_usuario = input('Por favor digite su pin: ')
    # se verifica que el pin esté correcto
    if(pin_del_usuario in lectura_base_datos and (len(pin_del_usuario) == 4)):
      return acciones_usuario(cajero_seleccionado, usuario_usando_el_sistema)
    else:
      # si el pin es incorrecto se le notifica al usuario y se vuelve al menu del usuario
      print('Sistema le informa: Pin incorrecto')
      return correr_menu_usuario_aux(cajero_seleccionado)
  else:
    print('Estimado usuario, por favor digite un usuario del banco existente')
    return correr_menu_usuario_aux(cajero_seleccionado)


def acciones_usuario(cajero_seleccionado, usuario_usando_el_sistema):
  """"
  Función auxiliar del menú de usuarios que el cliente elija la acción a realizar.
  Parámetro cajero_seleccionado: cajero seleccionado por el usuario.
  Parámetro usuario_usando_el_sistema: nombre del usuario usando el sistema.
  Return: si desea hacer un retiro se llama a la función retirar_dinero.
  Return: si desea hacer un depósito se llama a la función depositar_dinero.
  Return: si desea consultar su saldo se llama a la función consultar_saldo.
  Return: si desea ver su historial dde transacciones se llama a la función historial_transacciones.
  Return: si selecciona una opción no mostrada entonces se hace el llamado recursivo
  """
  elegir_accion_usuario = (input(
  '''
  Digite el número de la acción a realizar:
  (1) Retirar Dinero
  (2) Depositar Dinero
  (3) Consultar Saldo
  (4) Consultar Historial de Transacciones \n
  '''))
  if(elegir_accion_usuario == '1'):
    print('\n Acción a realizar: Retirar Dinero \n')
    from Cliente_del_banco import retirar_dinero
    return retirar_dinero(cajero_seleccionado, usuario_usando_el_sistema)
  if(elegir_accion_usuario == '2'):
    print('\n Acción a realizar: Depositar Dinero \n')
    from Cliente_del_banco import depositar_dinero
    return depositar_dinero(cajero_seleccionado, usuario_usando_el_sistema)
  if(elegir_accion_usuario == '3'):
    print('\n Acción a realizar: Consultar Saldo \n')
    from Cliente_del_banco import consultar_saldo
    return consultar_saldo(usuario_usando_el_sistema)
  if(elegir_accion_usuario == '4'):
    print('\n Acción a realizar: Consultar Historial de Transacciones \n')
    from Cliente_del_banco import historial_transacciones
    return historial_transacciones(usuario_usando_el_sistema)
  else:
    print('Estimado usuario, por favor seleccione una de las opciones disponibles')
    return correr_menu_usuario_aux(cajero_seleccionado)

correr_menu_principal()