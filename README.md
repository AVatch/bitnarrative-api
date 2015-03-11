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
```http
/api/v1/accounts/
```

```http
/api/v1/accounts/create/
```

```http
/api/v1/account/<pk>/
```

```http
/api/v1/account/<pk>/bits/
```

```http
/api/v1/me/
```


#### Content

#### Bits
