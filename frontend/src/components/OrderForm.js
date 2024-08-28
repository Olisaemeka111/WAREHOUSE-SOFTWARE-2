import React, { useState } from 'react';
import axios from '../services/api';

function OrderForm() {
  const [orderNumber, setOrderNumber] = useState('');
  const [deliveryInfo, setDeliveryInfo] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/orders', {
      order_number: orderNumber,
      delivery_info: deliveryInfo,
    })
    .then(response => {
      console.log('Order created:', response.data);
    })
    .catch(error => console.error('Error creating order:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Order</h2>
      <label>
        Order Number:
        <input
          type="text"
          value={orderNumber}
          onChange={(e) => setOrderNumber(e.target.value)}
        />
      </label>
      <label>
        Delivery Info:
        <input
          type="text"
          value={deliveryInfo}
          onChange={(e) => setDeliveryInfo(e.target.value)}
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

export default OrderForm;
