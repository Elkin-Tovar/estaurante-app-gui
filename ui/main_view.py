import tkinter as tk
from tkinter import messagebox


class MainView(tk.Frame):
    """
    Interfaz principal del restaurante para visualizar productos y usuarios registrados.
    """

    def __init__(self, parent, controlador, servicio) -> None:
        super().__init__(parent)
        self.controlador = controlador
        self.servicio = servicio

        self.configure(bg="#f4f4f4")

        # Barra superior
        frame_top = tk.Frame(self, bg="#333333", height=50)
        frame_top.pack(fill="x", side="top")

        lbl_header = tk.Label(
            frame_top, text="Panel Principal - Restaurante App", font=("Arial", 14, "bold"), bg="#333333", fg="white"
        )
        lbl_header.pack(side="left", padx=15, pady=10)

        btn_salir = tk.Button(
            frame_top, text="Cerrar Sesión", font=("Arial", 10), bg="#d9534f", fg="white", command=self.controlador.mostrar_login_view
        )
        btn_salir.pack(side="right", padx=15, pady=10)

        # Cuerpo central con secciones de visualización
        frame_content = tk.Frame(self, bg="#f4f4f4")
        frame_content.pack(fill="both", expand=True, padx=20, pady=20)

        # Sección Productos
        frame_prod = tk.LabelFrame(frame_content, text=" Productos Registrados ", font=("Arial", 11, "bold"), bg="#f4f4f4", padx=10, pady=10)
        frame_prod.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.txt_productos = tk.Text(frame_prod, font=("Arial", 10), width=35, height=15)
        self.txt_productos.pack(fill="both", expand=True, pady=5)

        btn_cargar_prod = tk.Button(
            frame_prod, text="Actualizar Productos", font=("Arial", 10, "bold"), bg="#008CBA", fg="white", command=self._cargar_productos_ui
        )
        btn_cargar_prod.pack(pady=5)

        # Sección Usuarios
        frame_user = tk.LabelFrame(frame_content, text=" Usuarios Registrados ", font=("Arial", 11, "bold"), bg="#f4f4f4", padx=10, pady=10)
        frame_user.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.txt_usuarios = tk.Text(frame_user, font=("Arial", 10), width=35, height=15)
        self.txt_usuarios.pack(fill="both", expand=True, pady=5)

        btn_cargar_user = tk.Button(
            frame_user, text="Actualizar Usuarios", font=("Arial", 10, "bold"), bg="#008CBA", fg="white", command=self._cargar_usuarios_ui
        )
        btn_cargar_user.pack(pady=5)

        # Sección inferior de funciones futuras
        frame_footer = tk.Frame(self, bg="#e0e0e0", height=40)
        frame_footer.pack(fill="x", side="bottom")
        lbl_futuro = tk.Label(frame_footer, text="Módulo de Ventas y otras funciones: [ Funcionalidades pendientes para siguientes semanas ]", font=("Arial", 9, "italic"), bg="#e0e0e0", fg="#555555")
        lbl_futuro.pack(pady=10)

        # Cargar datos iniciales automáticamente al abrir la vista
        self._cargar_productos_ui()
        self._cargar_usuarios_ui()

    def _cargar_productos_ui(self) -> None:
        """Limpia e inserta los productos obtenidos desde el servicio."""
        self.txt_productos.delete("1.0", tk.END)
        productos = self.servicio.obtener_productos()
        if not productos:
            self.txt_productos.insert(tk.END, "No hay productos registrados o el archivo JSON está vacío.")
        else:
            for p in productos:
                self.txt_productos.insert(tk.END, f"• {p.mostrar_informacion()}\n\n")

    def _cargar_usuarios_ui(self) -> None:
        """Limpia e inserta los usuarios obtenidos desde el servicio."""
        self.txt_usuarios.delete("1.0", tk.END)
        usuarios = self.servicio.obtener_usuarios()
        if not usuarios:
            self.txt_usuarios.insert(tk.END, "No hay usuarios registrados o el archivo JSON está vacío.")
        else:
            for u in usuarios:
                self.txt_usuarios.insert(tk.END, f"• {u.mostrar_informacion()}\n\n")