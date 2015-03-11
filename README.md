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

#####Request: GET, POST, PUT, DELETE
```http
/api/v1/account/<pk>/
```

#####Request: GET
```http
/api/v1/account/<pk>/bits/
```

#####Request: GET
```http
/api/v1/me/
```


#### Content

#### Bits
