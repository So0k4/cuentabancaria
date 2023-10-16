class CuentaBancaria:
    tasa_de_interés = 0.01
    balance = 0

    def __init__(self, tasa_de_interés, balance):
        self.tasa_de_interés = tasa_de_interés
        self.balance = balance

    def depósito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        self.balance -= monto
        return self

    def mostrar_info_cuenta(self):
        print(f"Tasa de interés: {self.tasa_de_interés}, Balance: {self.balance}")
        return self

    def generar_interés(self):
        self.balance += self.balance * self.tasa_de_interés
        return self

    @classmethod
    def mostrar_info_cuenta_todas(cls):
        for cuenta in cls.__dict__.values():
            if isinstance(cuenta, CuentaBancaria):
                print(f"Tasa de interés: {cuenta.tasa_de_interés}, Balance: {cuenta.balance}")

cuenta1 = CuentaBancaria(0.01, 100)
cuenta2 = CuentaBancaria(0.02, 200)

cuenta1.depósito(50).depósito(100).depósito(150).retiro(50).generar_interés().mostrar_info_cuenta()
cuenta2.depósito(100).depósito(200).retiro(50).retiro(100).retiro(50).retiro(100).generar_interés().mostrar_info_cuenta()

CuentaBancaria.mostrar_info_cuenta_todas()