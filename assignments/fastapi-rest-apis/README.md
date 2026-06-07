# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using FastAPI to manage a simple user directory. Practice defining routes, working with Pydantic models, and handling JSON request and response data.

## 📝 Tasks

### 🛠️ Create a user list endpoint

#### Description
Implement a `GET /users` endpoint that returns a list of users in JSON format.

#### Requirements
Completed program should:

- Define a Pydantic model for user data.
- Return a list of users from `GET /users`.
- Include at least three sample users in the response.

### 🛠️ Add a user creation endpoint

#### Description
Implement a `POST /users` endpoint that accepts JSON data to create a new user and returns the created user.

#### Requirements
Completed program should:

- Accept JSON request data for `name` and `email`.
- Validate the incoming data using a Pydantic model.
- Assign a new numeric `id` and return the created user object.

### 🛠️ Build a user detail endpoint with error handling

#### Description
Implement a `GET /users/{user_id}` endpoint that returns a single user or a 404 error if the user does not exist.

#### Requirements
Completed program should:

- Read `user_id` from the route path.
- Return the matching user when found.
- Return an HTTP 404 error when the user is not found.

### 🌟 Stretch Goal

#### Description
Add query parameter support for filtering users by email domain.

#### Requirements
Completed program should:

- Allow `GET /users?domain=example.com`.
- Return only users whose email ends with the provided domain.
