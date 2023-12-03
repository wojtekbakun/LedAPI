from flask import Flask, jsonify, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Ustawienia pinów GPIO dla diody LED RGB
PIN_RED = 11
PIN_GREEN = 12
PIN_BLUE = 13

# Inicjalizacja pinów GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)

# Początkowe wartości jasności składowych diody RGB
led_brightness = {
    "red": 0,
    "green": 0,
    "blue": 0
}

def set_led_color(red, green, blue):
    GPIO.output(PIN_RED, red)
    GPIO.output(PIN_GREEN, green)
    GPIO.output(PIN_BLUE, blue)

@app.route('/api/led', methods=['GET'])
def get_led_brightness():
    return jsonify(led_brightness)

@app.route('/api/led', methods=['POST'])
def set_led_brightness():
    data = request.get_json()
    led_brightness['red'] = data['red']
    led_brightness['green'] = data['green']
    led_brightness['blue'] = data['blue']

    # Obliczenie wypełnienia sygnału PWM na podstawie wartości jasności (0-100)
    red_pwm = (led_brightness['red'] / 100) * 255
    green_pwm = (led_brightness['green'] / 100) * 255
    blue_pwm = (led_brightness['blue'] / 100) * 255

    # Ustawienie jasności składowych diody RGB za pomocą sygnału PWM
    set_led_color(red_pwm, green_pwm, blue_pwm)
    return jsonify({"status": "Zmieniono składowe diodencji."})

if __name__ == '__main__':
    app.run(debug=True)
