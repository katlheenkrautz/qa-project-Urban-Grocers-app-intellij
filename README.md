# Proyecto Urban Grocers
## Descripción
Este proyecto automatiza las pruebas para la creación de kits de productos en la aplicación Urban Grocers utilizando 
Python y la librería `pytest` para las pruebas. El flujo de trabajo incluye la creación de un usuario, la obtención de 
un token de autenticación y la creación de un kit de productos, validando tanto las pruebas positivas como negativas.

## Estructura del Proyecto

- `configuration.py`: Almacena las URLs y rutas de solicitud.
- `data.py`: Contiene los cuerpos de las solicitudes POST.
- `sender_stand_request.py`: Contiene las funciones para enviar solicitudes.
- `create_kit_name_kit_test.py`: Contiene las pruebas automatizadas.
- `README.md`: Documentacion del proyecto
- `.gitignore`: Ignora archivos innecesarios.

## Ejecución de las Pruebas
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta las pruebas: `pytest create_kit_name_kit_test.py -v`.


## Tecnologías Utilizadas
- **Python**: Lenguaje de programación principal.
- **Pytest**: Framework para la ejecución de pruebas.
- **Requests**: Librería para enviar solicitudes HTTP.

