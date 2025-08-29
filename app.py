from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend JS can talk to backend

@app.route('/compare', methods=['POST'])
def compare_prices():
    data = request.get_json()
    product = data.get('product', '').strip()

    if not product:
        return jsonify({"error": "No product name provided"}), 400

    # Mock price data – replace with real API calls later
    prices = [
        {"store": "Amazon", "price": "₹12,999", "link": "https://amazon.in/search?q=" + product},
        {"store": "Flipkart", "price": "₹12,499", "link": "https://flipkart.com/search?q=" + product},
        {"store": "Myntra", "price": "₹12,799", "link": "https://myntra.com/search?q=" + product},
    ]

    return jsonify({"product": product, "prices": prices})

if __name__ == '__main__':
    app.run(debug=True)
