import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:
    """
    Servicio encargado de leer los datos locales desde archivos JSON.
    """

    def __init__(self) -> None:
        self.dir_datos = "datos"

    def cargar_productos(self, ruta: str = "datos/productos.json") -> List[Producto]:
        productos = []
        if not os.path.exists(ruta):
            return productos
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        productos.append(Producto(
                            item["codigo"],
                            item["nombre"],
                            item["categoria"],
                            float(item["precio"]),
                            int(item["stock"])
                        ))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return productos

    def cargar_usuarios(self, ruta: str = "datos/usuarios.json") -> List[Usuario]:
        usuarios = []
        if not os.path.exists(ruta):
            return usuarios
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        usuarios.append(Usuario(
                            item["identificacion"],
                            item["nombre"],
                            item["correo"]
                        ))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return usuarios