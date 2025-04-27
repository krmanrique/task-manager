from tarea.gestor import crear_tarea, listar_tareas, marcar_como_completada, eliminar_tarea

def menu():
  while True:
    print("\n1. Crear tarea\n2. Listar tareas\n3. Marcar tarea como completada\n4. Eliminar tarea\n5. Salir")
    opcion = input("Elige opción: ")
    if opcion == "1":
      desc = input("Descripción de la tarea: ")
      t = crear_tarea(desc)
      print("Tarea creada:", t.to_dict())
    elif opcion == "2":
      listar_tareas()
    elif opcion == "3":
      id_t = input("ID de la tarea a completar: ")
      if marcar_como_completada(id_t):
        print("Tarea marcada como completada.")
      else:
        print("Tarea no encontrada.")
    elif opcion == "4":
      id_t = input("ID de la tarea a eliminar: ")
      if eliminar_tarea(id_t):
        print("Tarea eliminada.")
      else:
        print("Tarea no encontrada.")
    elif opcion == "5":
      break

if __name__ == "__main__":
  menu()