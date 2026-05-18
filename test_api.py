import requests

# ============================================================
# API TESZTEK - JSONPlaceholder (ingyenes teszt API)
# ============================================================
# Telepítés: pip install requests pytest
# Futtatás:  pytest test_api.py -v

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    """GET kérés - felhasználó lekérése"""
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200, f"Várt: 200, Kapott: {response.status_code}"

    data = response.json()
    assert "name" in data, "Hiányzó mező: name"
    assert "email" in data, "Hiányzó mező: email"
    assert "@" in data["email"], "Hibás email formátum"

    print(f"✅ Felhasználó neve: {data['name']}")
    print(f"✅ Email: {data['email']}")


def test_get_all_users():
    """GET kérés - összes felhasználó lekérése"""
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10, f"Várt 10 felhasználó, kapott: {len(data)}"
    print(f"✅ Felhasználók száma: {len(data)}")


def test_create_post():
    """POST kérés - új bejegyzés létrehozása"""
    payload = {
        "title": "Teszt bejegyzés",
        "body": "Ez egy automatikus teszt által létrehozott bejegyzés.",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201, f"Várt: 201, Kapott: {response.status_code}"

    data = response.json()
    assert data["title"] == payload["title"], "A cím nem egyezik!"
    assert "id" in data, "Hiányzó mező: id"
    print(f"✅ Létrehozott bejegyzés ID: {data['id']}")


def test_update_post():
    """PUT kérés - bejegyzés frissítése"""
    payload = {
        "id": 1,
        "title": "Frissített cím",
        "body": "Frissített tartalom.",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Frissített cím", "A cím nem frissült!"
    print(f"✅ Frissített cím: {data['title']}")


def test_delete_post():
    """DELETE kérés - bejegyzés törlése"""
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200, f"Várt: 200, Kapott: {response.status_code}"
    print("✅ Bejegyzés sikeresen törölve!")


def test_not_found():
    """GET kérés - nem létező erőforrás (404 ellenőrzés)"""
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404, f"Várt: 404, Kapott: {response.status_code}"
    print("✅ 404-es hiba helyesen jelenik meg!")
