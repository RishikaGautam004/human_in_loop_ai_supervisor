#!/bin/bash

echo "Starting Backend..."
cd backend && python app.py &

echo "Starting Frontend..."
cd frontend && npm start