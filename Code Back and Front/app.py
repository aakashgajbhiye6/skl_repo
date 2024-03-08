from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
aws_api_endpoint = 'YOUR_AWS_API_ENDPOINT'  # Replace with your actual AWS API endpoint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Make a request to your AWS API endpoint
        aws_response = requests.post(aws_api_endpoint, json={'text': user_input})

        if aws_response.status_code == 200:
            result = aws_response.json().get('prediction')
            return render_template('index.html', result=result, user_input=user_input)
        else:
            return render_template('index.html', error="Failed to get prediction from AWS", user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)