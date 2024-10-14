// frontend/src/api.js

import axios from 'axios';

const API_URL = ' http://localhost:5000/api ';  //  Based on the address and port configuration of the backend server

export const registerUser = async (username, password) => {
return await axios.post(`${API_URL}/register`, { username, password });
};

export const loginUser = async (username, password) => {
return await axios.post(`${API_URL}/login`, { username, password });
};

export const fetchOrders = async (token) => {
return await axios.get(`${API_URL}/orders`, {
headers: { Authorization: `Bearer ${token}` }
});
};

export const createOrder = async (order, token) => {
return await axios.post(`${API_URL}/orders`, order, {
headers: { Authorization: `Bearer ${token}` }
});
};
