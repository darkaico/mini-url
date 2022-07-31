start:
	FLASK_APP=mini_url.app flask run -h 0.0.0.0 -p 4000

lint:
	pre-commit run --all-files

build:
	docker-compose build

up:
	docker-compose up
