# QA Portfolio – Tóth Péter

Üdvözlöm! Ez a repository az automatizálási tesztelési projektjeimet tartalmazza.  
Manuális tesztelőként 2+ éves tapasztalattal rendelkezem, és jelenleg aktívan tanulom a tesztautomatizálást.

---

## 📁 Projektek

### 1. `test_api.py` – API tesztelés
- **Eszköz:** Python + Requests
- **Tesztelt API:** JSONPlaceholder (publikus teszt API)
- **Lefedett esetek:** GET, POST, PUT, DELETE kérések, státuszkód ellenőrzések, 404 hibakezelés

### 2. `test_selenium.py` – Böngészős tesztelés
- **Eszköz:** Python + Selenium WebDriver
- **Tesztelt oldal:** Google keresés
- **Lefedett esetek:** Oldal betöltés, keresés funkcionalitás, cím változás ellenőrzése, üres keresés kezelése

### 3. `test_pytest.py` – Egységtesztelés
- **Eszköz:** Python + Pytest
- **Tesztelt funkció:** Számológép (összeadás, kivonás, szorzás, osztás)
- **Lefedett esetek:** Alap műveletek, hibakezelés, negatív számok, paraméteres tesztek

---

## 🛠️ Technikai készségek

| Eszköz | Szint |
|---|---|
| Python | Alapszint (tanulás alatt) |
| Pytest | Alapszint |
| Selenium WebDriver | Alapszint |
| API tesztelés (Requests) | Alapszint |
| JIRA | Tapasztalt |
| Manuális tesztelés | Tapasztalt (2+ év) |

---

## 📋 Telepítés és futtatás

### Szükséges telepítések
```bash
pip install pytest requests selenium pytest-html
```

### API tesztek futtatása
```bash
pytest test_api.py -v
```

### Selenium tesztek futtatása
```bash
pytest test_selenium.py -v
```

### Pytest egységtesztek futtatása
```bash
pytest test_pytest.py -v
```

### HTML riport generálása
```bash
pytest test_pytest.py -v --html=riport.html
```

---

## 🎓 Képesítések

- ✅ ISTQB Certified Tester Foundation Level (CTFL)
- 📚 ISTQB AI Testing – folyamatban

---

## 📬 Kapcsolat

- **Email:** petyego@gmail.com  
- **LinkedIn:** *(hamarosan)*
