from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    size = float(data['size'])
    beds = int(data['beds'])
    baths = float(data['baths'])
    zip_code = int(data['zip_code'])

    # Simple prediction logic
    price = (size * 500) + (beds * 20000) + (baths * 15000) + (zip_code % 100) * 1000

    return jsonify({'price': round(price, 2)})

if __name__ == '__main__':
    app.run(debug=True)
