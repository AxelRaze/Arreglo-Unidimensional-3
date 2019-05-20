Arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
class Arreglo3:
    """Mostrar el arrreglo en el siguiente orden: el primero,
    el último, el segundo, el penúltimo, el tercero, etc."""
    def Mostrar_Arreglo(self):
        for f in range(0, int((len(Arreglo))/2)):
            print(Arreglo[f], "\t", end="")
            print(len(Arreglo) - f, "\t", end="")
orden = Arreglo3()
orden.Mostrar_Arreglo()