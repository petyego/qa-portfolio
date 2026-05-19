from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# ============================================================
# SELENIUM TESZTEK - The Internet (Selenium gyakorló oldal)
# https://the-internet.herokuapp.com
# ============================================================
# Futtatás: python -m pytest test_selenium.py -v

BASE_URL = "https://the-internet.herokuapp.com"


@pytest.fixture
def driver():
    """Chrome böngésző indítása és leállítása minden teszthez"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_fooldal_betolt(driver):
    """Teszt: A főoldal betölt és tartalmazza a helyes címet"""
    driver.get(BASE_URL)

    assert "The Internet" in driver.title, (
        f"Várt 'The Internet' a címben, kapott: {driver.title}"
    )
    print(f"✅ Főoldal betöltve: {driver.title}")


def test_sikeres_bejelentkezés(driver):
    """
    Teszt: Helyes felhasználónévvel és jelszóval
    sikeres bejelentkezés történik
    """
    driver.get(f"{BASE_URL}/login")

    # Felhasználónév és jelszó megadása
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Sikeres belépés ellenőrzése
    sikeres_uzenet = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )

    assert "You logged into a secure area!" in sikeres_uzenet.text, (
        "Sikeres bejelentkezés üzenete nem jelent meg!"
    )
    print(f"✅ Bejelentkezés sikeres: {sikeres_uzenet.text.strip()}")


def test_hibas_bejelentkezés(driver):
    """
    Teszt: Hibás jelszóval a bejelentkezés megtagadva
    és hibaüzenet jelenik meg
    """
    driver.get(f"{BASE_URL}/login")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("rossz_jelszo")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Hibaüzenet ellenőrzése
    hiba_uzenet = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
    )

    assert "Your password is invalid!" in hiba_uzenet.text, (
        "Hibaüzenet nem jelent meg hibás jelszó esetén!"
    )
    print(f"✅ Hibaüzenet helyesen megjelent: {hiba_uzenet.text.strip()}")


def test_checkbox_bepipolas(driver):
    """
    Teszt: Checkbox bepipálható és az állapota
    helyesen változik
    """
    driver.get(f"{BASE_URL}/checkboxes")

    checkboxok = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    # Első checkbox bepipálása (alapból nincs bepipálva)
    elso_checkbox = checkboxok[0]
    assert not elso_checkbox.is_selected(), "Az első checkbox már be volt pipálva!"
    elso_checkbox.click()

    assert elso_checkbox.is_selected(), "A checkbox bepipálása nem sikerült!"
    print("✅ Checkbox sikeresen bepipálva!")


def test_kijelentkezes(driver):
    """
    Teszt: Bejelentkezés után a kijelentkezés
    visszavisz a login oldalra
    """
    driver.get(f"{BASE_URL}/login")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Kijelentkezés gomb megnyomása
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/logout']"))
    ).click()

    # Visszakerültünk a login oldalra
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    assert "/login" in driver.current_url, (
        "Kijelentkezés után nem a login oldalra kerültünk!"
    )
    print("✅ Kijelentkezés sikeres, visszairányítva a login oldalra!")