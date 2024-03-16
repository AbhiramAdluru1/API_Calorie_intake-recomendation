from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/')
def index():
    # Return each endpoint
    return jsonify({'endpoints': ['/api/bmi_category', '/api/calorie_intake', '/api/ideal_weight']}), 200

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

# Endpoint to check BMI category
@application.route('/api/bmi_category', methods=['GET', 'POST'])
def bmi_category():
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

    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        category = 'Underweight'
    elif bmi < 24.9:
        category = 'Normal weight'
    elif bmi < 29.9:
        category = 'Overweight'
    else:
        category = 'Obese'

    return jsonify({'bmi_category': category}), 200

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
