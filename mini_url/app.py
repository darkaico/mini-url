import os

from dotenv import load_dotenv

from mini_url import create_app

load_dotenv()


application = create_app(os.getenv("FLASK_CONFIG", "production"))
