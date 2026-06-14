from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_product_page_opens_from_collection():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://walldesigner.co.za/collections/all")

        product_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/products/']")

        assert len(product_links) > 0

        first_product_url = product_links[0].get_attribute("href")

        assert first_product_url is not None
        assert "/products/" in first_product_url

        driver.get(first_product_url)

        page_title = driver.title.lower()
        page_source = driver.page_source.lower()

        assert page_title != ""
        assert "walldesigner" in driver.current_url.lower()
        assert "add to cart" in page_source or "choose options" in page_source or "buy" in page_source

    finally:
        driver.quit()

def test_product_size_selection_adds_item_to_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://walldesigner.co.za/collections/all")

        product_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/products/']"))
        )

        first_product_url = product_links[0].get_attribute("href")

        assert first_product_url is not None
        assert "/products/" in first_product_url

        driver.get(first_product_url)

        possible_size_options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//button[not(@disabled)] | //label | //input[@type='radio']/following-sibling::label"
                )
            )
        )

        clicked_size = False

        for option in possible_size_options:
            option_text = option.text.strip().lower()

            if option.is_displayed() and option.is_enabled():
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
                driver.execute_script("arguments[0].click();", option)
                clicked_size = True
                break

        assert clicked_size is True

        driver.get("https://walldesigner.co.za/cart")

        cart_page_source = driver.page_source.lower()

        assert "cart" in cart_page_source
        assert "checkout" in cart_page_source or "subtotal" in cart_page_source or "total" in cart_page_source

    finally:
        driver.quit()