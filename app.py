from flask import Flask, request, jsonify
from models import ExpenseManager, SplitType

app = Flask(__name__)
manager = ExpenseManager()

@app.route('/')
def home():
    return jsonify({"status": "Running", "message": "Expense Backend"})

@app.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.json
        user = manager.add_user(data['user_id'], data['name'], data['email'])
        return jsonify({"message": "User created", "user": user.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/expense', methods=['POST'])
def add_expense():
    try:
        data = request.json
        category = data.get('category', 'General')
        manager.create_expense(
            data['split_type'], data['amount'], data['payer_id'], 
            data['splits'], category
        )
        return jsonify({"message": "Expense added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/history', methods=['GET'])
def get_history():
    # FIXED: Changed function name to match models.py
    history = manager.get_history() 
    return jsonify({"history": history})

@app.route('/simplify', methods=['GET'])
def get_simplified_debts():
    return jsonify({"transactions": manager.simplify_debts()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)