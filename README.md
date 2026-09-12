# Sistema de Restaurante (restaurante_app) - Semana 13

## **Autor**
* **Elkin Esteban Tovar Caicedo**

## **Propósito del Sistema**
Evolución del proyecto `restaurante_app` correspondiente a la Semana 13. Se inicia la transición desde una aplicación basada en consola hacia una aplicación de escritorio con **Interfaz Gráfica de Usuario (GUI)** utilizando **Tkinter**, manteniendo una separación limpia de responsabilidades mediante una arquitectura modular organizada en capas.

## **Estructura del Proyecto**
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

Responsabilidad de los Componentes
modelos/: Contienen las clases base Producto y Usuario para representar las entidades del dominio.

servicios/:

archivo_servicio.py: Centraliza la lectura de los datos locales desde archivos JSON.

restaurante_servicio.py: Administra la lógica de negocio, procesa los datos para las vistas y gestiona la validación de acceso simulado.

ui/:

login_view.py: Pantalla gráfica de acceso simulado construida con componentes de Tkinter.

main_view.py: Interfaz principal que permite visualizar los productos y usuarios registrados, con botones para actualizar dinámicamente la información y cerrar sesión.

main.py: Punto de entrada que inicializa una única ventana principal de Tkinter y gestiona la alternancia entre las vistas de acceso y el panel principal.

Flujo de la Aplicación
Inicio: Se ejecuta main.py y se muestra la pantalla de acceso (LoginView).

Autenticación: Se ingresan las credenciales y el servicio valida el acceso.

Interfaz Principal: Tras un ingreso exitoso, se despliega la MainView, desde donde se consultan los productos y usuarios cargados desde los archivos JSON.

Cierre de Sesión: Permite regresar de forma limpia a la pantalla de login dentro de la misma ventana de ejecución.

Instrucciones para Ejecutar
Asegúrate de contar con los archivos JSON de prueba dentro de la carpeta datos/.

Abre una terminal en la raíz del proyecto.

Ejecuta el comando:

Bash
python main.py
