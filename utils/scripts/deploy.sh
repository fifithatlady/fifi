#!/bin/bash

# Example deployment script for fifithalady_nanny_jobs on Heroku with MySQL

# Step 1: Login to Heroku (if not already logged in)
echo "Step 1: Logging in to Heroku..."
heroku login -i

# Step 2: Create a new Heroku app
echo "Step 2: Creating a new Heroku app..."
heroku create fifithalady_nanny_jobs

# Step 3: Add ClearDB MySQL add-on
echo "Step 3: Adding ClearDB MySQL add-on..."
heroku addons:create cleardb:ignite

# Step 4: Set up environment variables for MySQL database URL
echo "Step 4: Setting up environment variables for MySQL database URL..."
heroku config:set DATABASE_URL=$(heroku config:get CLEARDB_DATABASE_URL)

# Step 5: Push your code to Heroku
echo "Step 5: Pushing code to Heroku..."
git push heroku main

# Step 6: Run database migrations (if applicable)
echo "Step 6: Running database migrations..."
heroku run python manage.py db upgrade

# Step 7: Open the deployed application in the browser
echo "Step 7: Opening the deployed application in the browser..."
heroku open

echo "Deployment completed successfully."

