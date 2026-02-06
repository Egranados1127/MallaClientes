// src/services/api.js
export async function fetchClientes() {
  const res = await fetch('http://localhost:8000/clientes');
  if (!res.ok) throw new Error('Error al obtener clientes');
  const data = await res.json();
  return data.clientes;
}
