# backend-modify

### Technologies Used
* [NodeJS](https://nodejs.org/) This is a cross-platform runtime environment built on Chrome's V8 JavaScript engine used in running JavaScript codes on the server. It allows for installation and managing of dependencies and communication with databases.
* [ExpressJS](https://www.expresjs.org/) This is a NodeJS web application framework.

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/user/signup | To sign up a new user account |
| POST | /api/user/login | To login an existing user account |
| POST | /api/causes | To create a new cause |
| GET | /api/causes | To retrieve all causes on the platform |
| GET | /api/causes/:causeId | To retrieve details of a single cause |
| PATCH | /api/causes/:causeId | To edit the details of a single cause |
| DELETE | /api/causes/:causeId | To delete a single cause |

## Token Payload

1. POST /api/v1/auth/register

```json
{
    "username": "agung",
    "email": "agung5@gmail.com",
    "password": "Ayam123!"
}
```
Error Response
```json
{
    "success": false,
    "message": "Username or email already registered"
}
```

Success Response
```json
{
    "success": true,
    "message": "success registered"
}
```

2. POST /api/v1/auth/login

```json
{
    "email": "agung@gmail.com",
    "password": "Ayam1234!"
}

```
Error Response
```json
{
    "status": false,
    "error": "No User found"
}
```

Success Response
```json
{
    "status": true,
    "message": "login successfully",
    "accessToken": "<your_access_token>",
    "refreshToken": "<your_refresh_token>",
    "expRefreshToken": "2024-12-20T02:33:44.467Z"
}
```

Bearer token is expired response example
```json
{
    "message": "Invalid or expired token"
}
```

3. POST /api/v1/journals

```json
Authorization: <your_bearer_token>
{
    "journalContent": "<your_content>"
}
```

Error 409 Response
```json
{
    "status": false,
    "message": "Journal already created today"
}
```

Error 422 Response
```json
{
    "status": true,
    "message": "validation error when create new journal",
    "errors": [
        "String must contain at least 200 character(s)"
    ]
}
```

Success Response
```json
{
    "status": true,
    "message": "Successfully created journal"
}
```


4. GET /api/v1/profiles/me

```json
Authorization: <your_bearer_token>
```

Success Response
```json
{
    "status": true,
    "result": {
        "email": "komangweda@gmail.com",
        "username": "KomangWeda",
        "name": "Mr. Wednesday ",
        "gender": "male",
        "country": "Not Representing",
        "urlphoto": "https://storage.googleapis.com/bucket-profile-moodify/profileImage_komangweda@gmail.com_03122024_055647.jpeg"
    }
}
```

5. PUT /api/v1/profiles/me

```json
Authorization: <your_bearer_token>
{
    "name": "bagus candra",
    "gender": "male",
    "country": "USA"
}
```

Error 400 Response
```json
{
    "status": false,
    "error_msg": {
        "name": [
            "String must contain at least 4 character(s)"
        ]
    }
}
```

Success Response
```json
{
    "status": true,
    "message": "Success update your profile"
}
```

6. PATCH /api/v1/profiles/photo

```form-data
Authorization: <your_bearer_token>
{
    "name": "bagus candra",
    "gender": "male",
    "country": "USA"
}
```

Error Response Image Size Above 2 MB
```json
{
    "status": false,
    "message": "internal server error, Max size of image file must be below 2 MB"
}
```

Error Response With Input No Value or Text Value
```json
{
    "status": false,
    "message": "Please provide your photo profile"
}
```

Error Response With Wrong Format Image Input
```json
{
    "status": false,
    "message": "internal server error, Only PNG, JPEG, JPG, and WEBP are allowed"
}
```

Success Response
```json
{
    "status": true,
    "message": "success upload image",
    "imageUrl": "https://storage.googleapis.com/bucket-profile-moodify/profileImage_agung52@gmail.com_13122024_025756.png"
}
```

7. GET /api/v1/articles/bookmarks/me

8. GET /api/v1/journals?date=2024-12-10




## Dokumentasi Postman

![Articles](dokumentation%20postman/detail%20articles.png)
![Detail Articles](dokumentation%20postman/detail%20articles.png)
![Edit Journal](dokumentation%20postman/edit%20journal.png)
![Edit Photo Profile](dokumentation%20postman/edit%20photo%20profile.png)
![Edit Profile](dokumentation%20postman/edit%20profile.png)
![Journal Create Success](dokumentation%20postman/journal%20create%20success.png)
![Journal Each Day](dokumentation%20postman/journal%20each%20day.png)
![Journal Validate Fail](dokumentation%20postman/journal%20validate%20fail.png)
![Login](dokumentation%20postman/login.png)
![Nations](dokumentation%20postman/nations.png)
![New Bookmark](dokumentation%20postman/new%20bookmark.png)
![Profile](dokumentation%20postman/profile.png)
![Refresh Token](dokumentation%20postman/refresh%20token.png)
![Register](dokumentation%20postman/register.png)
![Show Bookmark](dokumentation%20postman/show%20bookmark.png)
![Update Journal by Date](dokumentation%20postman/update%20journal%20by%20date.png)
![Weekly Mood](dokumentation%20postman/weekly%20mood.png)
