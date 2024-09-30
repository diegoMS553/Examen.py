from abc import ABC, abstractmethod

class SalarioInvalidoException(Exception):
    pass

class Empleado_DSC27(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self._rfc = rfc
        self._apellidos = apellidos
        self._nombres = nombres
    
    @abstractmethod
    def calcular_sueldo_neto(self):
        pass
    
    def mostrar_informacion(self):
        return f"RFC: {self._rfc}, Apellidos: {self._apellidos}, Nombres: {self._nombres}"

class EmpleadoVendedor_DSC27(Empleado_DSC27):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self._monto_vendido = monto_vendido
        self._tasa_comision = tasa_comision
        
        if self.calcular_sueldo_neto() < 150:
            raise SalarioInvalidoException("El sueldo no puede ser menor al salario mínimo de 150 pesos.")

    def calcular_ingresos(self):
        return self._monto_vendido * self._tasa_comision

    def calcular_bonificacion(self):
        if self._monto_vendido < 1000:
            return 0
        elif 1000 <= self._monto_vendido <= 5000:
            return self.calcular_ingresos() * 0.05
        else:
            return self.calcular_ingresos() * 0.10

    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return ingresos * 0.11
        else:
            return ingresos * 0.15

    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return ingresos + bonificacion - descuento

class EmpleadoPermanente_DSC27(Empleado_DSC27):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self._sueldo_base = sueldo_base
        self._numero_seguro_social = numero_seguro_social

        if self.calcular_sueldo_neto() < 150:
            raise SalarioInvalidoException("El sueldo no puede ser menor al salario mínimo de 150 pesos.")

    def calcular_ingresos(self):
        return self._sueldo_base

    def calcular_descuento(self):
        return self._sueldo_base * 0.11

    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        descuento = self.calcular_descuento()
        return ingresos - descuento

def calcular_plantilla_empleados(empleados):
    for empleado in empleados:
        print(empleado.mostrar_informacion())
        print(f"Sueldo neto: {empleado.calcular_sueldo_neto()}\n")

try:
    vendedor = EmpleadoVendedor_DSC27("RFC001", "García", "Pedro", 1200, 0.05)
    permanente = EmpleadoPermanente_DSC27("RFC002", "López", "Ana", 5000, "123456789")

    empleados = [vendedor, permanente]
    calcular_plantilla_empleados(empleados)

except SalarioInvalidoException as e:
    print(e)
