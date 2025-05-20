from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    print(data)

    numbers = data.get('numbers', [])
    mode_type = data.get('mode', '').lower()

    response = {
        'numbers': numbers,
        'mode': mode_type
    }

    match mode_type:
        case 'mean':
            response['result'] = mean(numbers)
        case 'median':
            response['result'] = median(numbers)
        case 'mode':
            response['result'] = mode(numbers)
        case _:
            response['error'] = 'Invalid mode type. Please use mean, median, or mode.'

    return jsonify(response)

def mean(array):
    print('Mean function called')
    return sum(array) / len(array)

def median(array):
    print('Median function called')
    array.sort()
    n = len(array)
    mid = n // 2
    if n % 2 == 0:
        return (array[mid - 1] + array[mid]) / 2
    else:
        return array[mid]

def mode(array):
    print('Mode function called')
    frequency = {}
    max_count = 0
    mode_value = None

    for num in array:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_count:
            max_count = frequency[num]
            mode_value = num
    return mode_value

if __name__ == '__main__':
    app.run(port=3000)
