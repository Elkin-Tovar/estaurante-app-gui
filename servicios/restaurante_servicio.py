from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """
    Servicio que administra la lógica de negocio, procesa los datos cargados
    y valida el acceso simulado al sistema.
    """

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: List[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: List[Usuario] = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario: str, clave: str) -> bool:
        """
        Simulación pedagógica de acceso: permite el ingreso si se ingresan
        credenciales no vacías (ej. admin / 1234 o cualquier usuario registrado).
        """
        if not usuario.strip() or not clave.strip():
            return False
        # Simulación válida para la práctica de UI
        return True

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self.usuarios