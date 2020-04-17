# URL Shortener

This is a simple application URL shortener.

## Development

Build the containers with:

- `docker-compose build`

Apply database migrations with:

- `docker-compose run app pipenv run python3 manage.py migrate`

Create the admin user with:

- `docker-compose run app pipenv run python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"`

Providing initial data for models

- `docker-compose run app pipenv run python3 manage.py loaddata initial`

Spin up the containers with:

- `docker-compose -f docker-compose.yml up`

Acess the main app at `localhost:8888`

## Running Tests

- `docker-compose run app pipenv run python3 manage.py test`

## Examples

- Create user
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "usertest", "email": "user@test.com", "password": "usertest", "confirm_password": "usertest", "date_joined": "2020-04-17T00:00"}' \
  http://localhost:8888/users/

...
{"id":3,"username":"usertest","email":"user@test.com","date_joined":"2020-04-17T00:00:00Z","refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NzIyMjA4NCwianRpIjoiZDU0MDEwY2ExOTZkNDVhNzk4ZDIwMmQ3NzQyZmVmMDIiLCJ1c2VyX2lkIjozfQ.sZinAMEEACNH2VlFC7CF3kAkCnoLiQNycCi17tEFD34","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MTM1OTg0LCJqdGkiOiJjZTNhYWRiMzJjOTY0NTQxYTEwYjI0MDg3MDg1YzgwMyIsInVzZXJfaWQiOjN9.VkuMnh04N4GOUGQ0bS-mXwys6ttXP-hIMhCjet5y3zM"}
```

- Login with JWT:
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "usertest", "password": "usertest"}' \
  http://localhost:8888/users/api/token/

...
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

- Refresh token
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8888/api/token/refresh/

...
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"}
```

- URL Shortener (List)
```
curl \
  -X GET \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MTM2NzkyLCJqdGkiOiIwODNjZmQ0YmY1YzQ0YmJlOGYzNjFjMGMyYTc4OTY1YyIsInVzZXJfaWQiOjN9.0oWT-n_blCgPE6-4dSXvfeAYMzpcH1smjxm-zCi2Qq0" \
  http://localhost:8888/c/api/short-url

...
[
    {
        "id":1, 
        "short_url":"http://localhost:8888/c/867nv",
        "slug":"867nv","access_counter": 10, 
        "full_url":"https://www.apply.eu/profile.php"
    },
    {
        "id":2,
        "short_url":"http://localhost:8888/c/25t52",
        "slug":"25t52",
        "access_counter": 5,
        "full_url":"http://www.google.com"
    }
]
```

- URL Shortener (Create)
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MTM3NjE4LCJqdGkiOiI0ZGQ1NjY4NmU1OTM0NzZjYWMwN2ZmM2IwYmMzMTM4OCIsInVzZXJfaWQiOjN9.01OvgqJB4aSbdZZ0e2x6hJWRspgVWCVRWe6qcfY07Yc" \
  -d '{"full_url": "http://www.google.com"}' \
  http://localhost:8888/c/api/short-url

...
{"id":2, "short_url":"http://localhost:8888/c/25t52", "slug":"25t52", "access_counter":0, "full_url":"http://www.google.com"}
```