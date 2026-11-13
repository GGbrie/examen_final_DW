```jsx
import { useEffect, useState } from "react";
function ListaVehiculos() {
  const [vehiculos, setVehiculos] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/vehiculos/")
      .then((res) => res.json())
      .then((datos) => setVehiculos(datos));
  }, []);
  return <ul>{vehiculos.map((v) => (
    <li key={v.id}>{v.marca} {v.modelo} ({v.anio}) - {v.color}</li>
  ))}</ul>;
}
export default ListaVehiculos;
```
