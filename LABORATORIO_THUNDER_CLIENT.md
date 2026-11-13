# Laboratorio: probar el CRUD de Vehículos en Thunder Client

Esta guía es para practicar y entender qué hace cada método HTTP. La API ya tiene un
vehículo con **ID 1** (Toyota Corolla), por lo que los siguientes POST crearán los IDs 2, 3, etc.

## Recordatorio de los métodos

| Método | Para qué sirve | Código esperado |
|---|---|---|
| `POST` | Crear un vehículo nuevo | 201 Created |
| `GET` | Listar todos o consultar uno por ID | 200 OK |
| `PUT` | Reemplazar/actualizar un vehículo completo | 200 OK |
| `PATCH` | Actualizar solo algunos campos (opcional) | 200 OK |
| `DELETE` | Eliminar un vehículo | 204 No Content |

En Thunder Client: elige el método, escribe la URL, ve a **Body → JSON**, pega el cuerpo
y pulsa **Send**. Para GET y DELETE no se envía cuerpo.

---

## Experimento 1: crear dos vehículos más

### 1.1 Crear un Honda (debe salir con ID 2)

- **Método:** POST
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body:**

```json
{
  "marca": "Honda",
  "modelo": "Civic",
  "anio": 2020,
  "color": "Gris"
}
```

**Esperado:** `201 Created` y `"id": 2`.

### 1.2 Crear un Ford (debe salir con ID 3)

- **Método:** POST
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body:**

```json
{
  "marca": "Ford",
  "modelo": "Mustang",
  "anio": 2024,
  "color": "Negro"
}
```

**Esperado:** `201 Created` y `"id": 3`.

---

## Experimento 2: mostrar todos los vehículos

- **Método:** GET
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body:** sin cuerpo.

**Esperado:** `200 OK` con un arreglo de 3 vehículos (IDs 1, 2 y 3).

> El orden es del más reciente al más antiguo, porque el modelo usa `ordering = ["-created_at"]`.

---

## Experimento 3: consultar un solo vehículo por ID

- **Método:** GET
- **URL:** `http://127.0.0.1:8000/api/vehiculos/2/`
- **Body:** sin cuerpo.

**Esperado:** `200 OK` con el Honda y todos sus campos.
Si consultas un ID que no existe, por ejemplo `/api/vehiculos/999/`, recibirás `404 Not Found`.

---

## Experimento 4: actualizar el vehículo con PUT

- **Método:** PUT
- **URL:** `http://127.0.0.1:8000/api/vehiculos/2/`
- **Body:**

```json
{
  "marca": "Honda",
  "modelo": "Civic Touring",
  "anio": 2021,
  "color": "Blanco"
}
```

**Esperado:** `200 OK`.

Observa que:

- `modelo`, `anio` y `color` cambian.
- `created_at` conserva la fecha original.
- `updated_at` cambia a la fecha de la actualización.

> `PUT` reemplaza el registro completo, por eso debes enviar también la marca y todos los
> campos obligatorios. Si quieres cambiar solo un campo, se puede usar `PATCH`:
>
> ```json
> { "color": "Plateado" }
> ```

---

## Experimento 5: provocar un error de validación (400)

- **Método:** POST
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body:**

```json
{
  "marca": "",
  "modelo": "Prueba",
  "anio": "abc"
}
```

**Esperado:** `400 Bad Request`, con un JSON de errores por campo:

```json
{
  "marca": ["Este campo no puede estar en blanco."],
  "anio": ["Introduzca un número entero válido."],
  "color": ["Este campo es requerido."]
}
```

Esto demuestra que el serializer valida los datos antes de guardarlos. El vehículo
**no** se crea.

---

## Experimento 6: eliminar un vehículo

- **Método:** DELETE
- **URL:** `http://127.0.0.1:8000/api/vehiculos/3/`
- **Body:** sin cuerpo.

**Esperado:** `204 No Content`, sin respuesta en el cuerpo.

Luego puedes comprobarlo:

1. `GET /api/vehiculos/` → ya no aparece el Ford.
2. `GET /api/vehiculos/3/` → devuelve `404 Not Found`.

---

## Experimento 7: consultar un ID inexistente

- **Método:** GET
- **URL:** `http://127.0.0.1:8000/api/vehiculos/999/`
- **Body:** sin cuerpo.

**Esperado:** `404 Not Found` con:

```json
{
  "detail": "No encontrado."
}
```

---

## Resumen de lo que debes observar

- `POST` guarda un registro nuevo y devuelve **201**.
- `GET` nunca modifica datos: solo consulta y devuelve **200**.
- `PUT` actualiza un registro existente y devuelve **200**.
- `DELETE` borra el registro y devuelve **204** sin contenido.
- Los datos inválidos producen **400** con mensajes claros.
- Un ID inexistente produce **404**.
- Los campos `id`, `created_at` y `updated_at` los genera Django automáticamente;
  no se deben enviar en el cuerpo.

## Para dejar la base limpia antes de la entrega

Si quieres que la primera prueba del entregable vuelva a crear el **ID 1**, ejecuta en
una terminal del proyecto:

```powershell
& 'C:\xampp\mysql\bin\mysql.exe' -h 127.0.0.1 -P 3306 -u root -D serie4_vehiculos_db -e "TRUNCATE TABLE vehiculos;"
```

Eso borra todos los registros de práctica y reinicia el contador de IDs en 1.
