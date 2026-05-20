\# QA Portfolio – Tóth Péter



Manuális tesztelő vagyok 2+ év tapasztalattal, jelenleg aktívan tanulom a tesztautomatizálást. Ez a repository a gyakorlati automatizálási munkáimat tartalmazza.



\---



\## Projektek áttekintése



\### 1. test\_api.py – REST API tesztelés



Tesztelt szolgáltatás: JSONPlaceholder – publikus REST API



| Teszteset | Típus | Elvárt eredmény |

|---|---|---|

| Felhasználó lekérése (GET /users/1) | Pozitív | 200 OK, name és email mező megjelenik |

| Összes felhasználó lekérése (GET /users) | Pozitív | 200 OK, pontosan 10 felhasználó érkezik vissza |

| Új bejegyzés létrehozása (POST /posts) | Pozitív | 201 Created, az új bejegyzés ID-ja megjelenik |

| Bejegyzés frissítése (PUT /posts/1) | Pozitív | 200 OK, a frissített cím visszaérkezik |

| Bejegyzés törlése (DELETE /posts/1) | Pozitív | 200 OK |

| Nem létező erőforrás lekérése (GET /users/9999) | Negatív | 404 Not Found |



\### 2. test\_selenium.py – UI / böngészős tesztelés



Tesztelt oldal: \[The Internet](https://the-internet.herokuapp.com) – dedikált Selenium gyakorló oldal



A tesztek a bejelentkezési folyamat teljes körű ellenőrzését végzik, beleértve a pozitív és negatív eseteket, valamint az oldalelemek állapotának vizsgálatát.



| Teszteset | Típus | Elvárt eredmény |

|---|---|---|

| Főoldal betöltése | Pozitív | Az oldal betölt, a cím helyes |

| Sikeres bejelentkezés | Pozitív | Sikeres üzenet jelenik meg |

| Hibás jelszóval való bejelentkezés | Negatív | Hibaüzenet jelenik meg |

| Checkbox állapotának módosítása | Pozitív | A checkbox állapota megváltozik |

| Kijelentkezés | Pozitív | Visszairányítás a bejelentkező oldalra |



\### 3. test\_pytest.py – Egységtesztelés



Tesztelt funkció: Számológép (összeadás, kivonás, szorzás, osztás)



A tesztek lefedik az alap műveleteket, a hibás bemeneteket és a határértékeket. Paraméteres tesztekkel több eset egyszerre kerül ellenőrzésre.



| Teszteset | Típus | Elvárt eredmény |

|---|---|---|

| Alap műveletek (összeadás, kivonás, szorzás, osztás) | Pozitív | Helyes eredmény visszaadva |

| Nullával való osztás | Negatív | ValueError kivétel keletkezik |

| Ismeretlen művelet megadása | Negatív | ValueError kivétel keletkezik |

| Negatív számokkal való szorzás | Határérték | Helyes eredmény visszaadva |

| Paraméteres tesztek (4 eset egyszerre) | Pozitív | Minden eset helyes eredményt ad |



\---



\## Technológiák



| Eszköz | Szint |

|---|---|

| Python | Alapszint – jelenleg aktív fejlesztés alatt |

| Pytest | Alapszint – jelenleg aktív fejlesztés alatt |

| Selenium WebDriver | Alapszint – jelenleg aktív fejlesztés alatt |

| Requests (API tesztelés) | Alapszint – jelenleg aktív fejlesztés alatt |

| JIRA | Tapasztalt – napi szintű használat 2+ éve |

| Manuális tesztelés | Tapasztalt – 2+ év szakmai tapasztalat |



\---



\## Képesítések



\- ISTQB Certified Tester Foundation Level (CTFL)

\- ISTQB AI Testing – folyamatban



\---



\## Kapcsolat



\- Email: petyego@gmail.com

\- LinkedIn: \*(https://www.linkedin.com/in/t%C3%B3th-p%C3%A9ter-050408267/)\*

