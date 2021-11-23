#  Authentication & Production Server

## Description

- built using Django with Docker containers.

--------------------------------

## TESTING REQUEST TOKENS STEPS

```py
# Install httpie
$ brew update
$ brew install httpie
```

> http :8000/api/token/

```py
HTTP/1.1 405 Method Not Allowed
Allow: POST, OPTIONS
Content-Length: 40
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:02:10 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Method \"GET\" not allowed."
}
```
> http POST  :8000/api/token/

```py
HTTP/1.1 400 Bad Request
Allow: POST, OPTIONS
Content-Length: 79
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:05:38 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "password": [
        "This field is required."
    ],
    "username": [
        "This field is required."
    ]
}
```
> http POST  :8000/api/token/  username=bashar password=*********

```py
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 483
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:08:02 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzA1NTgyLCJpYXQiOjE2Mzc3MDUyODIsImp0aSI6IjYzZTRhOTgxMTljZDRkZTZhOTY1MGIzYzE5ZWYxMzlmIiwidXNlcl9pZCI6M30.qWw79c-qwy2ptSZ5w6N7B4QVxFDn5XWMRXqiHiQZ85I",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzc5MTY4MiwiaWF0IjoxNjM3NzA1MjgyLCJqdGkiOiJhNzhiZGY1MmEwOGU0NzZmOTQzZmU1ZDQyNWM2ZmY3OSIsInVzZXJfaWQiOjN9.dIjuXya7xUPDh6qdyBFv9AnngAETd38yls8EaoFrEBw"
}

```
> http DELETE  :8000/api/v1/Electro/1

```py

HTTP/1.1 401 Unauthorized
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 58
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:13:18 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Cookie, Origin
WWW-Authenticate: Bearer realm="api"
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Authentication credentials were not provided."
}
```
>  http DELETE  :8000/api/v1/Electro/1 "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzA1NTgyLCJpYXQiOjE2Mzc3MDUyODIsImp0aSI6IjYzZTRhOTgxMTljZDRkZTZhOTY1MGIzYzE5ZWYxMzlmIiwidXNlcl9pZCI6M30.qWw79c-qwy2ptSZ5w6N7B4QVxFDn5XWMRXqiHiQZ85I"


```py
HTTP/1.1 401 Unauthorized
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 183
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:22:04 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
WWW-Authenticate: Bearer realm="api"
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "code": "token_not_valid",
    "detail": "Given token not valid for any token type",
    "messages": [
        {
            "message": "Token is invalid or expired",
            "token_class": "AccessToken",
            "token_type": "access"
        }
    ]
}
```
>  http POST  :8000/api/token/refresh refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzc5MTY4MiwiaWF0IjoxNjM3NzA1MjgyLCJqdGkiOiJhNzhiZGY1MmEwOGU0NzZmOTQzZmU1ZDQyNWM2ZmY3OSIsInVzZXJfaWQiOjN9.dIjuXya7xUPDh6qdyBFv9AnngAETd38yls8EaoFrEBw


```py
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 241
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:26:06 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzA2NjY2LCJpYXQiOjE2Mzc3MDUyODIsImp0aSI6IjU3ZWVlMmQ4MTNkNzQ2MjM5Y2FkOWI0M2VhZTgyN2RkIiwidXNlcl9pZCI6M30.Djlkqj2AnF_uBrIDBei0fnxq-VQnZboQlzMlSKkmLqc"
}
```
> http DELETE  :8000/api/v1/Electro/1 "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzA2NjY2LCJpYXQiOjE2Mzc3MDUyODIsImp0aSI6IjU3ZWVlMmQ4MTNkNzQ2MjM5Y2FkOWI0M2VhZTgyN2RkIiwidXNlcl9pZCI6M30.Djlkqj2AnF_uBrIDBei0fnxq-VQnZboQlzMlSKkmLqc"


```py
HTTP/1.1 403 Forbidden
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 63
Content-Type: application/json
Date: Tue, 23 Nov 2021 22:27:18 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "You do not have permission to perform this action."
}

```
> http DELETE  :8000/api/v1/Electro/1 "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzA2NjY2LCJpYXQiOjE2Mzc3MDUyODIsImp0aSI6IjU3ZWVlMmQ4MTNkNzQ2MjM5Y2FkOWI0M2VhZTgyN2RkIiwidXNlcl9pZCI6M30.Djlkqj2AnF_uBrIDBei0fnxq-VQnZboQlzMlSKkmLqc"


```py
HTTP/1.1 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 0
Date: Tue, 23 Nov 2021 22:30:58 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.12
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

```

------------------------------------------------------

## Change log

- **drf_api_-Authentication & Production Server v1** _completed class_33_ `23-11-2021`

## [PR](https://github.com/BasharTaamneh/drf-auth/pull/1)