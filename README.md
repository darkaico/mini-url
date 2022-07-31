# Mini Url

Educational project recreating an url shortener service as Bit.ly.

## Run with Docker

```bash
$ docker-compose up
```

Or if you are using `make` just do:

```bash
$ make up
```

The server should be live in http://127.0.0.1:5001/

## Run locally

### Requisites

- Python 3.10.4
- Poetry installed [Resources](https://python-poetry.org/)
- MongoDB running locally [Resources](https://www.mongodb.com/docs/manual/installation/)
- Copy or rename `.env.example` into a new file called `.env` and fill values there (especially the mongo db URI specifying the DB)

#### Example of .env file

```.env
SECRET_KEY=your-super-secret-key
FLASK_CONFIG=development
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/miniUrlDB
```

### Steps

1. Install python dependencies

```bash
$ poetry install
```

2. Shell into virtualenv using poetry

```bash
$ poetry shell
```

3. Start the app

```bash
$ FLASK_APP=mini_url.app flask run -h 0.0.0.0 -p 4000
```

The server should be live in http://127.0.0.1:4000/

### Tests

One you are inside the potery shell you could just run tests body

```bash
$ pytest
```

# API

There are 2 basic endpoints to work with URL resources:

- Generate an URL
- Obtain information from a short url id

## `POST /api/mini-url`

Generate a short url.
Include the `url` you want to short in the body

```json
{
  "url": "https://www.google.com"
}
```

### Example Response

- Status: 201
- Content-Type: "application/json"

```
{
  "id": "RRQuIwk",
  "long_url": "https://www.google.com",
  "created": "2022-07-31T10:06:47.161241",
  "stats": null
}
```

## `GET /api/mini-url/{mini-url-id}`

Get information from an already generated mini url id
Include the `mini url id` generated previously in the url

### Example Response

- Status: 200
- Content-Type: "application/json"

```
{
  "id": "RRQuIwk",
  "long_url": "https://www.google.com",
  "created": "2022-07-31T10:06:47.161241",
  "stats": null
}
```

# Web

There are 2 simple pages in this project, the index just showing a message and the one that will be used as a redirection.

Once you have a mini url id you could go to the url formed as `{{host}}/{{mini url id}}` to verify the redirection

## Example

With the latest case we should go to `http://127.0.0.1:4000/RRQuIwk` and check that we are redirected

## Note

If we get redirected, we could also verify again how is the status of the mini url using the API

`GET /api/mini-url/{mini-url-id}`

And now the response will have basic stats information about it

```
{
  "id": "RRQuIwk",
  "long_url": "https://www.google.com",
  "created": "2022-07-31T10:29:26.301000",
  "stats": {
    "last_time_used": "2022-07-31T10:30:15.537000",
    "total_usage": 1
  }
}
```
