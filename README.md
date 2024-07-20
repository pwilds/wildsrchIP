# wildsrchIP

wildsrchIP es una aplicación web desarrollada con Flask que permite buscar información sobre una dirección IP utilizando la API de `geo.ipify.org`. La aplicación proporciona detalles como la ubicación y si la IP está asociada con una VPN.

## Requisitos

- Python 3.7 o superior
- Flask
- requests

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/wildsrchIP.git
cd wildsrchIP
```

2. Crea un entorno virtual y activa el entorno:

```bash
python -m venv venv
source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación Flask:

```bash
python app.py
```

2. Abre tu navegador y ve a `http://127.0.0.1:5000`.

## Rutas

- `GET /`: Página de inicio donde se puede ingresar una dirección IP para buscar información.
- `POST /buscar`: Realiza la búsqueda de la información de la dirección IP ingresada.

## Archivos

- `app.py`: Archivo principal de la aplicación Flask.
- `templates/index.html`: Plantilla HTML para la página de inicio.
- `templates/resultado.html`: Plantilla HTML para mostrar los resultados de la búsqueda.

## Ejemplo de Uso

1. Ingresar una dirección IP en la página de inicio y hacer clic en el botón de búsqueda.
2. La aplicación mostrará información sobre la dirección IP ingresada (ubicación, proveedor de servicios de Internet, si está asociada con una VPN, etc.).

## API

La aplicación utiliza la API de `geo.ipify.org` para obtener información sobre direcciones IP. Necesitas una clave de API que puedes obtener registrándote en [geo.ipify.org](https://geo.ipify.org/).

Reemplaza `api_key` en `app.py` con tu propia clave de API.

```python
api_key = 'tu_api_key'
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---
