# 📘 Assignment: JSON Data Manager

## 🎯 Objective

Learn how to manage data stored in JSON files using Python. Practice reading, writing, and updating JSON content with functions that make file-based data persistent.

## 📝 Tasks

### 🛠️ Load JSON data from a file

#### Description
Write a function that loads user records from a JSON file and returns them as Python objects.

#### Requirements
Completed program should:

- Read data from a JSON file named `users.json`.
- Parse the JSON into Python data structures.
- Return a list of users, where each user is represented by a dictionary.

### 🛠️ Add a new user record

#### Description
Write a function that adds a new user to the loaded data and saves the updated list back to the JSON file.

#### Requirements
Completed program should:

- Accept a `name` and `email` for a new user.
- Add the new user to the list with a unique numeric `id`.
- Save the updated user list back to `users.json`.

### 🛠️ Update an existing user

#### Description
Write a function that updates a user's email address based on the user's ID and saves the changed data.

#### Requirements
Completed program should:

- Find a user by `id` in the loaded data.
- Update the user's `email` field.
- Save the updated list back to `users.json`.
- Handle the case when the requested user is not found.

### 🌟 Stretch Goal

#### Description
Add search support to filter users by email domain.

#### Requirements
Completed program should:

- Allow filtering users whose email ends with a given domain.
- Return only matching user records.
