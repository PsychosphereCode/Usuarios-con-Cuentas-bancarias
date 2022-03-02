from CuentaBancaria import CuentaBancaria

class User:

    def __init__(self, nombre, cuentas):
        self.nombre = nombre
        self.cuenta = {}
        self.cuenta.update(cuentas)

    def mostrar_balance_cuenta(self, cuenta_especifica):
        self.cuenta[cuenta_especifica].mostrar_balance_usuario()
        return self



