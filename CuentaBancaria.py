class CuentaBancaria:
    nombre_banco = "Banco Dojo"
    lista_cuentas = []

    def __init__(self, tasa_int, balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)

    def hacer_retiro(self, cantidad):
        if CuentaBancaria.puede_retirar(self.balance, cantidad):
            self.balance -= cantidad
        else :   
            print("No hay suficiente dinero")
        return self

    def hacer_deposito(self, cantidad):
        self.balance += cantidad
        return self

    def nueva_tasa (self, tasa_nueva):
        self.tasa_int = tasa_nueva
        print(f"Nueva Tasa:{tasa_nueva}")
        return self

    def generar_interes (self):
        print(f"Balance previo intereses: {self.balance}")
        if (self.balance > 0):
            self.balance = int (self.balance * (1 + (self.tasa_int/100)))

        print(f"Balance actual: {self.balance}")
        return self

    
    @classmethod
    def cambio_banco(cls, nombre):
        cls.nombre_banco = nombre

    @classmethod
    
    def imprimir_cuentas(cls):
        for cuenta in cls.lista_cuentas:
            cuenta.mostrar_balance_usuario()

    def mostrar_balance_usuario(self):
        print(f"Tasa: {self.tasa_int}, Balance: {self.balance}")
        return self
        
        
    def transfer_dinero(self, otra_cuenta, cantidad):
        
        if CuentaBancaria.puede_retirar(self.balance, cantidad):
            self.balance -= cantidad
            otra_cuenta.cuenta.balance += cantidad
        else:
            print("No hay suficiente dinero")
        return self

    @staticmethod
    def puede_retirar(balance, cantidad_retirar):
        if balance > cantidad_retirar:
            return True
        else :
            return False
        
    