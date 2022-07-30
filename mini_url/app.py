import os

from dotenv import load_dotenv

load_dotenv()

from mini_url import create_app

application = create_app(os.getenv("FLASK_CONFIG", "production"))
