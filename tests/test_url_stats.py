from pyourls3 import client, exceptions
import pytest
import tests
import tests.sharevar

# tests for the url specific stats function
@pytest.fixture(scope="module")
def instance():
    c = client.Yourls(tests.sharevar.standard_url, key="12345")
    yield c
    tests.sharevar.modifier = None


def test_e_url_exists(instance):
    with pytest.raises(exceptions.Pyourls3ParamError):
        instance.url_stats("")


def test_e_request_params_correct(instance):
    u = "https://www.google.com"
    instance.url_stats(u)
    assert "shorturl" in tests.sharevar.last_request
    assert tests.sharevar.last_request["shorturl"] == u


def test_e_garbled_json(instance):
    tests.sharevar.modifier = "garbledjson"
    with pytest.raises(exceptions.Pyourls3HTTPError):
        instance.url_stats("https://www.google.com")


def test_e_generic_error(instance):
    tests.sharevar.modifier = "error"
    with pytest.raises(exceptions.Pyourls3APIError):
        instance.url_stats("https://www.google.com")
