import datetime
ARCHIVO = 'usuarios_test.txt'

def registrar_usuario(): # guarda directamente en el archivo txt
    nombre = input("Ingrese el nombre del usuario: ").strip().lower()
    edad = input("Ingrese la edad del usuario: ").strip().lower()
    correo = input("Ingrese el correo electrónico del usuario: ").strip().lower()
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not nombre or not edad or not correo:
        print("Todos los campos son obligatorios. Por favor, intente de nuevo.")
        return

    if not edad.isdigit() or int(edad) <= 0 or int(edad) > 120:
        print("La edad debe ser un número positivo entre 1 y 120. Por favor, intente de nuevo.")
        return

    try:
        with open(ARCHIVO, mode='r', encoding= 'utf-8') as file:
            for line in file:
                if nombre in line.split(',')[0].strip():
                    print("El usuario ya existe. Por favor, intente con otro nombre.")
                    return
    except FileNotFoundError:
        pass  # Si el archivo no existe, se creará al guardar el primer usuario

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

    with open(ARCHIVO, mode='a', encoding='utf-8') as file:
        #encabezado del archivo: Nombre, Edad , Correo , Fecha y Hora
        if file.tell() == 0:  # Si el archivo está vacío, escribir el encabezado
            file.write("Nombre, Edad , Correo , Fecha y Hora\n")
        file.write(f"{nombre}, {edad} , {correo} , {fecha_hora}\n")
        print(f"Usuario {nombre} registrado exitosamente.")


def mostrar_usuarios(): 
    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            for line in file:
                if line.strip() and not line.startswith("Nombre, Edad , Correo , Fecha y Hora"):
                    print(line.strip())
        
    except FileNotFoundError:
        print("No se encontró el archivo usuarios.txt. Por favor, registre usuarios primero.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
    

def buscar_usuario(nombre):
    try:
        with open(ARCHIVO, mode='r') as file:
            for line in file:
                if line.strip() and not line.startswith("Nombre, Edad , Correo , Fecha y Hora"):
                    if nombre in line.split(',')[0].strip().lower():
                        return line.strip()
        return None
    except FileNotFoundError:
        print("No se encontró el archivo usuarios.txt. Por favor, registre usuarios primero.")
        return None
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
        return None

#Pilas!!! en la opción de validar un archivo, yo les voy a pasar un archivo con errores y esa opción me va a mostrar los errores.



def crear_archivo_errores(): # Esta funcioncita lo que hace es: Lee el txt y luego va catalogando los errores encontrados, por ejemplo, si encuentra una línea que no tiene el formato correcto, lo registra en el archivo de errores y si esta bien crea un archivo de registros buenos.
    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            with open('usuarios_errores.txt', mode='a', encoding='utf-8') as error_file, \
                 open('usuarios_limpios.txt', mode='a', encoding='utf-8') as limpio_file:
                for line in file:
                    if not line.strip() or line.startswith("Nombre, Edad , Correo , Fecha y Hora"):
                        continue  
                    partes = line.split(',')
                    if len(partes) < 2:
                        error_file.write(f"Error de formato en la línea: {line.strip()}\n")
                        continue
                    nombre = partes[0].strip()
                    if nombre == "":
                        error_file.write(f"Error de formato de nombre (no hay nombre) en la línea: {line.strip()}\n")
                        continue
                    edad_partes = partes[1].strip() 
                    if len(edad_partes) < 2:
                        error_file.write(f"Error de formato de edad en la línea: {line.strip()}\n")
                        continue
                    if not edad_partes.isdigit():
                        error_file.write(f"Error de formato de edad en la línea: {line.strip()}\n")
                        continue
                    if int(edad_partes) < 0:
                        error_file.write(f"Error de formato de edad (negativa) en la línea: {line.strip()}\n")
                        continue
                    correo_partes = partes[2].strip()
                    if '@' not in correo_partes:
                        error_file.write(f"Error de formato de correo en la línea: {line.strip()}\n")
                        continue
                    fecha_hora_partes = partes[3].strip()
                    try:
                        datetime.datetime.strptime(fecha_hora_partes, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        error_file.write(f"Error de formato de fecha y hora en la línea: {line.strip()}\n")
                        continue
                    limpio_file.write(line)

    except FileNotFoundError:
        print("No se encontró el archivo usuarios.txt. Por favor, registre usuarios primero.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


def validaciones():
    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            for line in file:
                if not line.strip() or line.startswith("Nombre, Edad , Correo , Fecha y Hora"):
                    continue  
                partes = line.split(',')
                if len(partes) < 2:
                    print(f"Error de formato en la línea: {line.strip()}")
                    continue
                nombre = partes[0].strip()
                if nombre == "":
                    print(f"Error de formato de nombre (no hay nombre) en la línea: {line.strip()}")
                    continue
                edad_partes = partes[1].strip()
                if int(edad_partes) < 0:
                    print(f"Error de formato de edad (negativa) en la línea: {line.strip()}")
                    continue
                if not edad_partes.isdigit():
                    print(f"Error de formato de edad en la línea: {line.strip()}")
                    continue
                correo_partes = partes[2].strip()
                if '@' not in correo_partes:
                    print(f"Error de formato de correo en la línea: {line.strip()}")
                    continue
                fecha_hora_partes = partes[3].strip()
                try:
                    datetime.datetime.strptime(fecha_hora_partes, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Error de formato de fecha y hora en la línea: {line.strip()}")
                    
            print("--------------Validación completada--------------")
            
    except FileNotFoundError:
        print("No se encontró el archivo usuarios.txt. Por favor, registre usuarios primero.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


def menu(opcion):
    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        mostrar_usuarios()
    elif opcion == '3':
        nombre = input("Ingrese el nombre del usuario a buscar: ").strip().lower()
        resultado = buscar_usuario(nombre)
        if resultado:
            print(f"Usuario encontrado: {resultado}")
        else:
            print("Usuario no encontrado.")
    elif opcion == '4':
        crear_archivo_errores()
    elif opcion == '5':
        validaciones()
    elif opcion == '6':
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

    
#ESTRUCTURA PRINCIPAL CON MENÚ DE OPCIONES PARA EL USUARIO

def main():
    while True:
        print("\n1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Crear archivos de errores y limpio")
        print("5. Validaciones")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        menu(opcion)


if __name__ == "__main__":   
    main()

