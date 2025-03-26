# API Documentation

## Authentication

### Signup
**Endpoint:** `/api/signup`

**Method:** `POST`

**Request Body:**
```json
{
    "username": "testuser",
    "email": "test@test.com",
    "first_name": "test",
    "last_name": "tetes",
    "password": "Apple14-"
}
```

### Login
**Endpoint:** `/api/login`

**Method:** `POST`

**Request Body:**
```json
{
    "email": "test@test.com",
    "password": "Apple14-"
}
```

### Refresh Token
**Endpoint:** `/api/refresh`

**Method:** `POST`

### Signout
**Endpoint:** `/api/signout`

**Method:** `POST`

**Request Body:**
```json
{}
```

---

## Work Management

### Create Work
**Endpoint:** `/api/work/create`

**Method:** `POST`

**Request Body:**
```json
{
    "company": "id form",
    "about": "255 max length",
    "work_hour": "integer",
    "date": "YYYY-MM-DD"
}
```

### Delete Work
**Endpoint:** `/api/work/delete`

**Method:** `POST`

**Request Body:**
```json
{
    "id": 5
}
```

### Delete Work as Manager
**Endpoint:** `/api/work/forcedelete`

**Method:** `POST`

**Note:** Requires Manager Role

**Request Body:**
```json
{
    "id": 5
}
```

### Get Work
**Endpoint:** `/api/work/get`

**Method:** `GET`

### Get All Works
**Endpoint:** `/api/work/getall`

**Method:** `POST`

**Note:** Requires Manager Role

**Request Body (All parameters are optional):**
```json
{
    "user": "",
    "company": "",
    "date": ""
}
```

---

## User Management

### Get All Users
**Endpoint:** `/api/users/getall`

**Method:** `GET`

**Note:** Requires Manager Role

---

## Admin Credentials
**Admin Email:** `o***i@i**d.com`

**Admin Password:** `A***4-`

