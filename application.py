from flask import Flask, request, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/')
def index():
    # Return each endpoint
    return jsonify({'endpoints': ['/api/calorie_intake', '/api/ideal_weight']}), 200

# Endpoint to calculate calorie intake recommendation
@application.route('/api/calorie_intake', methods=['GET', 'POST'])
def calorie_intake_recommendation():
    if request.method == 'GET':
        height = float(request.args.get('height', None))
        weight = float(request.args.get('weight', None))
    elif request.method == 'POST':
        data = request.get_json()
        height = data.get('height', None)
        weight = data.get('weight', None)
    else:
        return jsonify({'error': 'Invalid HTTP method.'}), 405

    if height is None or weight is None:
        return jsonify({'error': 'Height and weight must be provided.'}), 400

    # Basic formula for estimating calorie intake (Mifflin-St Jeor Equation)
    bmr = 10 * weight + 6.25 * height - 5

    return jsonify({'calorie_intake': bmr}), 200

# Endpoint to calculate ideal weight based on height
@application.route('/api/ideal_weight', methods=['GET', 'POST'])
def ideal_weight():
    if request.method == 'GET':
        height = float(request.args.get('height', None))
    elif request.method == 'POST':
        data = request.get_json()
        height = data.get('height', None)
    else:
        return jsonify({'error': 'Invalid HTTP method.'}), 405

    if height is None:
        return jsonify({'error': 'Height must be provided.'}), 400

    # Basic formula for calculating ideal weight (for males only)
    ideal_weight_male = 50 + 0.91 * (height - 152.4)
    ideal_weight_female = 45.5 + 0.91 * (height - 152.4)

    return jsonify({'ideal_weight_male': ideal_weight_male, 'ideal_weight_female': ideal_weight_female}), 200

if __name__ == '__main__':
    application.run(debug=True)
