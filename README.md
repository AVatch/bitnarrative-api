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

####POST
```json
{
  "username":"",
  "password":""
}
```

####Response
```json
{
  "token":""
}
```

### Endpoints

#### Authentication

#### Accounts

#### Content

#### Bits
