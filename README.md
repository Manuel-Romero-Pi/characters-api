# Items API - FastAPI

API REST desarrollada con FastAPI para gestionar items de personajes de Star Wars. Los datos se almacenan en memoria durante la ejecución de la aplicación.

## Características

- Consultar todos los items almacenados
- Buscar items por nombre
- Agregar nuevos items
- Eliminar items por ID
- Validación automática de datos con Pydantic
- Documentación interactiva automática (Swagger UI y ReDoc)

## Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd characters-api
```

2. Crear y activar un ambiente virtual:

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la API en modo desarrollo:

```bash
uvicorn app:app --reload
```

La API estará disponible en: `http://localhost:8000`

## Documentación

Una vez que la API esté ejecutándose, puedes acceder a la documentación interactiva:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints Disponibles

### GET /items/getAll
Obtiene todos los items almacenados. Retorna solo los campos: id, name, height, mass, birth_year.

**Ejemplo de respuesta:**
```json
[
    {
        "id": 1,
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "birth_year": null
    }
]
```

### GET /items/get/{name}
Busca items por nombre (búsqueda case-insensitive). Retorna todos los campos del item.

**Parámetros:**
- `name` (path): Nombre del personaje a buscar

**Ejemplo:**
```
GET /items/get/Luke Skywalker
```

### POST /items/add
Agrega un nuevo item. Todos los campos son requeridos excepto birth_year.

**Body (JSON):**
```json
{
    "id": 9,
    "name": "Yoda",
    "height": 66,
    "mass": 17,
    "hair_color": "white",
    "skin_color": "green",
    "eye_color": "brown",
    "birth_year": null
}
```

**Validaciones:**
- Todos los campos son requeridos (excepto birth_year)
- El id debe ser único
- Los tipos de datos deben ser correctos

**Códigos de respuesta:**
- `201`: Item creado exitosamente
- `400`: El item con ese id ya existe
- `422`: Error de validación (campos faltantes, tipos incorrectos, etc.)

### DELETE /items/delete/{id}
Elimina un item por su ID.

**Parámetros:**
- `id` (path): ID del item a eliminar

**Ejemplo:**
```
DELETE /items/delete/1
```

**Códigos de respuesta:**
- `200`: Item eliminado exitosamente
- `400`: El item con ese id no existe

## Estructura del Proyecto

```
backend-path-level-1/
├── app.py                 # Archivo principal de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── services/             # Lógica de negocio
│   ├── __init__.py
│   └── item_service.py   # Servicios para manejar items
├── schemas/              # Esquemas de validación (Pydantic)
│   ├── __init__.py
│   └── item.py           # Modelos de datos
└── routes/               # Rutas de la API
    ├── __init__.py
    └── items.py          # Endpoints de items
```

## Estructura de Datos

Cada item tiene la siguiente estructura:

```json
{
    "id": 1,
    "name": "Luke Skywalker",
    "height": 172,
    "mass": 77,
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": null
}
```

**Tipos de datos:**
- `id`: integer (único, requerido)
- `name`: string (requerido)
- `height`: integer (requerido)
- `mass`: integer (requerido)
- `hair_color`: string (requerido)
- `skin_color`: string (requerido)
- `eye_color`: string (requerido)
- `birth_year`: string | null (opcional)

## Datos Iniciales

La API viene pre-cargada con 8 personajes de Star Wars:
1. Luke Skywalker
2. R2-D2
3. C-3PO
4. Darth Vader
5. Leia Organa
6. Owen Lars
7. Beru Whitesun lars
8. R5-D4

## Notas Importantes

- Los datos se almacenan en memoria durante la ejecución. Al reiniciar el servidor, los cambios se perderán y se restaurarán los datos iniciales.
- El campo `birth_year` es opcional y puede ser `null`.
- La búsqueda por nombre es case-insensitive.
- Todos los campos son validados automáticamente por FastAPI usando Pydantic.

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para construir APIs
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Pydantic**: Validación de datos usando tipos de Python

## Autor

Desarrollado como parte del curso Backend Path - Nivel 1

