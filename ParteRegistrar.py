import os #Importamos esta libreria para hacer uso de la funcion os.sytem
import time  # Importamos esta libreria para hacer uso de la funcion time.sleep

bienvenida = "Bienvenido Academia de Manejo CR"

#Aqui centramos el texto de bienvenida con la funcion center y le damos de referencia parametros 
print("\n"+bienvenida.center(200, " "))

#Aqui el numero se va registrar
nombre_usuario = input ("Ingrese su nombre: ")
correo_electronico = input ("Ingrese su correo electronico: ")
num_telefono = int (input ("Ingrese su numero de telefono: "))

#El sistema hace una breve espera antes de limpir consola
time.sleep (0.5)
os.system ("cls") #Esta funcion nos limpia consola

print ("Academica de Manejo CR".center(200," "))

#Creamos un menu interactivo
opcion = 1

while opcion != 4: 
    print("1. Curso Teorico"
          "\n2. Clases de Manejo"
          "\n3. Dictamen Medico"
          "\n4. Salir"
          )
    opcion = int (input ("\nSeleccionar una opcion: "))    
    
    if opcion == 4: 
        print("\nGracias por usar nuestro programa\n")