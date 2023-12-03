## Opis projektu
Projekt ma na celu zaprojektowanie i stworzenie REST API umożliwiającego sterowanie oraz odczytywanie jasności poszczególnych składowych diody RGB podłączonej do Raspberry Pi. API umożliwia zarządzanie jasnością diody LED poprzez wysyłanie żądań HTTP do Raspberry Pi, które pełni rolę serwera.

Program można przetestować przed wgraniem na RPi poprzez `ledAPI.py` tworząc serwer na komputerze lub uruchomić serwer bezpośrednio na RPi poprzez `ledAPIrpi.py`.

## Technologie
W tym projekcie wykorzystano Raspberry Pi jako serwer zarządzajacy diodą LED RGB dzięki bibliotece RPi.GPIO. Do komunikacji pomiędzy serwerem (RPi) a klientem (przeglądarka) wykorzystano protokół HTTP i architekturę REST API.
## Dokumentacja API

### Pobranie aktualnych składowych diody RGB
- endpoint: `GET /api/led` 
- odpowiedź:
```
{
    "red": 100,
    "green": 50,
    "blue": 75
}
```

### Aktualizacja składowych diody RGB
- endpoint: `POST /api/led` 
- żądanie:
```
{
    "red": "100",
    "green": "50",
    "blue": "75"
}
```
- odpowiedź:
```
{
"status": "Zmieniono składowe diodencji."
}
```
## Instrukcja instalacji
1. Stworzenie i aktywacja wirtualnego środowiska
```
python3 -m venv venvLedApi &&
source venvLedApi/bin/activate &&
cd venvLedApi
```

2. Klonowanie repozytorium
```
git clone https://github.com/wojtekbakun/LedAPI.git
```

3. Instalacja dodatkowych bibliotek:
```
pip install -r requirements.txt
```

-  *po skończonej pracy w środowisku wirtualnym należy je dezaktywować za pomocą komendy:* 
```
deactivate
```
## Przewodnik użytkowania
### Testowanie API
W terminalu należy wpisać następującą komendę:
```
python ledAPI.py
```

W odpowiedzi powinien pokazać się następujący komunikat:
```
Serving Flask app 'ledAPI'
Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on http://127.0.0.1:5000
Press CTRL+C to quit
Restarting with stat
Debugger is active!
Debugger PIN: 441-955-257
```

Teraz wpisz w przeglądarce adres z tej linijki:
```
Running on http://127.0.0.1:5000
```

- **Po wpisaniu do przeglądarki endpointa `/api/led/` odczytasz aktualne składowe diody RGB**

Przykładowo w programie Postman można wysłać żądania HTML i sprawdzić odpowiedzi serwera.

### Instalacja serwera na RPi
W terminalu należy wpisać następującą komendę:
```
python ledAPIrpi.py
```

W odpowiedzi powinien pokazać się następujący komunikat:
```
Serving Flask app 'ledAPIrpi'
Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on http://192.168.0.108:5000
Press CTRL+C to quit
Restarting with stat
Debugger is active!
Debugger PIN: 441-955-257
Debugger is active!
Debugger PIN: 396-812-396
```

Teraz wpisz w przeglądarce adres z tej linijki:
```
Running on http://192.168.0.108:5000
```

- **Po wpisaniu do przeglądarki `/api/led/` odczytasz aktualne składowe diody RGB**


## Przykłady korzystania

- Wysłano żądanie `GET http://127.0.0.1:5000/api/led`

![Screenshot 2023-12-03 at 23 15 04](https://github.com/wojtekbakun/LedAPI/assets/129949845/f8bd5675-0c07-43cf-8164-a8e041c490a3)

- Otrzymano odpowiedź:
```
{
"status": "Zmieniono składowe diodencji."
}
```

```
{
"blue": 0,
"green": 0,
"red": 0
}
```

---

- Wysłano żądanie `POST http://127.0.0.1:5000/api/led` z danymi:
```
{
"blue": "01",
"green": "10",
"red": "20"
}
```
- Otrzymano odpowiedź:
```
{
"status": "Zmieniono składowe diodencji."
}
```

- Ponownie wysłano żądanie `GET http://127.0.0.1:5000/api/led` i otrzymano odpowiedź:
```
{
"blue": "01",
"green": "10",
"red": "20"
}
```
