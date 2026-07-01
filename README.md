# Servidor Proxy de Cache

Español | [English](README.md)

Una solución robusta y modular en Python para implementar un **servidor proxy con mecanismo de almacenamiento en caché persistente**. Este proyecto intercepta las solicitudes HTTP dirigidas a un servidor de origen, almacena localmente las respuestas exitosas para optimizar los tiempos de carga y ofrece una interfaz de línea de comandos (CLI) para su administración.
# Servidor Proxy de Cache

[Español](README.es.md) | English

Una solución robusta y modular en Python para implementar un **servidor proxy con mecanismo de almacenamiento en caché persistente**. Este proyecto intercepta las solicitudes HTTP dirigidas a un servidor de origen, almacena localmente las respuestas exitosas para optimizar los tiempos de carga y ofrece una interfaz de línea de comandos (CLI) para su administración.

Proyecto desarrollado siguiendo las especificaciones del desafío [roadmap.sh/projects/caching-server](https://roadmap.sh/projects/caching-server).

---

## Características

* **Proxy totalmente transparente:** Permite redirigir dinámicamente cualquier ruta, método HTTP y parámetros de consulta al servidor de origen de forma segura.

* **Gestión eficiente de recursos estáticos:** Configuración robusta para capturar y servir sin problemas estilos CSS, JavaScript, imágenes y fuentes sin interferir con las rutas internas.

* **Caché persistente basada en JSON:** Almacenamiento local que se mantiene incluso después de reiniciar el servidor. Utiliza el hash SHA-256 de las solicitudes para generar nombres de archivo únicos y la codificación **Base64** para almacenar de forma segura el contenido binario.

* **Encabezados de diagnóstico de red:** Inserción automática del encabezado `X-Cache: HIT` (si el recurso se sirvió desde el almacenamiento local) o `X-Cache: MISS` (si se consultó al servidor de origen).

* **Arquitectura modular:** Separación estricta de responsabilidades entre el punto de entrada/CLI (`main.py`) y la lógica del servidor web (`server.py`).

---

## Requisitos previos

* Python 3.8 o superior
* Entorno virtual (venv) configurado e instalado

---

## Instalación y configuración

1. **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Aki-new/proxy-cache.git]
    cd proxy-cache
    
2. **Activar el entorno virtual e instalar las dependencias:**

    ```bash
    # En Windows:
    .venv\Scripts\activate
    # En macOS/Linux:
    source .venv/bin/activate
    # Instalar las dependencias necesarias (Flask y Requests)
    pip install -r requirements.txt
---
    
## Instrucciones de uso
El proyecto se gestiona completamente mediante la interfaz de línea de comandos (CLI) desde el archivo main.py.

1. **Iniciar el servidor proxy:**

    Para iniciar el proxy, se debe especificar la URL del servidor de origen. Opcionalmente, se puede proporcionar un puerto (el predeterminado es 5000):

    ```bash
    python main.py --port 3000 --origin https://www.python.org

2. **Verificar la funcionalidad de la caché:**
    Una vez que el servidor esté en funcionamiento, abra un navegador o utilice herramientas como curl o Postman para interactuar con él:

    * Solicitud inicial (MISS): Al acceder a http://localhost:3000/, se descargará el contenido del servidor de origen, se creará el archivo JSON local en la carpeta .cache/ y se responderá incluyendo el encabezado X-Cache: MISS.
    
    * Solicitudes subsiguientes (HIT): Recargar la página o solicitar el mismo recurso resultará en una respuesta instantánea utilizando el archivo local, incluyendo el encabezado X-Cache: HIT.
    
3. **Borrar caché persistente:**
Para vaciar completamente el almacenamiento local y eliminar la carpeta .cache/, ejecute el comando con la opción `--clear-cache`:

``` bash
python main.py --clear-cache