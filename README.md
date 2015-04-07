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
/api/v1/

/api/v1/api-token-auth/

/api/v1/accounts/
/api/v1/accounts/create/
/api/v1/account/<pk>/
/api/v1/account/<pk>/bits/
/api/v1/account/<pk>/communities/
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
Required fields: ```username```, ```password```


#####Request: GET, PUT, DELETE @auth-required
```http
/api/v1/account/<pk>/
```
Returns (```GET```) an account object and allows update (```PUT```) and deletion (```DELETE```) of account object.
```json
{
    "id": 1, 
    "last_login": "2015-04-04T04:04:02.226792Z", 
    "username": "avatchinsky", 
    "email": "adrian@adrian.com", 
    "first_name": "Adrian", 
    "last_name": "Vatchinsky", 
    "profile_picture_url": "http://placehold.it/150x150", 
    "is_admin": true, 
    "is_manager": false, 
    "created_at": "2015-04-04T04:03:50.932471Z", 
    "updated_at": "2015-04-07T18:20:20.098732Z"
}
```


#####Request: GET @auth-required
```http
/api/v1/account/<pk>/bits/
```
Returns a paginated list of bits the authenticated user has interacted with, sorted by most recent
```json
{
    "count": 1, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "bit": "   When it comes to crowdfunding it is usually  the record breakers that make news ", 
            "content_index": 0, 
            "view_count": 1, 
            "share_count": 0, 
            "up_count": 1, 
            "down_count": 0, 
            "created_at": "2015-04-04T04:31:54.821662Z", 
            "updated_at": "2015-04-07T18:22:43.167897Z", 
            "content": 1, 
            "accounts": [
                1
            ], 
            "community": []
        }
    ]
}
```


#####Request: GET @auth-required
```http
/api/v1/account/<pk>/bits/
```
Returns a paginated list of bits the authenticated user has interacted with, sorted by most recent
```json
{
    "count": 1, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "community": "Yoloswag", 
            "community_description": "Where big pimps chill", 
            "lead_image_url": "", 
            "participation_rate": null, 
            "created_at": "2015-04-04T04:30:55.535874Z", 
            "updated_at": "2015-04-07T18:23:47.544967Z", 
            "accounts": [
                1
            ], 
            "topics": [
                1
            ]
        }
    ]
}
```

#####Request: GET @auth-required
```http
/api/v1/me/
```
Returns the currently authenticated user account's object

```json
{
    "id": 1, 
    "last_login": "2015-04-04T04:04:02.226792Z", 
    "username": "avatchinsky", 
    "email": "adrian@adrian.com", 
    "first_name": "Adrian", 
    "last_name": "Vatchinsky", 
    "profile_picture_url": "http://placehold.it/150x150", 
    "is_admin": true, 
    "is_manager": false, 
    "created_at": "2015-04-04T04:03:50.932471Z", 
    "updated_at": "2015-04-07T18:20:20.098732Z"
}
```

#### Content

#### Bits
