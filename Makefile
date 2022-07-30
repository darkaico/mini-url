start:
	FLASK_APP=mini_url.app flask run

start-gunicorn:
	gunicorn 'mini_url.app'

lint:
	pre-commit run --all-files
