#!/usr/bin/python3

"""
Fifithatlady Nanny Jobs REST API Documentation

Introduction:
Fifithatlady Nanny Jobs is a platform for finding nanny job opportunities. This API documentation outlines the available endpoints for interacting with the Fifithatlady Nanny Jobs backend.

Authentication:
Authentication is required for certain endpoints. Authentication is handled using JSON Web Tokens (JWT). Users can obtain a JWT token by authenticating via the /signin endpoint with valid credentials. The token should be included in the Authorization header of subsequent requests.

Endpoints:

Users:

Create User:
- Endpoint: /api/users
- Method: POST
- Description: Create a new user account.
- Request Body:
  {
    "username": "example_user",
    "email": "example@example.com",
    "password": "password"
  }
- Response:
  - Success: Status code 201 (Created) and the created user object in JSON format.
  - Error: Status code 400 (Bad Request) if invalid data is provided.

Get User by ID:
- Endpoint: /api/users/{user_id}
- Method: GET
- Description: Retrieve user details by user ID.
- Request Parameters:
  - user_id: ID of the user to retrieve.
- Response:
  - Success: Status code 200 (OK) and the user object in JSON format.
  - Error: Status code 404 (Not Found) if the user ID does not exist.

Nanny Jobs:

Get All Nanny Jobs:
- Endpoint: /api/nanny_jobs
- Method: GET
- Description: Retrieve a list of all nanny job opportunities.
- Response:
  - Success: Status code 200 (OK) and a list of nanny job objects in JSON format.

Create Nanny Job:
- Endpoint: /api/nanny_jobs
- Method: POST
- Description: Create a new nanny job listing.
- Request Body:
  {
    "title": "Example Nanny Job",
    "description": "This is an example nanny job listing.",
    "salary": 3000,
    "requirements": "Experience with infants required.",
    "location": "New York",
    "user_id": "user_id_here"
  }
- Response:
  - Success: Status code 201 (Created) and the created nanny job object in JSON format.
  - Error: Status code 400 (Bad Request) if invalid data is provided.
"""

import argparse
import json
from models import db_session
from models.fifithatlady_nanny_job import FifithatladyNannyJob

def import_data(file_path):
    """Import data from a JSON file into the database."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                # Validate data before processing
                if not all(key in item for key in ['title', 'description', 'salary', 'requirements', 'location', 'user_id']):
                    print("Error: Invalid data format. Missing required fields.")
                    return
                
                nanny_job_data = {
                    'title': item['title'],
                    'description': item['description'],
                    'salary': item['salary'],
                    'requirements': item['requirements'],
                    'location': item['location'],
                    'user_id': item['user_id']
                }
                nanny_job_obj = FifithatladyNannyJob(**nanny_job_data)
                db_session.add(nanny_job_obj)

        db_session.commit()
        print("Data imported successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Import data into the Fifithatlady Nanny Jobs database")
    parser.add_argument("file_path", help="Path to the JSON file containing data")
    args = parser.parse_args()

    import_data(args.file_path)

if __name__ == "__main__":
    main()

