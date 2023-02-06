# Trabajo Práctico
# Autores: Abel Gutiérrez y Dayana Xie
# Funcionalidades a utilizar del cliente del banco

# se importa la librería que permitirá agregar la fecha y hora en el historial
import time

# Depositar dinero 
def depositar_dinero(cajero_seleccionado, usuario_usando_el_sistema):
  '''
  Función principal para depositar dinero en la cuenta del cliente.
  Parámetros: cajero el cual el usuario quiere hacer el depósito de su dinero y su nombre de 
  usuario para acceder a su cuenta.
  Return: se envían a la función la cantidad de biletes ingresados para sumarlo 
  '''
  enunciado_instrucciones = 'Por favor inserte la cantidad de billetes por denominación que desea depositar\n'
  print(enunciado_instrucciones)
  depositar_billetes_100 = (input('Introduzca la cantidad de billetes de 100 pesos\n'))
  verificar_entero(depositar_billetes_100)
  depositar_billetes_50 = (input('Introduzca la cantidad de billetes de 50 pesos\n'))
  verificar_entero(depositar_billetes_50)
  depositar_billetes_20 = (input('Introduzca la cantidad de billetes de 20 pesos\n'))
  verificar_entero(depositar_billetes_20)
  depositar_billetes_10 = (input('Introduzca la cantidad de billetes de 10 pesos\n'))
  verificar_entero(depositar_billetes_10)
  depositar_billetes_5 = (input('Introduzca la cantidad de billetes de 5 pesos\n'))
  verificar_entero(depositar_billetes_5)
  depositar_billetes_2 = (input('Introduzca la cantidad de billetes de 2 pesos\n'))
  verificar_entero(depositar_billetes_2)
  depositar_billetes_1 = (input('Introduzca la cantidad de billetes de 1 pesos\n'))
  verificar_entero(depositar_billetes_1)
  # se llama a la funciónn encargada de buscar la línea en donde se encuentra el cajero seleccionado
  actualizar_montos_cajeros(cajero_seleccionado, depositar_billetes_100, depositar_billetes_50, depositar_billetes_20, 
  depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1)

  # se llama a la función encargada de sumar la cantidad de billetes ingresados
  return sumar_monto_depositado(depositar_billetes_100, depositar_billetes_50, depositar_billetes_20, 
                                depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, 
                                depositar_billetes_1, cajero_seleccionado, usuario_usando_el_sistema)
  

def verificar_entero(cantidad_de_billetes_depositados):
  '''
  Función auxiliar para verificar que la entrada sea de tipo entero
  Parámetro: cantidad de billetes depositados por el usuario
  Return: se llama a la función depositar_dinero para volver a intentar depositar dinero.
  '''
  try: 
    cantidad_de_billetes_depositados = int(cantidad_de_billetes_depositados)
    verificar_cantidad_billetes(cantidad_de_billetes_depositados)
  except:
    raise ValueError('\nSistema le informa: "Tipo de entrada incorrecta."\nSistema le informa: "No se pudo realizar el depósito correctamente." ')

def verificar_cantidad_billetes(cantidad_de_billetes_depositados):
  '''
  Función auxiliar para verificar que la cantidad de billetes sean numeros enteros y positivos.
  Parámetro: cantidad de billetes depositados por el usuario
  Return: se llama a la función depositar_dinero para volver a intentar depositar dinero.
  '''
  cantidad_de_billetes_depositados = int(cantidad_de_billetes_depositados)
  if cantidad_de_billetes_depositados != abs(cantidad_de_billetes_depositados):
    raise ValueError('\nSistema le informa: "Cantidad de billetes inválida."\nSistema le informa: "No se pudo realizar el depósito correctamente." ')

def buscar_linea_cajero(cajero_seleccionado, posicion_del_archivo_cajero):
  '''
  Función encargada de buscar la línea en donde se encuentra el cajero seleccionado.
  Parámetro: el cajero en donde se desea hacer el depósito, la posición del archivo iniciado en cero
  y las cantidades de billetes depositados.
  Return: si se encuentra el cajero entonces se procede a actualizar la cantidad de billetes del cajero seleccionado.
  Return: si no se encuentra se hace el llamado recursivo para seguir buscando.
  '''             
  buscar_linea_archivo_cajero = open("Lista_de_cajeros.txt", "r+")
  lectura_linea_texto_cajero = buscar_linea_archivo_cajero.readlines()
  buscar_linea_archivo_cajero.close()
  lineas_texto_cajero = lectura_linea_texto_cajero[posicion_del_archivo_cajero]
  if cajero_seleccionado in lineas_texto_cajero:
    return posicion_del_archivo_cajero
  else:
    # si no se encueentra se sigue buscando
    posicion_del_archivo_cajero += 1
    return buscar_linea_cajero(cajero_seleccionado, posicion_del_archivo_cajero)

def actualizar_montos_cajeros(cajero_seleccionado, cantidad_billetes_100, cantidad_billetes_50, 
cantidad_billetes_20, cantidad_billetes_10, cantidad_billetes_5, cantidad_billetes_2, cantidad_billetes_1):
  '''
  Función encargada de actualizar la cantidad de cada denominación.
  Parámetro: el cajero en donde se desea hacer el depósito, la posición del archivo iniciado en cero
  y las cantidades de billetes depositados.
  Return: si se encuentra el cajero entonces se procede a rescatar las líneas que no van a ser modificadas.
  Return: si no se encuentra se hace el llamado recursivo para seguir buscando.
  '''             
  posicion_del_archivo_cajero = buscar_linea_cajero(cajero_seleccionado, 0)
  actualizar_linea_cajero = open("Lista_de_cajeros.txt", "r+")
  leer_linea_texto_cajero = actualizar_linea_cajero.readlines()
  linea_cajero = leer_linea_texto_cajero[posicion_del_archivo_cajero]
  linea_cajero = linea_cajero.replace("[", "")
  linea_cajero = linea_cajero.replace("]", "")
  linea_cajero = linea_cajero.replace("'", "")
  linea_cajero = linea_cajero.replace(" ", "")
  linea_cajero = linea_cajero.replace("\n", "")
  #divide la linea por comas
  lista_hileras_cajero_actualizado = linea_cajero.split(",") 

  # se suma la cantidad que ya estaba con la cantidad nueva
  # se sustituye la cantidad antigua con la nueva

  # posición en la hilera de la cantidad de billetes de 100
  lista_hileras_cajero_actualizado[3] = int(lista_hileras_cajero_actualizado[3]) + int(cantidad_billetes_100)
  # posición en la hilera de la cantidad de billetes de 50
  lista_hileras_cajero_actualizado[5] = int(lista_hileras_cajero_actualizado[5]) + int(cantidad_billetes_50)
  # posición en la hilera de la cantidad de billetes de 20
  lista_hileras_cajero_actualizado[7] = int(lista_hileras_cajero_actualizado[7]) + int(cantidad_billetes_20)
  # posición en la hilera de la cantidad de billetes de 10
  lista_hileras_cajero_actualizado[9] = int(lista_hileras_cajero_actualizado[9]) + int(cantidad_billetes_10)
  # posición en la hilera de la cantidad de billetes de 5
  lista_hileras_cajero_actualizado[11] = int(lista_hileras_cajero_actualizado[11]) + int(cantidad_billetes_5)
  # posición en la hilera de la cantidad de billetes de 2
  lista_hileras_cajero_actualizado[13] = int(lista_hileras_cajero_actualizado[13]) + int(cantidad_billetes_2)
  # posición en la hilera de la cantidad de billetes de 1
  lista_hileras_cajero_actualizado[15] = int(lista_hileras_cajero_actualizado[15]) + int(cantidad_billetes_1)

  actualizar_linea_cajero.close()
  return rescatar_lineas_cajero_cliente(0, '', lista_hileras_cajero_actualizado, cajero_seleccionado)

def rescatar_lineas_cajero_cliente(posicion_cajero, datos_cajero_actualizados, lista_hileras_cajero_actualizado, cajero_seleccionado):
  """
  Función que se encarga de rescatar las líneas del archivo que no se van a modificar.
  posicion_cajero: inicializado en 0, luego va a ser modificado y utilizado para leer todas las lineas.
  datos_cajero_actualizados: espacio vacío donde se guardarán las hileras no modificadas.
  lista_hileras_cajero_actualizado: hilera actualizada con los billetes agregados.
  cajero_seleccionado: cajero seleccionado por el banquero al que desea agregar billetes.
  return: si se lee o no la línea que posee el cajero actualizado se hace el llamado recursivo para que lea la siguiente línea.
  return: si se termina de rescatar todas las lineas no modificadas se llama a la función para que actualice el archivo.
  """
  rescatar_linea_archivo_cajero_cliente = open("Lista_de_cajeros.txt", "r")
  leer_linea_texto_cajero = rescatar_linea_archivo_cajero_cliente.readlines()
  rescatar_linea_archivo_cajero_cliente.close()
  if posicion_cajero < len(leer_linea_texto_cajero):
    linea_a_revisar_cajero = leer_linea_texto_cajero[posicion_cajero]
    linea_a_revisar_cajero = linea_a_revisar_cajero.replace("\n", "")
    linea_a_revisar_cajero = linea_a_revisar_cajero.replace('"', "")
    linea_a_revisar_cajero = linea_a_revisar_cajero.replace('"', "")
    linea_a_revisar_cajero = linea_a_revisar_cajero.replace(" ", "")
    if cajero_seleccionado in linea_a_revisar_cajero:
      # si el cajero seleccionado está en las lineas se salta
      posicion_cajero += 1
      return rescatar_lineas_cajero_cliente(posicion_cajero, datos_cajero_actualizados, lista_hileras_cajero_actualizado, cajero_seleccionado)
    else:
      # si el cajero seleccionado no está entonces se guarda la hilera en la variable
      datos_cajero = linea_a_revisar_cajero + '\n'
      datos_cajero_actualizados += datos_cajero
      # se sigue con la siguiente línea
      posicion_cajero += 1
      return rescatar_lineas_cajero_cliente(posicion_cajero, datos_cajero_actualizados, lista_hileras_cajero_actualizado, cajero_seleccionado)
  else:
    # se suman las hileras no modificadas con la modificada
    datos_cajero_actualizados += str(lista_hileras_cajero_actualizado)
    return actualizar_datos_cajero_cliente(datos_cajero_actualizados)

def actualizar_datos_cajero_cliente(datos_cajero_actualizados):
  """
  Función que se encarga de actualizar el archivo de los cajeros.
  Parámetro: los datos actualizados luego de ser modificados.
  """
  archivo_cajeros_original = open("Lista_de_cajeros.txt", "a")
  # se vacía el archivo
  archivo_cajeros_original.truncate(0)
  # se escriben los datos nuevos/actualizados
  archivo_cajeros_original.write(datos_cajero_actualizados)
  archivo_cajeros_original.close()


##

def sumar_monto_depositado(depositar_billetes_100, depositar_billetes_50, depositar_billetes_20,
depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1, 
cajero_seleccionado, usuario_usando_el_sistema):
  '''
  Función encargada de sumar todo el monto depositado por el usuario para actualizar su saldo.
  Parámetro: las cantidades de billetes depositados, el cajero seleccionado y el nombre del usuario.
  Return: se llama a la función con el nombre de usuario, un cero como posición inicial a revisar, el monto
  total depositado y el cajero seleccionado.
  '''      
  # se multiplica cada cantidad con su respectiva denominación para así tener el monto total depositado
  monto_depositado = (int(depositar_billetes_100)*100) + (int(depositar_billetes_50)*50) + (int(depositar_billetes_20)*20) + \
  (int(depositar_billetes_10)*10) + (int(depositar_billetes_5)*5) + (int(depositar_billetes_2)*2) + int(depositar_billetes_1)
  return actualizar_monto_usuario(usuario_usando_el_sistema, monto_depositado, cajero_seleccionado)

def buscar_linea_usuario(usuario_usando_el_sistema, posicion_del_archivo_usuario):
  '''
  Función encargada de buscar la línea en donde se encuentra los datos del usuario en el archivo.
  Parámetro: el nombre del usuario, la posición inicializada en cero, el monto total depositado y el cajero seleccionado
  donde se quiere hacer el depósito.
  Return: si se encuentra el usuario entonces se procede a actualizar la cantidad de billetes del cajero seleccionado.
  Return: si no se encuentra se hace el llamado recursivo para seguir buscando.
  '''     
  buscar_linea_archivo_usuario = open("Lista_de_usuarios.txt", "r+")
  lectura_linea_texto_usuario = buscar_linea_archivo_usuario.readlines()
  buscar_linea_archivo_usuario.close()
  lectura_lineas_texto = lectura_linea_texto_usuario[posicion_del_archivo_usuario]
  if usuario_usando_el_sistema in lectura_lineas_texto:
    return posicion_del_archivo_usuario
  else:
    # si no se encuentra se sigue con la siguiente
    posicion_del_archivo_usuario += 1
    return buscar_linea_usuario(usuario_usando_el_sistema, posicion_del_archivo_usuario)

def actualizar_monto_usuario(usuario_usando_el_sistema, monto_depositado, cajero_seleccionado):
  '''
  Función encargada de actualizar el saldo del usuario.
  Parámetro: el nombre del usuario, la posición inicializada en cero, el monto total depositado y el cajero seleccionado
  donde se quiere hacer el depósito.
  Return: se llama a la función actualizar datos 
  '''    
  posicion_del_archivo = buscar_linea_usuario(usuario_usando_el_sistema, 0)
  actualizar_linea_usuario = open("Lista_de_usuarios.txt", "r+")
  leer_linea_texto_usuario = actualizar_linea_usuario.readlines()
  linea = leer_linea_texto_usuario[posicion_del_archivo]
  linea = linea.replace("'", "")
  linea = linea.replace("[", "")
  linea = linea.replace("]", "")
  linea = linea.replace("\n", "")
  #divide la linea por comas
  lista_hileras_usuario_actualizado = linea.split(",")
  # esa es la posición en la hilera donde se encuentra guardado el saldo del usuario
  # se le suma el monto depositado al saldo antiguo 
  nuevo_monto = int(lista_hileras_usuario_actualizado[5]) + monto_depositado
  # se le actualiza el saldo del usuario
  lista_hileras_usuario_actualizado[5] = nuevo_monto
  monto = str(monto_depositado)
  # se crea la variable que indicará el monto del depósito en el historial
  deposito = ' ' +'+' + monto
  # se crea la variable que indicará la fecha y hora del depósito en el historial
  hora = ' ' + time.asctime()
  # se crea la variable que indicará en qué cajero se hizo el depósito
  cajero_seleccionado = ' ' + 'Accion_realizada_en: ' + cajero_seleccionado
  # la posición 7 es la destinada al historial de transacciones

  # si no hay nada en el historial 
  if lista_hileras_usuario_actualizado[7] == ' ':
    # se asigna el primer valor y luego se suman los otros al string
    lista_hileras_usuario_actualizado[7] = deposito 
    lista_hileras_usuario_actualizado[7] += hora
    lista_hileras_usuario_actualizado[7] += cajero_seleccionado
    print(lista_hileras_usuario_actualizado)
    
  else: 
    # si el historial no está vacío solo se suman los strings
    lista_hileras_usuario_actualizado[7] += deposito
    lista_hileras_usuario_actualizado[7] += hora
    lista_hileras_usuario_actualizado[7] += cajero_seleccionado
    
  actualizar_linea_usuario.close()  
  return rescatar_lineas_usuario(0, '' , lista_hileras_usuario_actualizado, usuario_usando_el_sistema)

def rescatar_lineas_usuario(posicion, datos_usuario_actualizados, lista_hileras_usuario_actualizado, usuario_usando_el_sistema):
  '''
  Función encargada de rescatar las líneas del archivo de usuarios que no se van a modificar.
  Parámetros: posición leyendo lilera del archivo iniciada en cero, la variable vacía en donde se almacenarán ya todos 
  los datos actualizados con las hileras no modificadas, la hilera actualizada y el usuario usando el sistema.
  donde se quiere hacer el depósito.
  Return: se llama a la función encargada de actualizar los datos del usuario.
  '''    
  rescatar_linea_usuario = open("Lista_de_usuarios.txt", "r")
  leer_linea_texto_usuario = rescatar_linea_usuario.readlines()
  if posicion < len(leer_linea_texto_usuario):
    linea_a_revisar = leer_linea_texto_usuario[posicion]
    linea_a_revisar = linea_a_revisar.replace("\n", "")
    linea_a_revisar = linea_a_revisar.replace('"', "")
    linea_a_revisar = linea_a_revisar.replace('"', "")
    rescatar_linea_usuario.close()
    if usuario_usando_el_sistema in linea_a_revisar:
      posicion += 1
      # si se encuentra la hilera sin modificar del usuario se salta
      return rescatar_lineas_usuario(posicion, datos_usuario_actualizados, lista_hileras_usuario_actualizado, usuario_usando_el_sistema)
    else:
      # se guardan las hileras que no fueron modificadas
      datos = str(linea_a_revisar) + '\n'
      # se agrega a la variable que guardará todos los nuevos datos
      datos_usuario_actualizados += datos
      # se sigue con las hileras restantes
      posicion += 1
      return rescatar_lineas_usuario(posicion, datos_usuario_actualizados, lista_hileras_usuario_actualizado, usuario_usando_el_sistema)
  else:
    # una vez rescatado todos los datos se agrega la hilera modificada
    datos_usuario_actualizados += str(lista_hileras_usuario_actualizado)
    return actualizar_datos_usuario(datos_usuario_actualizados)

def actualizar_datos_usuario(datos_usuario_actualizados):
  """
  Función que se encarga de actualizar el archivo de los usuarios.
  Parámetro: los datos actualizados luego de ser modificados.
  """
  archivo_usuarios_original = open("Lista_de_usuarios.txt", "r+")
  archivo_usuarios_original.truncate(0)
  archivo_usuarios_original.writelines(datos_usuario_actualizados)
  print('Estimado Usuario, la transacción de dinero se ha realizado correctamente.')
  archivo_usuarios_original.close()
  from Menu_principal import correr_menu_principal
  print('\nVolviendo al menú principal...')
  return correr_menu_principal()


# Retirar dinero
def retirar_dinero(cajero_seleccionado, usuario_usando_el_sistema):
  '''
  Función encargada de pedirle al usuario el monto de dinero que desea retirar del cajero.
  Parámetros: el cajero en el que se desea hacer el retiro y el nombre del usuario que desea hacer el retiro.
  Return: se llama a la función encargada de buscar la línea en el que se encuentra el cajero seleccionado.
  '''
  instrucciones_del_retiro = 'Por favor inserte el monto de pesos que desea retirar. \n'
  retirar_monto = input(instrucciones_del_retiro)

  # de ser una entrada inválida, se tira un error informando al usuario
  try: 
    retirar_monto = int(retirar_monto) 
    if isinstance(retirar_monto, int):
      if retirar_monto != abs(retirar_monto):
        raise ValueError('Sistema le informa: Tipo de entrada incorrecta')
      else:
        # se inicializa la posición a revisar en cero 
        return verificar_posibilidad_del_retiro(cajero_seleccionado, retirar_monto, usuario_usando_el_sistema)
  except ValueError:
    raise ValueError('Sistema le informa: Tipo de entrada incorrecta')
  
def verificar_posibilidad_del_retiro(cajero_seleccionado, retirar_monto, usuario_usando_el_sistema):
  '''
  Función encargada de verificar que el cajero y el usuario tengan dinero suficiente para hacer el retiro.
  Parámetros: el cajero en el que se desea hacer el retiro, el monto a retirar y el nombre del usuario que desea hacer el retiro.
  Return: se llama a otra función para que complete el retiro de dinero.
  '''
  # se hace llamado a la función ya creada para buscar la línea en donde se encuentra el cajero seleccionado
  posicion_cajero_retirar = buscar_linea_cajero(cajero_seleccionado, 0)
  # se lee el archivo del cajero
  verificar_cajero_retiro = open("Lista_de_cajeros.txt", "r+")
  leer_linea_cajero = verificar_cajero_retiro.readlines()
  verificar_cajero_retiro.close()
  cajero_a_retirar = leer_linea_cajero[posicion_cajero_retirar]
  cajero_a_retirar = cajero_a_retirar.replace("[", "")
  cajero_a_retirar = cajero_a_retirar.replace("]", "")
  cajero_a_retirar = cajero_a_retirar.replace("'", "")
  cajero_a_retirar = cajero_a_retirar.replace(" ", "")
  cajero_a_retirar = cajero_a_retirar.replace("\n", "")
  #divide la linea por comas
  hilera_del_cajero = cajero_a_retirar.split(",")
  # se muestra la cantidad de dinero que hay por billetes
  print('Cantidad de billetes de 100 disponibles:', hilera_del_cajero[3]) 
  print('Cantidad de billetes de 50 disponibles:', hilera_del_cajero[5])
  print('Cantidad de billetes de 20 disponibles:', hilera_del_cajero[7])  
  print('Cantidad de billetes de 10 disponibles:', hilera_del_cajero[9]) 
  print('Cantidad de billetes de 5 disponibles:', hilera_del_cajero[11]) 
  print('Cantidad de billetes de 2 disponibles:', hilera_del_cajero[13]) 
  print('Cantidad de billetes de 1 disponibles:', hilera_del_cajero[15]) 
  # se suma la cantidad disponible que tiene el cajero
  dinero_disponible = (int(hilera_del_cajero[3])*100) + (int(hilera_del_cajero[5])*50) + (int(hilera_del_cajero[7])*20) + \
  (int(hilera_del_cajero[9])*10) + (int(hilera_del_cajero[11])*5) + (int(hilera_del_cajero[13])*2) + int(hilera_del_cajero[15])
  # se abre el archivo de los usuarios para obtener la hilera del usuario que quiere hacer el retiro
  verificar_usuario_retiro = open("Lista_de_usuarios.txt", "r+")
  leer_linea_usuario = verificar_usuario_retiro.readlines()
  verificar_usuario_retiro.close()
  # se llama a la función ya creada anteriormente para buscar la línea en donde se encuentra el usuario actual en el archivo.
  posicion_usuario_actual = buscar_linea_usuario(usuario_usando_el_sistema, 0)
  # se lee la línea que contiene la información del usuario actual
  verificar_saldo_a_retirar = leer_linea_usuario[posicion_usuario_actual]
  verificar_saldo_a_retirar = verificar_saldo_a_retirar.replace("[", "")
  verificar_saldo_a_retirar = verificar_saldo_a_retirar.replace("]", "")
  verificar_saldo_a_retirar = verificar_saldo_a_retirar.replace("'", "")
  verificar_saldo_a_retirar = verificar_saldo_a_retirar.replace(" ", "")
  verificar_saldo_a_retirar = verificar_saldo_a_retirar.replace("\n", "")
  #divide la linea por comas
  hilera_del_saldo_usuario = verificar_saldo_a_retirar.split(",")
  # si la cantidad disponible es igual o mayor a la cantidad de dinero a retirar se realiza el retiro
  if dinero_disponible >= retirar_monto:
    if (int(hilera_del_saldo_usuario[5])) >= retirar_monto:
      # tres es donde inicia la cantidad de billetes por denominación en la hilera
      return realizar_el_retiro(cajero_seleccionado, retirar_monto, hilera_del_cajero, 3,  
      usuario_usando_el_sistema, retirar_monto, hilera_del_cajero)

   # si no es posible realizar el retiro se notifica al usuario            
    else:
      print('Estimado usuario, su cuenta no posee el saldo suficiente para realizar el retiro.')
      print('Sistema le informa: "No se pudo realizar el retiro de dinero."')
      from Menu_principal import correr_menu_principal
      print('Volviendo al menú principal...')
      return correr_menu_principal()
  else:
    print('Estimado usuario, el cajero no dispone suficiente dinero para realizar el retiro.')
    print('Sistema le informa: "No se pudo realizar el retiro de dinero."')
    print('Volviendo al menú principal...')
    return correr_menu_principal()

def obtener_denominacion(posicion_de_billetes):
  '''
  Función que determina la denominación correspondiente de billetes según la posición en la hilera.
  Parámetro: la poisición actual que se está leyendo en la hilera.
  Return: se retorna el monto de la denominación 
  '''
  monto_denominacion = 0
  # la posición 3 correspone a la cantidad de billetes de 100
  if posicion_de_billetes == 3:
    monto_denominacion = 100
  # la posición 5 correspone a la cantidad de billetes de 50
  elif posicion_de_billetes == 5:
    monto_denominacion = 50
  # la posición 7 correspone a la cantidad de billetes de 20
  elif posicion_de_billetes == 7:
    monto_denominacion = 20
  # la posición 9 correspone a la cantidad de billetes de 10
  elif posicion_de_billetes == 9:
    monto_denominacion = 10
  # la posición 11 correspone a la cantidad de billetes de 5
  elif posicion_de_billetes == 11:
    monto_denominacion = 5
  # la posición 13 correspone a la cantidad de billetes de 2
  elif posicion_de_billetes == 13:
    monto_denominacion = 2
  # la posición 15 correspone a la cantidad de billetes de 1
  elif posicion_de_billetes == 15:
    monto_denominacion = 1
  return monto_denominacion


def realizar_el_retiro(cajero_seleccionado, retirar_monto, hilera_del_cajero, posicion_de_billetes, 
usuario_usando_el_sistema, retirar_monto_original, hilera_modificada):
  '''
  Función que realiza el retiro correspondiente, actualizando a su vez la cantidad de billetes en el cajero.
  Parámetros: el cajero en el que se desea hacer el retiro, el monto a retirar que se tomará como referencia para ver cuanto dinero 
  falta por retirar, la hilera que contiene la información del cajero, la posición de la primera cantidad de billetes por 
  denominación en la hilera, el nombre de usuario, el monto a retirar que se utilizará para el historial y la hilera que contiene la información del usuario
  Return: se llama a otra función para que complete el retiro de dinero, si no se ha terminado de verificar por denominación se hace el llamado recursivo.
  '''
  # se hace llamado a la función recien creada para determinar cuál es la denominación correspondiente a la posición
  monto_denominacion = obtener_denominacion(posicion_de_billetes)
  # el retiro inicial no puede ser cero
  if retirar_monto > 0:
    # la última posición que posee la cantidad de billetes es 15, no se puede sobrepasar de este
    if posicion_de_billetes <= 15:
      # se busca la cantidad de billetes que hay de la denominación
      cantidad_billetes = hilera_del_cajero[posicion_de_billetes]
      # la división entera no puede dar cero porque eso significa que no hay billetes para hacer la denominación
      # deben de existir una cantidad de billetes 
      if ((retirar_monto // monto_denominacion) != 0) and (int(cantidad_billetes) != 0):  # la división entera ayuda a saber cuantos billetes se pueden utilizar
        # se calcula la cantidad de billetes que no vayan a ser utilzados
        billetes_restantes = int(hilera_del_cajero[posicion_de_billetes]) - (retirar_monto // monto_denominacion)
        # se calcula la cantidad de billetes que sí se van a utilizar para el retiro
        billetes_a_utilizar = int(hilera_del_cajero[posicion_de_billetes]) - billetes_restantes
        # se calcula el monto que queda por retirar
        monto_restante = retirar_monto - (int(billetes_a_utilizar * monto_denominacion))
        # se actualiza la hilera con los billetes sobrantes de la denominación recién usada
        hilera_modificada[posicion_de_billetes] = billetes_restantes
        # si aun queda dinero por retirar se sigue con la siguiente denominacion
        if monto_restante > 0:
          # la ubicación de las cantidades de los billetes en la hilera va de dos en dos
          posicion_de_billetes += 2
          return realizar_el_retiro(cajero_seleccionado, monto_restante, hilera_del_cajero, posicion_de_billetes,
                                    usuario_usando_el_sistema, retirar_monto_original, hilera_modificada)
        # si ya no queda monto por retirar entonces se procede a actualizar el cajero y el saldo e historial del usuario
        else:
          # se hace llamado a la función ya creada para rescatar y actualizar los datos del cajero
          rescatar_lineas_cajero_cliente(0, '', hilera_modificada, cajero_seleccionado)
          # se actualiza el saldo del usuario
          return actualizar_monto_usuario_con_retiro(usuario_usando_el_sistema,  retirar_monto_original, cajero_seleccionado)
    
      # si la denominacion no tiene  billetes se sigue con el siguiente
      else:
        posicion_de_billetes += 2
        return realizar_el_retiro(cajero_seleccionado, retirar_monto, hilera_del_cajero, posicion_de_billetes,
                                  usuario_usando_el_sistema, retirar_monto_original, 
                                  hilera_modificada)
    # si hay dinero suficiente para hacer el retiro pero no las denominaciones suficientes
    else:
      print('Sistema le informa: "Estimado usuario, no se pudo completar el retiro".')
      from Menu_principal import correr_menu_principal
      print('\nVolviendo al menú principal...')
      return correr_menu_principal()

  # no se puede hacer retiro de cero pesos
  else:
    print('Estimado usuario, digite una cantidad que sea posible retirar.')
    from Menu_principal import correr_menu_principal
    print('\nVolviendo al menú principal...')
    return correr_menu_principal()


def actualizar_monto_usuario_con_retiro(usuario_actual, monto_retirado, cajero_seleccionado):
  '''
  Función que agrega el retiro al historial del cliente del banco y actualiza su saldo.
  Parámetros: el nombre del usuario, el monto total retirado y el cajero en el que se desea hacer el retiro. 
  Return: se llama a otra función para que terminar de actualizar el archivo del usuario.
  '''
  actualizar_saldo_usuario = open("Lista_de_usuarios.txt", "r+")
  leer_datos_del_usuario = actualizar_saldo_usuario.readlines()
  # se busca la posición en el archivo en la función previamente creada
  posicion_usuario_actual = buscar_linea_usuario(usuario_actual, 0)
  reemplazar_linea = leer_datos_del_usuario[posicion_usuario_actual]
  reemplazar_linea = reemplazar_linea.replace("'", "")
  reemplazar_linea = reemplazar_linea.replace("[", "")
  reemplazar_linea = reemplazar_linea.replace("]", "")
  reemplazar_linea = reemplazar_linea.replace("\n", "")
  #divide la linea por comas
  lista_usuario_a_actualizado = reemplazar_linea.split(",")
  # se actualiza el saldo del usuario
  nuevo_monto_con_retiro = int(lista_usuario_a_actualizado[5]) - monto_retirado
  lista_usuario_a_actualizado[5] = nuevo_monto_con_retiro

  # se crea la variable con el retiro
  monto_retirado = str(monto_retirado)
  #se concatenan 
  retiro = ' ' +'-' + monto_retirado
  # se crea la variable con la fecha y hora que se hizo el retiro
  hora_del_retiro = ' ' + time.asctime()
  # se crea una variable con la ubicación del retiro realizado
  cajero_seleccionado = ' ' + 'Accion_realizada_en: ' + cajero_seleccionado
  # se actualiza el historial
  lista_usuario_a_actualizado[7] += retiro
  lista_usuario_a_actualizado[7] += hora_del_retiro
  lista_usuario_a_actualizado[7] += cajero_seleccionado
  actualizar_saldo_usuario.close()  
  # se utiliza la función ya creada para actualizar el archivo con los datos del usuario
  return rescatar_lineas_usuario(0, '' , lista_usuario_a_actualizado, usuario_actual)

# Mostrar saldo del usuario

def consultar_saldo(usuario_usando_el_sistema):
  '''
  Función que muestra el saldo del cliente del banco.
  Parámetros: el nombre del usuario que desea consultar su saldo.
  '''
  linea_con_saldo_usuario = open("Lista_de_usuarios.txt", "r+")
  leer_datos_usuario = linea_con_saldo_usuario.readlines()
  # se busca la hilera del usuario actual en el archivo con la función ya existente
  posicion_del_archivo_usuario = buscar_linea_usuario(usuario_usando_el_sistema, 0)
  buscar_usuario_en_bases_de_datos = leer_datos_usuario[posicion_del_archivo_usuario]
  # se reemplaza todo lo que no nos interesa
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("'", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("[", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("]", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("   ", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("  ", "") 
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("\n", "")
  linea_correcta = buscar_usuario_en_bases_de_datos.split(',') 
  # se muestra el monto disponible
  # la posición 5 siempre se encuentra el saldo del usuario en la hilera
  print('Monto disponible:', linea_correcta[5])
  from Menu_principal import correr_menu_principal
  print('\nVolviendo al menú principal...')
  return correr_menu_principal()

 
# Mostrar historial de transacciones
def historial_transacciones(usuario_usando_el_sistema):
  '''
  Función que muestra el historial de transacciones del usuario.
  Parámetros: el nombre del usuario que desea conocer su historial.
  '''
  buscar_historial = open("Lista_de_usuarios.txt", "r+")
  buscar_linea_con_hisotorial = buscar_historial.readlines()
  # se busca la hilera del usuario actual en el archivo con la función ya existente
  posicion_del_archivo_usuario = buscar_linea_usuario(usuario_usando_el_sistema, 0)
  # se guardan sus datos en una variable
  buscar_usuario_en_bases_de_datos = buscar_linea_con_hisotorial[posicion_del_archivo_usuario]
  # se elimina todo lo que no nos interesa
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("'", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("[", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("]", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("   ", "")
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("  ", "") 
  buscar_usuario_en_bases_de_datos = buscar_usuario_en_bases_de_datos.replace("\n", "")
  # se divide para que sea lista
  linea_correcta = buscar_usuario_en_bases_de_datos.split(',') 
  # se asigna un nombre significativo al historial del usuario
  hilera_con_historial = linea_correcta[7]
  if (hilera_con_historial == ' '):
    print('Estimado usuario, no posee historial de transacciones')
    from Menu_principal import correr_menu_principal
    return correr_menu_principal()
  else:
    # se llama a la función que imprime los títulos del historial
    imprimir_titulos()
    # se llama a la función que se encarga de imprimir cada dato del historial del usuario
    # se inicializa en cero la posción a revisar
    separar_transaccion(hilera_con_historial, 0)


def imprimir_titulos():
  '''
  Función que se encarga de imprimir los títulos de cada información del historial a mostrar
  No tiene parámetros
  '''
  titulo_cantidad = "Transaccion realizada"
  titulo_fecha_y_hora = "Fecha y hora de la transaccion"
  titulo_ubicacion = 'Cajero donde se hizo la transaccion \n'

  # se ajusta la ubicación de cada título
  titulo_cantidad = titulo_cantidad.ljust(10)
  titulo_fecha_y_hora = titulo_fecha_y_hora.center(30)
  titulo_ubicacion = titulo_ubicacion.rjust(30)
  print(titulo_cantidad,titulo_fecha_y_hora,titulo_ubicacion) 

def imrprimir_datos(cantidad, fecha_y_hora, ubicacion):
  '''
  Función que imrprime los datos del historial del usuario.
  Parámetros: cantidad de dinero depositado o retirado, fecha y hora que se realizó la transacción.
  y el cajero en donde se hizo la acción.
  '''
  # se ajusta la posición para que quede simétrico
  cantidad = cantidad.ljust(10)
  fecha_y_hora = fecha_y_hora.center(51)
  ubicacion = ubicacion.rjust(0)
  print(cantidad, fecha_y_hora, ubicacion)

def separar_transaccion(hilera_con_historial, posicion_str_historial):
  '''
  Función que divide el historial de transacción con sus respectivas categorías.
  Parámetros: cantidad de dinero depositado o retirado, fecha y hora que se realizó la transacción 
  y el cajero en donde se hizo la acción.
  '''
  # separamos por espacio 
  lista_de_hilera_con_historial = hilera_con_historial.split(' ')
  largo_del_historial = len(lista_de_hilera_con_historial)
  # estructura general:
  # monto retirado/depositado, dia-mes-número de día-hora-minutos-segundos, acción realizada en-nombre del cajero

  # tiene que llegar hasta el último elemento del historial
  if(posicion_str_historial <= (largo_del_historial - 1)):
    # se guarda el monto retirado/depositado
    cantidad = lista_de_hilera_con_historial[(posicion_str_historial)]
    # se guarda la fecha y hora
    fecha_y_hora = lista_de_hilera_con_historial[(posicion_str_historial+1)] + ' ' + lista_de_hilera_con_historial[(posicion_str_historial+2)] + \
    ' ' + lista_de_hilera_con_historial[(posicion_str_historial+3)] + ' ' + lista_de_hilera_con_historial[(posicion_str_historial+4)] + ' ' + \
    lista_de_hilera_con_historial[(posicion_str_historial+5)]
    # se guarda en dónde se hizo la transacción
    ubicacion = lista_de_hilera_con_historial[(posicion_str_historial+6)] + ' ' + lista_de_hilera_con_historial[(posicion_str_historial+7)]
    # se imprimen los datos correspondientes
    imrprimir_datos(cantidad, fecha_y_hora, ubicacion)
    # si aún queda historial por leer se sigue con la siguiente, separandola de la otra con \n
    if posicion_str_historial + 7 < (largo_del_historial - 1):
      # el inicio de las transacciones va en 8 en ocho
      posicion_str_historial += 8
      # se llama a la función ya creada para que imprima los datos del historial
      return separar_transaccion(hilera_con_historial, posicion_str_historial)
    else:
      from Menu_principal import correr_menu_principal
      print('\nVolviendo al menú principal...')
      return correr_menu_principal()
