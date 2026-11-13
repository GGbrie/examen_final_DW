# API REST de Vehículos

Proyecto académico desarrollado con **Python, Django, Django REST Framework y MySQL/MariaDB**.
Permite gestionar vehículos mediante operaciones CRUD en formato JSON, **sin autenticación**.

## Tecnologías

- Python 3.10
- Django 4.2 LTS
- Django REST Framework 3.15
- MySQL / MariaDB (XAMPP)
- django-cors-headers
- mysqlclient

## Funcionalidades

- Crear vehículos con `POST`.
- Listar todos los vehículos con `GET`.
- Consultar un vehículo por ID con `GET`.
- Actualizar un vehículo con `PUT` (y parcialmente con `PATCH`).
- Eliminar un vehículo con `DELETE`.
- Validación de campos obligatorios con respuestas JSON y código HTTP 400.
- CORS habilitado para consumir la API desde React.

## Requisitos previos

1. Tener instalado Python 3.10 o superior.
2. Tener MySQL o MariaDB iniciado en `127.0.0.1:3306`.
3. Usuario `root` sin contraseña (configuración local del proyecto).

## Instalación

Abre una terminal en la carpeta del proyecto y ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

> Si pip muestra un error de certificado SSL, usa:
>
> ```powershell
> .\.venv\Scripts\python.exe -m pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
> ```

## Crear la base de datos

El script `crear_bd.py` crea automáticamente la base `serie4_vehiculos_db` si no existe:

```powershell
.\.venv\Scripts\python.exe crear_bd.py
```

## Aplicar migraciones

```powershell
.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate
```

## Ejecutar el servidor

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

La API estará disponible en:

```text
http://127.0.0.1:8000/api/vehiculos/
```

## Endpoints

| Método | URL | Acción | Código esperado |
|---|---|---|---|
| POST | `/api/vehiculos/` | Crear un vehículo | 201 Created |
| GET | `/api/vehiculos/` | Listar todos | 200 OK |
| GET | `/api/vehiculos/<id>/` | Consultar uno por ID | 200 OK |
| PUT | `/api/vehiculos/<id>/` | Actualizar completo | 200 OK |
| PATCH | `/api/vehiculos/<id>/` | Actualizar parcial | 200 OK |
| DELETE | `/api/vehiculos/<id>/` | Eliminar | 204 No Content |

### Ejemplo de creación

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "anio": 2022,
  "color": "Rojo"
}
```

## Documentación de apoyo

- `ENTREGABLE_GUIA.md`: las 6 pruebas obligatorias con JSON listos para copiar.
- `LABORATORIO_THUNDER_CLIENT.md`: ejemplos adicionales para practicar el CRUD.

## Modelo `Vehiculo`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | BigAutoField | Llave primaria automática |
| `marca` | CharField(100) | Marca, obligatoria y no vacía |
| `modelo` | CharField(100) | Modelo, obligatorio y no vacío |
| `anio` | IntegerField | Año, obligatorio |
| `color` | CharField(50) | Color, obligatorio y no vacío |
| `created_at` | DateTimeField | Fecha de creación automática |
| `updated_at` | DateTimeField | Fecha de actualización automática |

## Nota de seguridad

Este proyecto usa la configuración local solicitada para una práctica académica:
`DEBUG = True`, usuario `root` sin contraseña y la `SECRET_KEY` de desarrollo incluida.
No debe utilizarse tal cual en producción.
