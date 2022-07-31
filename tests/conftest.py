import pytest

from mini_url import create_app


@pytest.fixture()
def app():
    app = create_app("testing")

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
