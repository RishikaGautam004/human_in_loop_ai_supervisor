import React, { useState, useEffect } from 'react';

const RequestList = () => {
    const [requests, setRequests] = useState([]);

    useEffect(() => {
        fetch('/get_pending_requests')
            .then(res => res.json())
            .then(data => setRequests(data));
    }, []);

    return (
        <div className="mt-4">
            <h2 className="text-xl font-semibold">Pending Requests</h2>
            <ul>
                {requests.map((req, idx) => (
                    <li key={idx} className="p-2 border-b">{req.question}</li>
                ))}
            </ul>
        </div>
    );
};

export default RequestList;