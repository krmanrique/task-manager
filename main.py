from tarea.gestor import crear_tarea, listar_tareas

def menu():
  while True:
    print("\n1. Crear tarea\n2. Listar tareas\n5. Salir")
    opcion = input("Elige opción: ")
    if opcion == "1":
      desc = input("Descripción de la tarea: ")
      t = crear_tarea(desc)
      print("Tarea creada:", t.to_dict())
    elif opcion == "2":
      listar_tareas()
    elif opcion == "5":
      break

if __name__ == "__main__":
  menu()
