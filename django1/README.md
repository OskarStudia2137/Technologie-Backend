# Django Blog Project - Full Stack & API

Projekt blogowy zrealizowany w ramach kursu programowania backendowego. Aplikacja obejmuje pelna sciezke rozwoju: od definicji bazy danych, przez autoryzacje uzytkownikow, az po profesjonalne API REST-owe.

## Wykorzystane Technologie
* Backend: Django 5.x + Python 3.11
* API: Django REST Framework (DRF)
* Dokumentacja: drf-spectacular (Swagger UI)
* Baza Danych: SQLite
* Frontend: Django Templates + Bootstrap 5
* Grafika: Pillow (obsluga avatar'ów)

## Instrukcja Uruchomienia

1. Przygotowanie srodowiska:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

2. Konfiguracja Bazy Danych:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

3. Uruchomienie serwera:
   python manage.py runserver

---

## Nawigacja po Projekcie
* Strona glowna: http://127.0.0.1:8000/
* Dokumentacja API (Swagger): http://127.0.0.1:8000/api/docs/
* Panel Administratora: http://127.0.0.1:8000/admin/
* Profil uzytkownika: http://127.0.0.1:8000/profile/

---

Uwaga: Pliki bazy danych (db.sqlite3) oraz folder media/ zostaly dodane do pliku .gitignore zgodnie z najlepszymi praktykami.
