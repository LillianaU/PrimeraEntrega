"""
paso este ejemplo de clase a python
class Usuario {
  +int DNI
  +String Nombre1
  +String Nombre2
  +String Apellido1
  +String Apellido2
  +String Direccion
  +String Email
  +insertar()
  +modificar()
  +eliminar()
  +buscar()
}
"""
class usuario:
    def __init__(self,DNI,nombre1,nombre2,apellido1, apellido2,direccion,email):
        self.DNI = DNI
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 =apellido2
        self.direccion = direccion
        self.email = email
    # simular los metodos como un crud
    def insertar(self):
        print(f"Usuario {self.nombre1} {self.apellido1} insertado correctamente.")
    def modificar(self):
        print(f"Usuario {self.nombre1} {self.apellido1} modificado correctamente.")
    def eliminar(self):
        print(f"Usuario {self.nombre1} {self.apellido1} eliminado correctamente.")
    def buscar(self):
        print(f"Buscando usuario {self.nombre1} {self.apellido1}")

# crear herencia del proveedor
class Proveedor:
    def __init__(self,DNI, nombre1, nombre2, apellido1, apellido2, direccion, email, contacto):
        super().__init__(DNI, nombre1, nombre2, apellido1, apellido2, direccion, email)
        self.contacto = contacto
    # sobreescribir el metodo insertar
    def insertar(self):
        print(f"Proveedor {self.nombre1} {self.apellido1} insertado correctamente.")
    # agregar nuevo metodo para proveedor
    def contactar(self):
        print(f"Contactando al proveedor {self.nombre1} {self.apellido1} con el contacto {self.contacto}")
        
