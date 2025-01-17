from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from alloy_request import make_request

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/validate', methods=['POST'])
def validate():
    response_object = {'status': 'success'}
    data = request.get_json()

    if not data.get('name_first'):
        response_object['status'] = 'error'
        response_object['error'] = 'First name required'
        return jsonify(response_object)

    results = make_request(data)

    response_object['name_first'] = data.get('name_first')
    results_dict = json.loads(results)
    response_object['outcome'] = results_dict.get('summary').get('outcome')
    response_object['name_first'] = data.get('name_first')
    response_object['name_last'] = data.get('name_last')
    
    response_object['supplied_info'] = results_dict.get('supplied')
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()