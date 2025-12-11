from unittest.mock import patch

import pytest
import requests

from app.scraper import search_library


@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code != 200:
                raise Exception("HTTP Error")

    return MockResponse(b"", 200)


def test_search_library_success(mock_response):
    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        result = search_library(
            "test",
            "vpl",
            {"vpl": "http://test.com?query={query}"},
            {"vpl": "http://test.com"},
        )
        assert "items" in result


def test_search_library_http_error():
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("HTTP Error")
        result = search_library(
            "test",
            "vpl",
            {"vpl": "http://test.com?query={query}"},
            {"vpl": "http://test.com"},
        )
        assert "error" in result


def test_search_library_invalid_key():
    result = search_library(
        "test",
        "invalid",
        {"vpl": "http://test.com?query={query}"},
        {"vpl": "http://test.com"},
    )
    assert "error" in result
