import React, { useEffect, useState } from 'react';
import { fetchClientes } from './services/api';

function ClientesTable() {
  const [clientes, setClientes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchClientes()
      .then(setClientes)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Cargando clientes...</p>;
  if (error) return <p>Error al cargar clientes</p>;
  if (!clientes.length) return <p>No hay datos de clientes.</p>;

  const columns = Object.keys(clientes[0]);

  return (
    <div>
      <h2>Listado de Clientes (demo)</h2>
      <table border="1" cellPadding="4">
        <thead>
          <tr>
            {columns.map(col => <th key={col}>{col}</th>)}
          </tr>
        </thead>
        <tbody>
          {clientes.map((cli, i) => (
            <tr key={i}>
              {columns.map(col => <td key={col}>{cli[col]}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ClientesTable;
