import os


def test_app():
    print(f"{os.getenv('AWS_APP_CLIENT_ID')=}")
    assert True
