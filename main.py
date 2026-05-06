from cliente import Cliente
from servicios_especificos import Asesoria, ReservaSala
from reserva import Reserva


print("===== CASO CORRECTO =====")
cliente1 = Cliente("Juan", "juan@gmail.com")
servicio1 = Asesoria("basico")

r1 = Reserva(cliente1, servicio1)
r1.confirmar()
r1.cancelar()


print("===== ERROR DATOS =====")
r2 = Reserva(None, None)
r2.confirmar()


print("===== ERROR SERVICIO =====")
try:
    servicio_error = Asesoria("medio")
except Exception as e:
    print("❌ Error:", e)


print("===== ERROR CANCELAR =====")
cliente3 = Cliente("Maria", "maria@gmail.com")
servicio3 = ReservaSala()

r3 = Reserva(cliente3, servicio3)
r3.cancelar()
