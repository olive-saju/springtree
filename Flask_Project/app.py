from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        data = request.json
        year = data.get('year')
        month = data.get('month')
        day = data.get('day')
        hour = data.get('hour')
    else:
        year = 1990
        month = 5
        day = 21
        hour = 14

    result = {
        "year_element": "갑",
        "month_element": "을",
        "day_element": "병",
        "hour_element": "정"
    }

    response = Response(
        response=json.dumps(result, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
