# Install required packages using pip install flask




from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Mock data for demonstration purposes
users = {
    "user1": {"balance": 1000, "microfinance_limit": 5000},
    "user2": {"balance": 500, "microfinance_limit": 3000},
}

# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/financial-literacy')
def financial_literacy():
    # Add code to display financial literacy content
    return render_template('financial_literacy.html')

@app.route('/balance/<username>')
def check_balance(username):
    user_data = users.get(username)
    if user_data:
        balance = user_data['balance']
        return f"Balance for {username}: ${balance}"
    else:
        return "User not found."

@app.route('/microfinance/<username>', methods=['GET', 'POST'])
def apply_microfinance(username):
    user_data = users.get(username)
    if request.method == 'POST':
        amount_requested = int(request.form['amount'])
        if user_data and amount_requested <= user_data['microfinance_limit']:
            # Implement microfinance approval logic here
            return f"Microfinance request for {username} approved: ${amount_requested}"
        else:
            return "Microfinance request denied. Invalid user or amount exceeds limit."

    return render_template('microfinance.html')

if __name__ == '__main__':
    app.run(debug=True)
