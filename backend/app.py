from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Enable CORS explicitly for this API
CORS(app, resources={r"/analyze-login": {"origins": "*"}})

@app.route('/analyze-login', methods=['POST'])
@cross_origin()
def analyze_login():
    data = request.get_json()

    location = data.get('location', 'same')
    device = data.get('device', 'known')
    time = data.get('time', 'normal')
    failed_attempts = data.get('failed_attempts', 0)

    risk_score = 0
    reasons = []

    if location == 'new':
        risk_score += 30
        reasons.append('New location detected')

    if device == 'unknown':
        risk_score += 20
        reasons.append('Unknown device detected')

    if time == 'odd':
        risk_score += 20
        reasons.append('Login at unusual time')

    if failed_attempts > 3:
        risk_score += 30
        reasons.append(f'Multiple failed attempts ({failed_attempts})')

    if risk_score <= 39:
        risk_level = 'Low'
        recommended_action = 'Allow'
    elif risk_score <= 69:
        risk_level = 'Medium'
        recommended_action = 'Require MFA'
    else:
        risk_level = 'High'
        recommended_action = 'Block'

    return jsonify({
        'risk_score': risk_score,
        'risk_level': risk_level,
        'reasons': reasons,
        'recommended_action': recommended_action
    })

if __name__ == '__main__':
    app.run(debug=True)
