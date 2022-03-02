from User2 import User
from CuentaBancaria import CuentaBancaria


Violeta= User("Violeta Rojas",{"Ahorro":CuentaBancaria(4,5000)})
Nancy= User("Nancy Rojas", {"Ahorro":CuentaBancaria(6,1000), "Viajes":CuentaBancaria(-3,1000), "Estudios Hijos": CuentaBancaria(20, 20000)})


# Violeta.mostrar_balance_cuenta("Ahorro")
# Nancy.mostrar_balance_cuenta("Ahorro")
# Nancy.mostrar_balance_cuenta("Viajes")
Violeta.cuenta["Ahorro"].generar_interes().mostrar_balance_usuario()
Nancy.cuenta["Ahorro"].generar_interes().mostrar_balance_usuario()
Nancy.cuenta["Viajes"].generar_interes().mostrar_balance_usuario()
Nancy.cuenta["Estudios Hijos"].generar_interes().mostrar_balance_usuario()




