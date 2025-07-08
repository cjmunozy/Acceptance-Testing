class Task:

    def __init__(self, nombre, descripcion, encargado, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.encargado = encargado
        self.estado = estado

    @classmethod
    def desde_nombre(cls, nombre):
        return cls(nombre, nombre, "", "Pendiente")

    @classmethod
    def desde_nombre_y_estado(cls, nombre, estado):
        return cls(nombre, nombre, "", estado)

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.nombre == other.nombre
        return False

    def cambiar_estado(self, estado):
        self.estado = estado

    def get_nombre(self):
        return self.nombre


todo_list = []


def crear_tarea(nombre, descripcion, encargado, estado):
    return Task(nombre, descripcion, encargado, estado)


def agregar_tarea(tarea):
    todo_list.append(tarea)


def listar_tareas():
    partes = []
    for tarea in todo_list:
        partes.append("- " + tarea.get_nombre())
    return "Tasks:\n" + "\n".join(partes)


def tachar_tarea(tarea):
    if tarea in todo_list:
        tarea.cambiarEstado("Completada")


def limpiar_lista(todo_list):
    todo_list.clear()
