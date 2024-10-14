// frontend/src/components/Orders.js

import React,  { useEffect,  useState } from 'react';
import axios from 'axios';

const Orders = ({ token }) => {
const [orders, setOrders] = useState([]);
const [itemName, setItemName] = useState('');
const [quantity, setQuantity] = useState('');

useEffect(() => {
if (token) {
fetchOrders();
}
}, [token]);

const fetchOrders = async () => {
try {
const response = await axios.get('/api/orders', {
headers: { Authorization: `Bearer ${token}` },
});
setOrders(response.data);
} catch (error) {
Alert ('Unable to retrieve order:'+error message);
}
};

const createOrder = async (e) => {
e.preventDefault();
try {
await axios.post('/api/orders', { item_name: itemName, quantity }, {
headers: { Authorization: `Bearer ${token}` },
});
fetchOrders();
setItemName('');
setQuantity('');
} catch (error) {
Alert ('Unable to create order:'+error message);
}
};

return (
<div>
<h2>Order Management</h2>
<form onSubmit={createOrder}>
<input
type="text"
Placeholder="Product Name"
value={itemName}
onChange={(e) => setItemName(e.target.value)}
required
/>
<input
type="number"
Placeholder="quantity"
value={quantity}
onChange={(e) => setQuantity(e.target.value)}
required
/>
<button type="submit">Create order</button>
</form>
<h3>My order</h3>
<ul>
{orders.map(order => (
<li key={order. id}>{order. tem_name} - Quantity: {order. quantity}</li>
))}
</ul>
</div>
);
};

export default Orders;
