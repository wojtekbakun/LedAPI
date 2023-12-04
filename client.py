import requests
def get_led_brightness():
    response = requests.get('http://192.168.0.108:5000/api/led')  
    if response.status_code == 200:
        return response.json()
    else:
        return None

def set_led_brightness(red, green, blue):
    data = {
        "red": red,
        "green": green,
        "blue": blue
    }
    response = requests.post('http://192.168.0.108:5000/api/led', json=data) 
    if response.status_code == 200:
        print("Jasność składowych diody RGB została ustawiona.")
    else:
        print("Błąd podczas ustawiania jasności diody RGB.")

def main():
    print("Podaj jasność dla każdej ze składowych diody RGB (0-100).")
    red = int(input("Czerwony: "))
    green = int(input("Zielony: "))
    blue = int(input("Niebieski: "))

    set_led_brightness(red, green, blue)

    current_brightness = get_led_brightness()
    if current_brightness:
        print(f"Aktualna jasność diody LED RGB: R={current_brightness['red']}, G={current_brightness['green']}, B={current_brightness['blue']}")
    else:
        print("Nie udało się pobrać aktualnej jasności diody LED RGB.")

if __name__ == "__main__":
    main()
