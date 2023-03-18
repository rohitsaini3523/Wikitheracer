#create pytest file and run pytest for link validation
import pytest
import requests
from bs4 import BeautifulSoup
from algo import getter_links
def test_getter_links():
    #test for link validation
    url = "https://en.wikipedia.org/wiki/" + "Search"
    response =  requests.get(url)
    #if response status is not 200
    assert response.status_code == 200
    #check if response contains "a" tag
    assert "a" in response.text
    #check if response contains "href" tag
    assert "href" in response.text
    #check if response contains "https://en.wikipedia.org/wiki/" tag
    assert "https://en.wikipedia.org/wiki/" in response.text
test_getter_links()