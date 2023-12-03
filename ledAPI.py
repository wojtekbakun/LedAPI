from flask import Flask, jsonify, request

app = Flask(__name__)

led_brightness = {
    "red": 0,
    "green": 0,
    "blue": 0
}

@app.route('/api/led', methods=['GET'])
def get_led_brightness():
    return jsonify(led_brightness)

@app.route('/api/led', methods=['POST'])
def set_led_brightness():
    data = request.get_json()
    led_brightness['red'] = data['red']
    led_brightness['green'] = data['green']
    led_brightness['blue'] = data['blue']
    return jsonify({"status": "Zmieniono składowe diodencji."})

if __name__ == '__main__':
    app.run(debug=True)
