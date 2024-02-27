#!/bin/bash

# Navigate to the project root directory
cd /fifi || exit

# Backend setup
echo "Setting up backend..."
cd backend || exit
# Perform any necessary backend setup tasks, such as installing Python dependencies
pip install -r requirements.txt

# Frontend compilation
echo "Compiling frontend..."
cd ../frontend || exit
# Install frontend dependencies and build the frontend assets
npm install
npm run build  # Adjust this command based on your specific frontend build process

# Move compiled assets to appropriate locations
# For example, if your backend serves the frontend assets from a "static" directory
mv dist/* ../backend/static/  # Adjust the paths as needed

echo "Compilation complete."
