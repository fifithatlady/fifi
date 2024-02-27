#!/bin/bash

# Define absolute paths
ROOT_DIR="/home/ubuntu/Fifithatlady_Nanny_Jobs"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

# Install backend dependencies
echo "Step 1: Installing backend dependencies..."
cd "$BACKEND_DIR" || exit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the backend server
echo "Step 2: Starting the backend server..."
# Assuming you start the backend server with app.py
nohup python3 app.py &

# Start the Express.js server
echo "Step 3: Starting the Express.js server..."
cd "$ROOT_DIR" || exit
# Assuming you start the Express.js server with app.js
nohup node "$BACKEND_DIR/app.js" &

# Install frontend dependencies and build
echo "Step 4: Installing frontend dependencies and building..."
cd "$FRONTEND_DIR" || exit
npm install
npm run build

# Start the frontend server
echo "Step 5: Starting the frontend server..."
# Assuming you start the frontend server with npm start
nohup npm start &

# Restart nginx, fifithatlady-nanny-jobs, and gunicorn
echo "Step 6: Restarting nginx, fifithatlady-nanny-jobs, and gunicorn..."
sudo systemctl restart nginx
sudo systemctl restart fifithatlady-nanny-jobs
sudo systemctl restart gunicorn
sudo systemctl status nginx
sudo systemctl status fifithatlady-nanny-jobs

