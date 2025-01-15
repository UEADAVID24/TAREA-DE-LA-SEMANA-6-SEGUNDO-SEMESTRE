# Clase Base
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca  # Atributo encapsulado
        self.modelo = modelo
        self.anio = anio

    # Método Encapsulado
    def __get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    # Método de acción común
    def arrancar(self):
        print(f"{self.__get_marca()} {self.modelo} arrancó.")

    def detener(self):
        print(f"{self.__get_marca()} {self.modelo} se detuvo.")

# Clase Derivada (Herencia)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_motor):
        super().__init__(marca, modelo, anio)
        self.tipo_motor = tipo_motor

    # Sobrescribir el método arrancar (Polimorfismo)
    def arrancar(self):
        print(f"El automóvil {self._Vehiculo__get_marca()} {self.modelo}, con motor {self.tipo_motor}, arrancó.")

# Clase Derivada (Herencia)
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_moto):
        super().__init__(marca, modelo, anio)
        self.tipo_moto = tipo_moto

    # Sobrescribir el método arrancar (Polimorfismo)
    def arrancar(self):
        print(f"La motocicleta {self._Vehiculo__get_marca()} {self.modelo}, tipo {self.tipo_moto}, arrancó.")

# Crear instancias y demostrar la funcionalidad
if __name__ == "__main__":
    # Crear instancias de los vehículos
    auto1 = Automovil("Toyota", "Corolla", 2020, "Híbrido")
    moto1 = Motocicleta("Yamaha", "MT-09", 2022, "Deportiva")

    # Llamar a los métodos
    auto1.arrancar()  # Polimorfismo: Método sobrescrito
    moto1.arrancar()  # Polimorfismo: Método sobrescrito

    # Acceder al atributo encapsulado correctamente
    print(f"La marca del automóvil es: {auto1._Vehiculo__get_marca()}")
    moto1.set_marca("Honda")
    print(f"La marca de la motocicleta es: {moto1._Vehiculo__get_marca()}")
