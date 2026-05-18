import pytest

# ============================================================
# PYTEST TESZTEK - Számológép függvény tesztelése
# ============================================================
# Telepítés: pip install pytest pytest-html
# Futtatás:  pytest test_pytest.py -v
# HTML riport: pytest test_pytest.py -v --html=riport.html
# ============================================================


def szamologep(a, b, muvelet):
    """
    Egyszerű számológép függvény.
    Támogatott műveletek: osszeadas, kivonas, szorzas, osztas
    """
    if muvelet == "osszeadas":
        return a + b
    elif muvelet == "kivonas":
        return a - b
    elif muvelet == "szorzas":
        return a * b
    elif muvelet == "osztas":
        if b == 0:
            raise ValueError("Nullával nem lehet osztani!")
        return a / b
    else:
        raise ValueError(f"Ismeretlen művelet: {muvelet}")


# ── Alap műveletek ───────────────────────────────────────────

def test_osszeadas():
    """Összeadás ellenőrzése"""
    assert szamologep(3, 5, "osszeadas") == 8

def test_kivonas():
    """Kivonás ellenőrzése"""
    assert szamologep(10, 4, "kivonas") == 6

def test_szorzas():
    """Szorzás ellenőrzése"""
    assert szamologep(4, 3, "szorzas") == 12

def test_osztas():
    """Osztás ellenőrzése"""
    assert szamologep(10, 2, "osztas") == 5.0


# ── Hibakezelés ──────────────────────────────────────────────

def test_nullaval_osztas():
    """Nullával osztás ValueError-t dob"""
    with pytest.raises(ValueError, match="Nullával nem lehet osztani!"):
        szamologep(10, 0, "osztas")

def test_ismeretlen_muvelet():
    """Ismeretlen művelet ValueError-t dob"""
    with pytest.raises(ValueError, match="Ismeretlen művelet"):
        szamologep(5, 5, "hatvanyas")


# ── Speciális esetek ─────────────────────────────────────────

def test_negativ_szamok():
    """Negatív számokkal való szorzás"""
    assert szamologep(-3, -2, "szorzas") == 6

def test_nulla_hozzaadasa():
    """Nullával való összeadás"""
    assert szamologep(5, 0, "osszeadas") == 5

def test_nagy_szamok():
    """Nagy számok összeadása"""
    assert szamologep(1000000, 2000000, "osszeadas") == 3000000

def test_tizedes_eredmeny():
    """Tizedes eredményt adó osztás"""
    assert szamologep(7, 2, "osztas") == 3.5


# ── Paraméteres tesztek (haladóbb) ───────────────────────────

@pytest.mark.parametrize("a, b, muvelet, elvart", [
    (2, 3, "osszeadas", 5),
    (9, 3, "osztas", 3.0),
    (6, 7, "szorzas", 42),
    (15, 5, "kivonas", 10),
])
def test_parameteres(a, b, muvelet, elvart):
    """Több eset egyszerre tesztelve - paraméteres teszt"""
    assert szamologep(a, b, muvelet) == elvart
