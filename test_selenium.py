from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest

# ============================================================
# SELENIUM TESZTEK - Google keresés
# Futtatás:
# python -m pytest test_selenium.py -v
# ============================================================


@pytest.fixture
def driver():
    """Chrome böngésző indítása és leállítása minden teszthez"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


def cookie_elfogadas(driver):
    """
    Google cookie popup elfogadása
    """

    try:
        elfogad_gomb = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'Az összes elfogadása') "
                "or contains(., 'Accept all')]"
            ))
        )

        elfogad_gomb.click()

        print("✅ Cookie popup elfogadva!")

    except TimeoutException:
        print("ℹ️ Nem jelent meg cookie popup.")


def test_google_megnyilik(driver):
    """Teszt: A Google főoldal betölt"""

    driver.get("https://www.google.com")

    cookie_elfogadas(driver)

    assert "Google" in driver.title, (
        f"Várt 'Google' a címben, kapott: {driver.title}"
    )

    print(f"✅ Oldal betöltve: {driver.title}")


def test_google_kereses(driver):
    """
    Teszt:
    Google keresés működik és megjelennek az eredmények
    """

    driver.get("https://www.google.com")

    cookie_elfogadas(driver)

    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    search_box.send_keys("ISTQB tesztelés")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    results = driver.find_elements(By.CSS_SELECTOR, "h3")

    assert len(results) > 0, (
        "Hiba: Nem jelent meg egyetlen találat sem!"
    )

    print(f"✅ Keresési eredmények száma: {len(results)}")


def test_google_kereses_cim_valtozik(driver):
    """Teszt: Keresés után az oldal címe megváltozik"""

    driver.get("https://www.google.com")

    cookie_elfogadas(driver)

    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    search_box.send_keys("Python tesztelés")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.title_contains("Python")
    )

    assert "Python" in driver.title, (
        "A keresési kifejezés nem jelent meg a címsorban!"
    )

    print(f"✅ Oldal cím keresés után: {driver.title}")


def test_ures_kereses(driver):
    """Teszt: Üres keresőmező beküldése nem okoz hibát"""

    driver.get("https://www.google.com")

    cookie_elfogadas(driver)

    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    search_box.send_keys(Keys.RETURN)

    assert "google.com" in driver.current_url, (
        "Az oldal elhagyta a Google-t!"
    )

    print("✅ Üres keresés kezelve, az oldal Google-on maradt!")