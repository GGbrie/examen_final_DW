# ENTREGABLE – API REST de Vehículos

API construida con **Django + Django REST Framework + MySQL/MariaDB**, sin inicio de sesión
ni autenticación. Todas las respuestas son en formato **JSON**.

## Datos generales para Thunder Client / Postman

| Dato | Valor |
|---|---|
| URL base | `http://127.0.0.1:8000/api/vehiculos/` |
| Método de envío | `Body` → `JSON` (o `raw` → `JSON`) |
| Cabecera obligatoria al enviar datos | `Content-Type: application/json` |
| Autenticación | Ninguna (no usar token, usuario ni contraseña) |

> **Importante:** ejecuta las pruebas en el orden mostrado. La prueba 1 crea el registro
> con **ID 1**, las pruebas 3, 4 y 6 usan ese ID, y la prueba 6 lo elimina al final.
>
> Si ya existen vehículos en la base de datos, el POST creará un ID nuevo (2, 3, ...).
> En ese caso, usa el ID que devuelva la respuesta en las rutas `/api/vehiculos/<id>/`.

---

## a) Pruebas obligatorias en Thunder Client / Postman

### Prueba 1 – POST: crear un registro válido

- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body (JSON):**

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "anio": 2022,
  "color": "Rojo"
}
```

**Resultado esperado:** código **201 Created** y el registro creado con `"id": 1`.

---

### Prueba 2 – GET: listar registros

- **Método:** `GET`
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body:** no lleva cuerpo.

**Resultado esperado:** código **200 OK** y un arreglo JSON con todos los vehículos.

---

### Prueba 3 – GET: consultar por ID

- **Método:** `GET`
- **URL:** `http://127.0.0.1:8000/api/vehiculos/1/`
- **Body:** no lleva cuerpo.

**Resultado esperado:** código **200 OK** y el vehículo con ID 1.

---

### Prueba 4 – PUT: actualizar el registro

- **Método:** `PUT`
- **URL:** `http://127.0.0.1:8000/api/vehiculos/1/`
- **Body (JSON):**

```json
{
  "marca": "Toyota",
  "modelo": "Corolla Cross",
  "anio": 2023,
  "color": "Azul"
}
```

**Resultado esperado:** código **200 OK** con los datos actualizados.
En `PUT` se deben enviar todos los campos obligatorios, porque reemplaza el registro completo.

---

### Prueba 5 – POST: datos inválidos/incompletos (error 400)

- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/api/vehiculos/`
- **Body (JSON):**

```json
{
  "marca": "",
  "modelo": "Corolla",
  "anio": "dos mil"
}
```

Faltan el `color`, la `marca` está vacía y el `anio` no es un número entero.

**Resultado esperado:** código **400 Bad Request** con errores claros por campo, por ejemplo:

```json
{
  "marca": ["Este campo no puede estar en blanco."],
  "anio": ["Introduzca un número entero válido."],
  "color": ["Este campo es requerido."]
}
```

---

### Prueba 6 – DELETE: eliminar el registro

- **Método:** `DELETE`
- **URL:** `http://127.0.0.1:8000/api/vehiculos/1/`
- **Body:** no lleva cuerpo.

**Resultado esperado:** código **204 No Content** (respuesta sin contenido).

---

## b) Consumo con React

React consume la API mediante `fetch`, guarda la respuesta en un estado y dibuja la lista
en pantalla. Las cuatro piezas clave son `useState`, `useEffect`, `fetch` y `map` con `key`.

**`useState`** crea una variable de estado y una función para cambiarla. En el ejemplo,
`vehiculos` empieza como un arreglo vacío `[]` porque todavía no se han pedido los datos,
y `setVehiculos` es la función que los actualiza. Cuando se llama a `setVehiculos`, React
vuelve a renderizar el componente automáticamente para mostrar la información nueva.

**`useEffect`** sirve para ejecutar código después de que el componente aparece en pantalla.
Se usa para pedir los datos al servidor. El arreglo vacío `[]` al final (las dependencias)
indica que el efecto se ejecute **una sola vez**, al montar el componente; si no se pusiera,
se ejecutaría después de cada renderizado y podría provocar peticiones repetidas.

**`fetch`** hace la petición HTTP a la URL de Django. Devuelve una *promesa*; el primer
`.then((res) => res.json())` convierte la respuesta en objetos de JavaScript y el segundo
`.then((datos) => setVehiculos(datos))` guarda ese arreglo en el estado. La URL usada es
`http://127.0.0.1:8000/api/vehiculos/`, y funciona desde React gracias a que Django tiene
CORS habilitado (`CORS_ALLOW_ALL_ORIGINS = True`). Recuerda tener los dos servidores activos:
Django en el puerto 8000 y React en su propio puerto (por ejemplo, 5173).

**`map` con `key`** recorre el arreglo `vehiculos` y transforma cada vehículo en un elemento
`<li>`. La propiedad `key={v.id}` es obligatoria en las listas de React: le da a cada elemento
una identidad única y estable para que React pueda actualizar la lista de forma eficiente.
Se debe usar el `id` de la base de datos, no el índice del arreglo. Sin `key`, React muestra
una advertencia y puede renderizar mal los cambios.

```jsx
import { useEffect, useState } from "react";

function Vehiculos() {
  const [vehiculos, setVehiculos] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/vehiculos/")
      .then((res) => res.json())
      .then((datos) => setVehiculos(datos));
  }, []);
  return <ul>{vehiculos.map((v) => <li key={v.id}>{v.marca} {v.modelo}</li>)}</ul>;
}
export default Vehiculos;
```

> El bloque anterior tiene **12 líneas de código** (el máximo permitido era 15).

---

## Cómo volver a ejecutar el proyecto

1. Inicia MySQL desde el panel de XAMPP (botón **Start** de MySQL).
2. Abre una terminal en la carpeta del proyecto.
3. Levanta Django:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

4. Abre Thunder Client/Postman y ejecuta las pruebas de esta guía.
