import React, { useState, useEffect } from 'react';

const LearnedAnswers = () => {
    const [answers, setAnswers] = useState([]);

    useEffect(() => {
        fetch('/knowledge_base')
            .then(res => res.json())
            .then(data => setAnswers(data.learned_answers));
    }, []);

    return (
        <div className="mt-4">
            <h2 className="text-xl font-semibold">Learned Answers</h2>
            <ul>
                {answers.map((entry, idx) => (
                    <li key={idx} className="p-2 border-b">{entry.question}: {entry.answer}</li>
                ))}
            </ul>
        </div>
    );
};

export default LearnedAnswers;