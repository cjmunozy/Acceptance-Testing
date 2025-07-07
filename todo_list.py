class Tarea:
    
    def __init__(self, nombre, descripcion, encargado, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.encargado = encargado
        self.estado = estado
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def cambiarEstado(self, estado):
        self.estado = estado
    
    def getNombre(self):
        return self.nombre

todo_list = []

def crearTarea(nombre, descripcion, encargado, estado):
    return Tarea(nombre, descripcion, encargado, estado)

def agregarTarea(tarea):
    todo_list.append(tarea)

def listarTareas():
    print("Tareas:")
    for tarea in todo_list:
        print("- " + tarea.getNombre())

def tacharTarea(tarea):
    if tarea in todo_list:
        tarea.cambiarEstado("Completada")

def limpiarLista():
    todo_list.clear
