from servicio import Servicio


class Asesoria(Servicio):
    def __init__(self, nivel):
        if nivel not in ["basico", "avanzado"]:
            raise ValueError("Nivel inválido")

        self.nivel = nivel

    def calcular_costo(self):
        return 50 if self.nivel == "basico" else 100

    def descripcion(self):
        return f"Asesoría {self.nivel}"


class ReservaSala(Servicio):
    def calcular_costo(self):
        return 80

    def descripcion(self):
        return "Reserva de sala"


class AlquilerEquipo(Servicio):
    def calcular_costo(self):
        return 120

    def descripcion(self):
        return "Alquiler de equipo"
