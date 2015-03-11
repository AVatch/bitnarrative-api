# bitnarrative-api

### Table of Contents

### First Time Setup

```bash
>> virtualenv env
>> source env/bin/activate
>> pip install -r requirements.txt
>> cd bit-narrative-api
>> python manage.py migrate
>> python manage.py createsuperuser
>> python manage.py runserver
```

### Authentication Flow
Currently authentication is token based. That means that upon successful authentication, a response will be returned containing 
a token.


#####Request: POST
```http
/api/v1/api-token-auth/
```
```json
{
  "username":"",
  "password":""
}
```

#####Response
```json
{
  "token":""
}
```

All subsequent requests need to contain the following header:

```
Authorization: Token <token>
```

### Endpoints
```http
/api/v1/accounts/
/api/v1/accounts/create/
/api/v1/account/<pk>/
/api/v1/account/<pk>/bits/
/api/v1/me/

/api/v1/content/
/api/v1/content/<pk>)/
/api/v1/content/<pk>/bits/
/api/v1/content/<pk>/topbits/

/api/v1/bits/
/api/v1/bit/<pk>/
/api/v1/bit/<pk>/accounts/
```

#### Accounts
#####Request: GET @auth-required
```http
/api/v1/accounts/
```
#####Response
Paginated result of all accounts. ```next``` and ```previous``` contain ```urls``` to the 
following pages.
```json
{
    "count": 4, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "username": "avatchinsky", 
            "email": "", 
            "first_name": "", 
            "last_name": "", 
            "profile_picture_url": null, 
            "is_manager": false, 
            "created_at": "2015-02-25T17:57:07.446229Z", 
            "updated_at": "2015-02-25T17:57:07.450180Z"
        } 
    ]
}
```

#####Request: POST
```http
/api/v1/accounts/create/
```
Required fields: ```username```, ```password```, ```confirm_password```
```json
{
  "username": "",
  "email": "",
  "first_name": "",
  "last_name": "",
  "profile_picture_url": "",
  "is_manager": "",
  "password": "",
  "confirm_password": ""
}
```

#####Request: GET, POST, PUT, DELETE @auth-required
```http
/api/v1/account/<pk>/
```
Returns an account object
```json
{
  "id": 1, 
  "username": "avatchinsky", 
  "email": "", 
  "first_name": "", 
  "last_name": "", 
  "profile_picture_url": null, 
  "is_manager": false, 
  "created_at": "2015-02-25T17:57:07.446229Z", 
  "updated_at": "2015-02-25T17:57:07.450180Z"
}
```


#####Request: GET @auth-required
```http
/api/v1/account/<pk>/bits/
```
Returns a paginated list of bits the authenticated user has interacted with, sorted by most recent
```json
{
    "count": 12, 
    "next": "http://127.0.0.1:8000/api/v1/account/1/bits/?page=2", 
    "previous": null, 
    "results": [
        {
            "id": 13, 
            "bit": "more", 
            "content_index": 19, 
            "accounts": [
                "http://127.0.0.1:8000/api/v1/account/1/"
            ], 
            "content": "http://127.0.0.1:8000/api/v1/content/1/", 
            "view_count": 1, 
            "share_count": 0, 
            "up_count": 0, 
            "down_count": 0, 
            "created_at": "2015-02-25T18:29:46.260509Z"
        }
    ]
}
```

#####Request: GET @auth-required
```http
/api/v1/me/
```
Returns the currently authenticated user account's object

#### Content

#### Bits
