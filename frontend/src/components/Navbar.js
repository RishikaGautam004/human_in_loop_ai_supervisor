import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="p-4 bg-gray-800 text-white">
            <ul className="flex gap-4">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/requests">Requests</Link></li>
                <li><Link to="/knowledge">Knowledge Base</Link></li>
            </ul>
        </nav>
    );
};

export default Navbar;