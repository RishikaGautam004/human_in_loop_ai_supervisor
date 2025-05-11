import React from 'react';
import RequestList from '../components/RequestList';
import LearnedAnswers from '../components/LearnedAnswers';

const Home = () => {
    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">Supervisor Dashboard</h1>
            <RequestList />
            <LearnedAnswers />
        </div>
    );
};

export default Home;