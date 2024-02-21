# QuickSearch Estates REST API Documentation

## Introduction
QuickSearch Estates is a platform for buying and selling properties. This API documentation outlines the available endpoints for interacting with the QuickSearch Estates backend.

## Authentication
Authentication is required for certain endpoints. Authentication is handled using JSON Web Tokens (JWT). Users can obtain a JWT token by authenticating via the `/signin` endpoint with valid credentials. The token should be included in the `Authorization` header of subsequent requests.

## Endpoints

### Users

#### Create User
- Endpoint: `/api/users`
- Method: POST
- Description: Create a new user account.
- Request Body:
  ```json
  {
    "username": "example_user",
    "email": "example@example.com",
    "password": "password"
  }
- Response:
  - Success: Status code 201 (Created) and the created user object in JSON format.
  - Error: Status code 400 (Bad Request) if invalid data is provided.

#### Get User by ID
- Endpoint: `/api/users/{user_id}`
- Method: GET
- Description: Retrieve user details by user ID.
- Request Parameters:
  - `user_id`: ID of the user to retrieve.
- Response:
  - Success: Status code 200 (OK) and the user object in JSON format.
  - Error: Status code 404 (Not Found) if the user ID does not exist.

### Properties

#### Get All Properties
- Endpoint: `/api/properties`
- Method: GET
- Description: Retrieve a list of all properties.
- Response:
  - Success: Status code 200 (OK) and a list of property objects in JSON format.

#### Create Property
- Endpoint: `/api/properties`
- Method: POST
- Description: Create a new property listing.
- Request Body:
  ```json
  {
    "title": "Example Property",
    "description": "This is an example property listing.",
    "price": 100000,
    "bedrooms": 3,
    "bathrooms": 2,
    "area": 1500,
    "address": "123 Main St",
    "city_id": "city_id_here"
  }
- Response:
  - Success: Status code 201 (Created) and the created property object in JSON format.
  - Error: Status code 400 (Bad Request) if invalid data is provided.

