// frontend/src/components/Auth.js

import React,  { useState } from 'react';
import axios from 'axios';

const Auth = ({ setToken }) => {
const [username, setUsername] = useState('');
const [password, setPassword] = useState('');
const [isRegistering, setIsRegistering] = useState(true);

const handleSubmit = async (e) => {
e.preventDefault();
const endpoint = isRegistering ? '/api/register' : '/api/login';
try {
const response = await axios.post(endpoint, { username, password });
if (response.data.access_token) {
setToken(response.data.access_token);
Alert ('Successful login ');
}
} catch (error) {
Alert ('Error occurred:'+error. response. data. msg);
}
};

return (
<form onSubmit={handleSubmit}>
<h2>{isRegistering? 'Register': 'Login'}</h2>
<input
type="text"
Placeholder="username"
value={username}
onChange={(e) => setUsername(e.target.value)}
required
/>
<input
type="password"
Placeholder="password"
value={password}
onChange={(e) => setPassword(e.target.value)}
required
/>
<button type="submit">{isRegistering? 'Register:' Login '}</button>
<p onClick={() => setIsRegistering(!isRegistering)}>
{isRegistering? 'Already have an account? Login': 'Don't have an account? Register'}
</p>
</form>
);
};

export default Auth;
