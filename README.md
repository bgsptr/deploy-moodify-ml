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

Authorization: <your_bearer_token>

Success Response
```json
{
    "status": true,
    "message": "successfully fetch bookmark article for user with email: komangweda@gmail.com",
    "articles": [
        {
            "id": "03e37921-8d94-4e6c-a584-b33ec4879453",
            "source": "Forbes",
            "author": "Lance Eliot, Contributor, \n Lance Eliot, Contributor\n https://www.forbes.com/sites/lanceeliot/",
            "title": "Generative AI Is Helping To Clear Up Brain Fog",
            "description": "People talk about having brain fog. The meaning differs. One creative way to aid diagnosing and resolving brain fog is via generative AI. Here's the inside scoop.",
            "url": "https://www.forbes.com/sites/lanceeliot/2024/11/24/generative-ai-is-helping-to-clear-up-brain-fog/",
            "urlToImage": "https://imageio.forbes.com/specials-images/imageserve/6742bd86c3e3f33f6f0ec417/0x0.jpg?format=jpg&crop=2882,2160,x664,y0,safe&height=900&width=1600&fit=bounds",
            "publishedAt": "2024-11-24T05:52:47.000Z",
            "content": "Generative AI and large language models (LLMs) are now one of the modern solutions that are thought to help overcome brain fog, a condition that often makes a person find it difficult to think clearly and lose focus. This technology is able to convey information, provide structured reminders, and even assist in creative processes such as brainstorming ideas when the brain is not optimal. Additionally, AI-based tools can automate routine tasks, so users can focus more on work that requires strategic thinking. However, using AI to overcome brain fog also has risks, such as excessive reliance on technology that can reduce natural cognitive resilience, as well as privacy issues related to circulating data. With a balanced approach, a combination of AI assistance and lifestyle changes such as maintaining sleep patterns, nutrition, and mindfulness practices, can be a holistic way to manage brain fog effectively."
        }
    ]
}
```

8. GET /api/v1/journals?date=<query_params_date>

Authorization: <your_bearer_token>
query_params_date: 2024-12-10

Error Response Journal Not Found
```json
{
    "status": false,
    "message": "Journal created that day is not found"
}
```

Success Response
```json
{
    "status": true,
    "message": "Journal fetch successfully from database",
    "journal": {
        "emailAuthor": "komangweda@gmail.com",
        "journalId": "9f7fbc3e-be0c-4e0e-bec4-fc21012e88ee",
        "content": "Today felt like an emotional rollercoaster. I woke up feeling excited, looking forward to the plans I had made. The morning sunlight streaming through the window made everything feel possible. I brewed my favorite coffee, the aroma filling the room with warmth and comfort. For a moment, I felt truly happy.\n\nBut as the day progressed, things started to shift. An unexpected message from an old friend brought up memories I thought I had buried. It was bittersweet—part of me felt nostalgic, but another part was overwhelmed by regret and sadness. Why do good moments always seem to carry a shadow of the past?\n\nBy evening, frustration crept in. A task I had been working on all week hit another roadblock, and I could feel my patience slipping away. I wanted to scream but settled for a deep breath instead.\n\nAs I write this, I’m realizing how much I’ve felt in just one day. It’s exhausting but also oddly grounding. Maybe feeling all of this is just part of being alive.",
        "createdAt": "2024-12-11T07:57:25.393Z",
        "updatedAt": "2024-12-11T07:57:25.393Z",
        "isPredicted": true
    }
}
```



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
