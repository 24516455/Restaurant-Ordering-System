
// frontend/src/App.js

import React,  { useState } from 'react';
import { BrowserRouter as Router,  Route, Switch } from 'react-router-dom';
import Auth from './components/Auth';
import Orders from './components/Orders';

const App = () => {
const [token, setToken] = useState(null);

return (
<Router>
<div>
<Switch>
<Route path="/auth">
<Auth setToken={setToken} />
</Route>
<Route path="/orders">
<Orders token={token} />
</Route>
<Route path="/">
<h1>Welcome to the Order Management System</h1>
Login/Register</a>
</Route>
</Switch>
</div>
</Router>
);
};

export default App;
