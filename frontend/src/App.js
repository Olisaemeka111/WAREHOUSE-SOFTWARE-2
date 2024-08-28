import React from 'react';
import ItemList from './components/ItemList';
import OrderForm from './components/OrderForm';

function App() {
  return (
    <div className="App">
      <h1>Warehouse Management System</h1>
      <ItemList />
      <OrderForm />
    </div>
  );
}

export default App;
