from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor: str,num_tarjeta :str) -> None:
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = num_tarjeta
        
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    
    def _crear_nueva_membresia(self, nueva_membresia : int):
        if nueva_membresia == 1:
            return MembresiaBasica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return MembresiaFamiliar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return MembresiaSinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return MembresiaPro(self.correo_suscriptor, self.numero_tarjeta)
    
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia : int):
        pass
    
    @abstractmethod
    def cancelar_suscripcion(self, nueva_membresia : int):
        pass
class MembresiaGratis(Membresia):
    costo = 0
    cantidad_dispositivos = 1
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 and nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    def  cancelar_suscripcion(self):
        pass
    
class MembresiaBasica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2
    
    def __init__(self, correo_suscriptor: str, num_tarjeta: str) -> None:
        super().__init__(correo_suscriptor, num_tarjeta)
        if isinstance(self, MembresiaFamiliar) or isinstance(self, MembresiaSinConexion):
            self.dias_regalo = 7
        elif isinstance(self,MembresiaPro):
            self.dias_regalo = 15
    
    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_suscriptor, self.numero_tarjeta)
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia <2 or nueva_membresia>4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
            
class MembresiaFamiliar(MembresiaBasica):
    costo = 5000
    cantidad_dispositivos = 5
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1,3,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    
    
class MembresiaSinConexion(MembresiaBasica):
    costo = 3500
    cantidad_dispositivos = 2
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1,2,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
        
    def incrementar_cantidad_contenido(self):
        pass
    
class MembresiaPro(MembresiaFamiliar, MembresiaSinConexion):
    costo = 7000
    cantidad_dispositivos = 6
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


gratis = MembresiaGratis("asd@asd.cl","1234")
print(type(gratis))

basica = gratis.cambiar_suscripcion(1)
print(type(basica))

familiar = basica.cambiar_suscripcion(2)
print(type(familiar))

sin_conexion = familiar.cambiar_suscripcion(3)
print(type(sin_conexion))

pro = familiar.cambiar_suscripcion(4)
print(type(pro))

cancelar = pro.cancelar_suscripcion()
print(type(cancelar))

print(cancelar.correo_suscriptor)
print(cancelar.numero_tarjeta)