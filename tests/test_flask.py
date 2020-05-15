import importlib
import sys

import cdiserrors
import flask
import pytest


def test_make_json_error():
    app = flask.Flask(__name__)

    @app.route("/")
    def get():
        return cdiserrors.make_json_error(Exception("James is shot"))

    with app.test_client() as client:
        rv = client.get("/")
        assert rv.status_code == 500
        assert rv.get_json() == dict(message="James is shot")


def test_default_handlers():
    app = flask.Flask(__name__)
    cdiserrors.setup_default_handlers(app)

    @app.route("/")
    def get():
        flask.abort(400, "James is shot again")

    with app.test_client() as client:
        rv = client.get("/")
        assert rv.status_code == 400
        assert rv.get_json() == dict(message="400 Bad Request: James is shot again")


def test(monkeypatch):
    monkeypatch.setitem(sys.modules, "flask", None)
    importlib.reload(cdiserrors)
    try:
        with pytest.raises(NotImplementedError):
            assert cdiserrors.make_json_error(None)
        with pytest.raises(NotImplementedError):
            assert cdiserrors.setup_default_handlers(None)
    finally:
        monkeypatch.undo()
        importlib.reload(cdiserrors)
