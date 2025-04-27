import json
import uuid
import os
from tarea.modelos import Tarea #clase Tarea de modelos.py

RUTA = os.path.join("data", "tareas.json") #ruta de la carpeta data y el archivo tareas.json

def cargar_tareas():
  if not os.path.exists(RUTA):
    return []
  with open(RUTA, "r") as f: # Open()=función para abrir archivo "r"=lectura, "f"= file
    datos = json.load(f) #Convierte el JSON en un objeto de Python
  return [Tarea.from_dict(d) for d in datos]


def guardar_tareas(lista):
  with open(RUTA, "w") as f: # w= write
    json.dump([t.to_dict() for t in lista], f, indent=2) #dump=guardar obje en file json, indet= define bloques de codigos

def crear_tarea(descripcion):
  tareas = cargar_tareas()
  tarea_id = str(uuid.uuid4()) 
  nueva = Tarea(descripcion=descripcion, id=tarea_id) 
  tareas.append(nueva)
  guardar_tareas(tareas)
  return nueva

def listar_tareas():
  tareas = cargar_tareas()
  for t in tareas:
    estado = "✅" if t.completada else "❌"
    print(f"{t.id} - {t.descripcion} - Completada: {estado}")

def marcar_como_completada(id_tarea):
  tareas = cargar_tareas()
  for t in tareas:
    if t.id == id_tarea:
      t.completada = True
      guardar_tareas(tareas)
      return t
  return None

def eliminar_tarea(id_tarea):
  tareas = cargar_tareas()
  for i, t in enumerate(tareas):
    if t.id == id_tarea:
      tareas.pop(i)
      guardar_tareas(tareas)
      return True
  return False

