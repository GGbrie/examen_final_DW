# Inciso B – Mostrar en React la lista de vehículos con GET

Esta explicación corresponde al consumo de la API desde React. La URL real que se utiliza es:

```text
http://127.0.0.1:8000/api/vehiculos/
```

El código completo y listo para copiar está en el archivo **`INCISO_B_CODIGO.md`**.

## 1. `useState`: guardar la lista en la memoria del componente

`useState` crea una variable especial llamada **estado**. En este caso se usa para guardar
el arreglo de vehículos que llega desde la API.

- `vehiculos` es la variable que contiene la lista. Al principio vale `[]`, es decir, una
  lista vacía, porque todavía no se han pedido los datos al servidor.
- `setVehiculos` es la función que permite cambiar ese valor.
- Cuando se llama a `setVehiculos` con los datos nuevos, React vuelve a dibujar el
  componente automáticamente para mostrar la información actualizada.

Sin `useState`, la lista podría descargarse, pero el componente no se actualizaría en
pantalla cuando llegaran los datos.

## 2. `useEffect`: pedir los datos en el momento correcto

`useEffect` ejecuta código después de que el componente aparece por primera vez en pantalla.
Se usa para hacer la petición a la API, porque no conviene pedir datos durante el dibujo
inicial del componente.

- El segundo argumento es un arreglo de dependencias.
- Al usar `[]` (arreglo vacío), el efecto se ejecuta **una sola vez**, cuando el componente
  se monta.
- Si se omitiera ese arreglo, el efecto se ejecutaría después de cada renderizado y podría
  provocar peticiones repetidas o un ciclo infinito.

En resumen: `useEffect` responde a la pregunta **“¿cuándo debo pedir los datos?”**.

## 3. `fetch`: hacer la petición HTTP a la API

`fetch` es la función de JavaScript que hace la petición al servidor. Si no se indica un
método, utiliza **GET** por defecto, que es justamente el método para consultar la lista.

El flujo es:

1. `fetch("http://127.0.0.1:8000/api/vehiculos/")` envía la petición GET.
2. `fetch` devuelve una **promesa**, porque la respuesta no llega de inmediato.
3. El primer `.then((res) => res.json())` convierte la respuesta HTTP en datos de JavaScript.
4. El segundo `.then((datos) => setVehiculos(datos))` guarda el arreglo recibido en el estado.

La API está configurada sin autenticación y con CORS habilitado, por lo que React puede
consumirla desde otro puerto, por ejemplo `http://localhost:5173`, sin enviar tokens.

## 4. `map` con `key`: dibujar cada vehículo en la lista

`map` recorre el arreglo `vehiculos` y transforma cada objeto en un elemento de React,
en este caso un `<li>`.

- Por cada vehículo se crea un elemento con su marca, modelo, año y color.
- `key={v.id}` asigna una identidad única a cada elemento.
- La `key` debe ser un valor estable y único; por eso se usa el `id` que genera la base de
  datos, y no el índice del arreglo.
- Gracias a la `key`, React puede saber qué elementos se agregaron, cambiaron o eliminaron
  y actualizar la lista de forma eficiente.
- Si no se coloca la `key`, React muestra una advertencia en la consola y puede renderizar
  mal los cambios.

## 5. Flujo completo, paso a paso

1. El componente inicia con `vehiculos = []`.
2. React dibuja el componente por primera vez.
3. `useEffect` se ejecuta una vez y llama a `fetch`.
4. `fetch` hace el `GET` a `/api/vehiculos/`.
5. Django responde con un arreglo JSON de vehículos.
6. `res.json()` convierte la respuesta en objetos de JavaScript.
7. `setVehiculos(datos)` actualiza el estado.
8. React vuelve a dibujar el componente.
9. `map` recorre la lista y crea un `<li>` por cada vehículo, usando `key={v.id}`.
10. El usuario ve la lista completa en pantalla.

## 6. Cómo comprobarlo

1. Inicia MySQL desde XAMPP.
2. Levanta Django con `.\.venv\Scripts\python.exe manage.py runserver`.
3. Inicia el proyecto de React.
4. Abre la página en el navegador y revisa la pestaña **Network** o **Red** para confirmar
   que la petición `GET /api/vehiculos/` devuelve **200 OK**.
5. Si la lista está vacía, crea vehículos primero con **POST** desde Thunder Client.
