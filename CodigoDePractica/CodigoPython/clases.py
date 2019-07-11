# Una clase es como un plano para crear objetos tiene propiedades
#Create a class
class Usuario:
#constructor (funcion que corre cuando hacesuna instalacion de u)
  def __init__(self,nombre,email,edad):
      self.nombre = nombre
      self.email = email
      self.edad = edad
      self.saldo = 0

  def establecer_saldo(self,saldo):
      self.saldo = saldo  
  def saludos(self,num1=1):
      print(num1)
      return "Me llamo{0} y tengo{1}" .format(self.nombre,self.edad)
  def tengo_cumple(self):
      self.edad+=1 

#Init un objeto para el usuario
Mayra = Usuario('Mayra Vazquez','mayralin_81@hotmail.com',21)
print(type(Mayra))
print(Mayra.nombre)
print(Mayra.saludos("d"))

#Init un cliente

Rufina_usuario = usuario('Rufina Madrid', 'rufina@yahoo.com',2)
Rufina_cliente = cliente('Rufina Madrid', 'rufina@yahoo.com' ,2)
Rufina_cliente.establecer_saldo(5e10)
print(Rufina_cliente.saludos())
print(Rufina_usuario.saludos())

