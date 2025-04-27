import uuid #identificador unico

class Tarea:
  def __init__ (self, descripcion, completada=False, id=None):
    self.id = id if id else str(uuid.uuid4()) #referenciar atribu
    self.descripcion = descripcion
    self.completada = completada

  def to_dict(self): # Metodo - atributos en diccionario
    return {"id": str(self.id), "descripcion": self.descripcion, "completada": self.completada} #json
  
  @staticmethod #clase en metodo Es.
  def from_dict(data): #data = diccionario
    return Tarea(data["descripcion"], data["completada"], data["id"]) #[aceder al Valor del diccionario]
  
