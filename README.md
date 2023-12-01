# Artist API

## Introduction

Welcome to the Artist API built with Django REST Framework. This API allows users to perform CRUD operations on artists and their works. Token-based authentication is implemented, ensuring that only authenticated users can access and manipulate the data.

    Note : Debug mode is True and Admin Page is exposed for testing purposes

## Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.10
- Django
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lohitsai/ArtistAPI
   ```

2. Navigate to the project directory:

   ```bash
   cd ArtistAPI
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run Server:
   ```bash
   python manage.py runserver
   ```

## Token-Based Authentication

To access CRUD operations, users need to be authenticated. Follow these steps:

1. Register an account by making a POST request to `http://127.0.0.1:8000/api/register/`. Provide the Username, Password and Display Name in the following format in the request Body. you will receive an authentication token.
   ```json
   {
     "username": "user1",
     "password": "password1",
     "displayName": "user1name"
   }
   ```
   Response:
   ```json
   {
     "token": "aabc90a939931ffbc51335c56c61c6c4c29d7af1"
   }
   ```
2. Login by making a POST request to `http://127.0.0.1:8000/api/login/`. Provide your username and password in the following format in the request Body. You will receive an authentication token.
   ```json
   {
     "username": "user1",
     "password": "password1"
   }
   ```
   Response:
   ```json
   {
     "token": "aabc90a939931ffbc51335c56c61c6c4c29d7af1"
   }
   ```
3. Include the obtained token in the header of your requests using the `Authorization` key for further API requests.
   ![image](https://i.imgur.com/BcPkvXu.png)

## API Endpoints

- **Retrieve a list of all Artists:**

  ```
  GET http://127.0.0.1:8000/api/artists/
  ```

  Response Example:

  ```json
  [
    {
      "name": "ArtistName1"
    },
    {
      "name": "ArtistName2"
    },
    {
      "name": "ArtistName3"
    },
    {
      "name": "ArtistName4"
    }
  ]
  ```

- **Retrieve a list of all works:**

  ```
  GET http://127.0.0.1:8000/api/works/
  ```

  Response Example:

  ```json
  [
    {
      "link": "https://www.youtube.com/",
      "workType": "Youtube"
    },
    {
      "link": "https://www.youtube.com/1",
      "workType": "Instagram"
    },
    {
      "link": "https://www.youtube.com/2",
      "workType": "Youtube"
    }
  ]
  ```

- **Create a new work:**

  ```
  POST http://127.0.0.1:8000/api/works/create/
  ```

  Provide the necessary information in the request body.
  Request Body Example:

  ```json
  {
    "link": "https://www.imgur.com/7",
    "workType": "Other"
  }
  ```

- **Filter works by Work Type:**
  _YT stands for YouTube, IG stands for Instagram, OT stands for Other._

  ```
  GET http://127.0.0.1:8000/api/works?work_type=YT
  ```

  or

  ```
  GET http://127.0.0.1:8000/api/works?work_type=IG
  ```

- **Search works by Artist name:**

  ```
  GET http://127.0.0.1:8000/api/works?artist=[Artist Name]/
  ```

- **Search works by Artist name and Work Type:**
  ```
  GET http://127.0.0.1:8000/api/works/?artist=[Artist Name]&work_type=[YT/IG/OT]
  ```

## Admin Panel

Access the admin panel to manage artists and works using the following URL:

- Admin URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Username: admin
- Password: password
