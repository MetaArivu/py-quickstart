# Quick Start with FastAPI

## Run the Application

```
$ uvicorn main:app --reload
```

## To Test the App

Request URL: http://localhost:8000/hello

```
$ curl -X 'GET' \
  'http://localhost:8000/hello' \
  -H 'accept: application/json'
```

Request URL: http://localhost:8000/hello/karsh

```
$ curl -X 'GET' \
  'http://localhost:8000/hello/karsh' \
  -H 'accept: application/json'
```

Request URL: http://localhost:8000/food/american

```
$ curl -X 'GET' \
  'http://localhost:8000/food/american' \
  -H 'accept: application/json'
```

Request URL: http://localhost:8000/cuisine/italian

```
$ curl -X 'GET' \
  'http://localhost:8000/cuisine/italian' \
  -H 'accept: application/json'
```

Request URL: http://localhost:8000/coupon/3

```
$ curl -X 'GET' \
  'http://localhost:8000/coupon/3' \
  -H 'accept: application/json'
```

## API Docs

Browser: http://localhost:8000/docs

img

Browser: http://localhost:8000/redoc

img

