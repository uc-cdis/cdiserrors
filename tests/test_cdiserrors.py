import importlib
import logging
import sys

import cdiserrors
import pytest


@pytest.fixture(params=[True, False], autouse=True)
def use_flask(request, monkeypatch):
    if not request.param:
        monkeypatch.setitem(sys.modules, "flask", None)
        importlib.reload(cdiserrors)

    yield request.param

    if not request.param:
        monkeypatch.undo()
        importlib.reload(cdiserrors)


def test():
    assert str(cdiserrors.APIError(code="007")) == "[007]"
    assert (
        str(cdiserrors.APIError(code="007", message="James Bond"))
        == "[007] - James Bond"
    )
    assert str(cdiserrors.APINotImplemented("No James")) == "[501] - No James"
    assert str(cdiserrors.NotFoundError("James Missing")) == "[404] - James Missing"
    assert str(cdiserrors.UserError("I'm James")) == "[400] - I'm James"

    class UnsupportedError(cdiserrors.BaseUnsupportedError):
        supported_formats = ["006", "007"]

    assert (
        str(UnsupportedError("005"))
        == "[400] - Format 005 is not supported; supported formats are: 006,007."
    )

    assert (
        str(cdiserrors.AuthError()) == "[403] - You don't have access to this resource"
    )
    assert (
        str(cdiserrors.AuthError("James"))
        == "[403] - You don't have access to this resource: James"
    )

    assert str(cdiserrors.AuthNError()) == "[401]"
    assert str(cdiserrors.AuthNError("James")) == "[401] - Authentication Error: James"

    cdiserrors.AuthZError()
    cdiserrors.InvalidTokenError()

    assert str(cdiserrors.InternalError()) == "[500] - Internal server error"
    assert (
        str(cdiserrors.InternalError("James is sick"))
        == "[500] - Internal server error: James is sick"
    )

    assert (
        str(cdiserrors.ServiceUnavailableError("James is busy"))
        == "[503] - James is busy"
    )

    cdiserrors.ParsingError()

    assert str(cdiserrors.UnhealthyCheck("James is sick")) == "[500] - James is sick"


def test_schema_error(monkeypatch):
    ex = None

    # noinspection PyUnusedLocal
    def exception(self, e):
        nonlocal ex
        ex = e

    monkeypatch.setattr(logging.Logger, "exception", exception)

    assert str(cdiserrors.SchemaError("Suit up")) == "Suit up"
    assert (
        str(cdiserrors.SchemaError("Suit up", Exception("black"))) == "Suit up: black"
    )
    assert str(ex) == "black"
