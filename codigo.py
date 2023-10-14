import os

class Menu:
  """
    Clase que maneja el registro de productos y proporciona funcionalidades como registro, búsqueda, modificación y eliminación.
    """
    def __init__(self):
   """
        Constructor para la clase Menu, inicializa las variables de instancia.
        """
        self.nombre = ''
        self.codigo = ''
        self.precio = ''
        self.proveedor = ''
        self.existencias = ''

    def menu_principal(self):
 """
        Función para mostrar el menú principal y manejar las diferentes opciones.
        """
        opcion = 0
        while opcion != 6:
            print("\t\t************ REGISTRO DE PRODUCTOS ************\t\n\n")
            print("\t\t\t1. REGISTRAR PRODUCTO  \n\n")
            print("\t\t\t2. BUSCAR PRODUCTO \n\n")
            print("\t\t\t3. MODIFICAR DATOS\n\n")
            print("\t\t\t4. SALIR\n\n")
            opcion = int(input("\t\t\tOpción: "))
            os.system('clear' if os.name == 'posix' else 'cls')

            if opcion == 1:
                self.registrar()
            elif opcion == 2:
                self.detalle_productos()
            elif opcion == 3:
                self.lista_productos()
            elif opcion == 4:
                self.retirar()
            elif opcion == 5:
                self.modificar_productos()
            elif opcion == 6:
                break
            else:
                print("\nHa ingresado una opción inválida\n\n")

    def registrar(self):
  """
        Función para registrar un nuevo producto.
        """
        with open("productos.txt", "a") as escritura:
            with open("productos.txt", "r") as verificador:
                aux_codigo = input("Ingresa el código del producto: ")
                if aux_codigo == "":
                    while aux_codigo == "":
                        aux_codigo = input("Código del producto no válido!, intentalo nuevamente: ")
                coincidencia = False
                for linea in verificador:
                    datos = linea.split()
                    if self.existencias == aux_codigo:
                        coincidencia = True
                        print("\n\nYa existe un producto con ese código\n\n")
                        print("El producto con ese código es: ", self.nombre, "\n\n")
                        aux_codigo = input("Ingresa un código válido: ")
                        if aux_codigo == "":
                            while aux_codigo == "":
                                aux_codigo = input("Código del producto no válido!, intentalo nuevamente: ")
                        break
                if verificador.closed and (not coincidencia or self.existencias != aux_codigo):
                    self.existencias = aux_codigo
                    print("\t\t\t\t***REGISTRAR EL PRODUCTO***\t\t\t\t\n\n")
                    print("Ingresa si hay existencias: ", self.existencias, "\n\n")
                    self.nombre = input("Ingresa el nombre del producto: ")
                    self.codigo = input("Ingresa el código del producto: ")
                    self.precio = input("Ingresa el precio del producto: ")
                    self.proveedor = input("Proveedor: ")

                    escritura.write(
                        f"{self.existencias}\n\n{self.nombre}\n\n{self.codigo}\n\n{self.precio}\n\n{self.proveedor}\n\n")
                    print("El registro se ha completado correctamente.\n\n")

        pausa()
   """
        Función que pausa la ejecución y espera a que el usuario presione Enter para continuar.
        ""

    def retirar(self):
        encontrado = False
        aux_codigo = input("Ingresa el código del producto que deseas retirar: ")
        respuesta = input(f"Realmente deseas retirar de la lista: {self.nombre} (s/n)?: ")
        if respuesta.lower() in ['s', 'si']:
            print("\n\nEl producto fue retirado correctamente\n\n")
        else:
            print("\n\nProducto conservado\n\n")

        if not encontrado:
            print(f"\n\nNo se encontró el código: {aux_codigo}\n\n")

        with open("productos.txt", "r") as lectura, open("auxiliar.txt", "w") as auxiliar:
            for linea in lectura:
                datos = linea.split()
                if datos and datos[0] == aux_codigo:
                    encontrado = True
                else:
                    auxiliar.write(linea)

        if encontrado:
            os.remove("productos.txt")
            os.rename("auxiliar.txt", "productos.txt")

        pausa()

    def detalle_productos(self):
        encontrado = False
        aux_codigo = input("Ingresa el código del producto que deseas consultar detalles: ")
        with open("productos.txt", "r") as mostrar:
            for linea in mostrar:
                datos = linea.split()
                if datos and datos[0] == aux_codigo:
                    encontrado = True
                    print("\n\nRegistro Encontrado\n\n")
                    print(f"Existencias: {datos[0]}\nNombre: {datos[1]}\nProveedor: {datos[4]}\n\n")
                    break

        if not encontrado:
            print(f"\n\nNo se encontró el registro: {aux_codigo}\n\n")

        pausa()

    def modificar_productos(self):
        encontrado = False
        coincidencia = False
        mismo_codigo = False
        aux_codigo = input("Ingresa el código del producto que deseas modificar: ")
        if aux_codigo == "":
            while aux_codigo == "":
                aux_codigo = input("Código del producto no válido!, intentalo nuevamente: ")

        codigo_modif = aux_codigo
        with open("productos.txt", "r") as lectura, open("productos.txt", "r") as verificador, open("auxiliar.txt",
                                                                                                  "w") as auxiliar:
            for linea in lectura:
                datos = linea.split()
                if datos and datos[0] == aux_codigo:
                    encontrado = True
                    self.mostar_registro(codigo_modif)

                    print("****************************************************")
                    print("\n\n")
                    print("INGRESE LA NUEVA INFORMACIÓN PARA EL PRODUCTO\n\n")
                    aux_codigo = input("Ingresa el código del producto: ")
                    if aux_codigo == codigo_modif:
                        mismo_codigo = True
                    if not mismo_codigo:
                        while True:
                            if aux_codigo == codigo_modif:
                                coincidencia = False
                                break
                            for linea_verif in verificador:
                                datos_verif = linea_verif.split()
                                if datos_verif and datos_verif[0] == aux_codigo:
                                    coincidencia = True
                                    print("\n\nYa existe un producto con ese código!\n\n")
                                    print(f"El producto con ese código es: {datos_verif[1]}\n\n")
                                    aux_codigo = input("Ingresa un código válido: ")
                                    if aux_codigo == "":
                                        while aux_codigo == "":
                                            aux_codigo = input("Código de producto no válido!, intentalo nuevamente: ")
                                    break
                            if not coincidencia:
                                break
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("***MODIFICAR LOS DATOS DEL PRODUCTO***\n\n")
                    print(f"Ingresa el código del PRODUCTO que deseas modificar: {codigo_modif}")





# Documentación Externa - Registro de Productos

## Descripción
Este programa en Python es un sistema básico de gestión de inventario que permite a los usuarios registrar, buscar, modificar y eliminar productos en un archivo de texto. El programa utiliza un archivo de texto llamado `productos.txt` para almacenar la información de los productos. Proporciona un menú de opciones para realizar diferentes acciones relacionadas con la gestión de productos.

## Funcionalidades Principales

### Registrar Producto
Permite al usuario agregar un nuevo producto al archivo `productos.txt`. Verifica si el código del producto ya existe y solicita al usuario que ingrese un código único si se encuentra una coincidencia.

### Buscar Producto
Permite al usuario buscar un producto específico por su código en el archivo `productos.txt` y muestra los detalles del producto si se encuentra.

### Modificar Producto
Permite al usuario modificar la información de un producto existente en el archivo `productos.txt`. Verifica si el nuevo código ya existe y solicita al usuario que ingrese un código único si se encuentra una coincidencia.

### Eliminar Producto
Permite al usuario eliminar un producto específico del archivo `productos.txt` según su código.

### Listar Productos
Muestra todos los productos registrados en el archivo `productos.txt` junto con su información detallada.

## Requisitos
El programa requiere que el archivo de texto `productos.txt` esté presente en la misma ubicación que el script de Python. Asegúrese de que el archivo tenga el formato de datos correcto para que el programa funcione sin problemas.

## Ejecución
El programa se ejecuta desde un entorno de Python y proporciona un menú interactivo para que el usuario elija diferentes opciones de gestión de productos. Para iniciar el programa, ejecute el script de Python y siga las instrucciones que aparecen en el menú.

## Dependencias
El código utiliza la biblioteca `os` de Python para limpiar la pantalla y manejar comandos específicos del sistema operativo. Asegúrese de que la biblioteca `os` esté instalada en su entorno de Python antes de ejecutar el programa.

## Contribuciones
Este programa puede ser mejorado y ampliado para incluir más funcionalidades y una interfaz de usuario más amigable. Se pueden agregar validaciones adicionales para garantizar la integridad de los datos ingresados por el usuario.

