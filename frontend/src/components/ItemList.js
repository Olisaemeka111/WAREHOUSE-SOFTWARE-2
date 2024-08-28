import React, { useState, useEffect } from 'react';
import axios from '../services/api';

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('/items')
      .then(response => setItems(response.data))
      .catch(error => console.error('Error fetching items:', error));
  }, []);

  return (
    <div>
      <h2>Items</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ItemList;
