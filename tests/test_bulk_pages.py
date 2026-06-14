from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def load_urls():
    urls_file = Path("urls.txt")
    urls = urls_file.read_text().splitlines()

    return [url.strip() for url in urls if url.strip()]


@pytest.mark.parametrize("url", load_urls())
def test_store_pages_load_successfully(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url)

        page_title = driver.title
        current_url = driver.current_url.lower()
        page_source = driver.page_source.lower()

        assert page_title != ""
        assert "404" not in page_title.lower()
        assert "page not found" not in page_source
        assert "not found" not in page_title.lower()
        assert "walldesigner.co.za" in current_url

    finally:
        driver.quit()
        
def test_collection_page_displays_products():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://walldesigner.co.za/collections/all")

        page_source = driver.page_source.lower()

        assert "products" in page_source
        assert "wall designer" in page_source
        assert "from r" in page_source
        assert "choose options" in page_source

    finally:
        driver.quit()